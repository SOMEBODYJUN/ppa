#!/usr/bin/env python3
"""Rebuild the isolated TeX environment from checksum-locked sources."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import zipfile

root = Path(__file__).resolve().parent
for relative in ('downloads', 'sources', 'formats', 'build', 'var', 'config', 'cache', 'var/fonts'):
    (root / relative).mkdir(parents=True, exist_ok=True)
manifest = json.loads((root / 'dependencies.json').read_text())
for dep in manifest['dependencies']:
    archive = root / 'downloads' / dep['file']
    if not archive.exists():
        temporary = archive.with_suffix('.download')
        subprocess.run(['curl', '-L', '--fail', '--retry', '2', '--connect-timeout', '15',
                        '--max-time', '120', dep['url'], '-o', str(temporary)], check=True)
        temporary.replace(archive)
    actual = hashlib.sha256(archive.read_bytes()).hexdigest()
    if actual != dep['sha256']:
        raise SystemExit(f'Checksum mismatch: {archive}; expected {dep["sha256"]}, got {actual}')
    with zipfile.ZipFile(archive) as bundle:
        bundle.extractall(root / 'sources')

base = root / 'sources' / 'ctex-kit-ctex-v2.5.10'
environment = os.environ.copy()
environment['TEXINPUTS'] = str(base / 'support') + '//:'
environment['LUAINPUTS'] = str(base / 'support') + '//:'
for package in ('ctex', 'xeCJK', 'zhnumber'):
    directory = base / package
    # Expand the official archive snapshot identity through upstream ctxdocstrip.
    (directory / f'{package}.id').write_text(
        f'$Id: {package}.dtx 13a2256 2022-07-14 03:54:08 +0000 CTeX upstream snapshot $\n')
    if package == 'xeCJK':
        command = ['xetex', '-ini', '-etex', f'-jobname={package}', '-interaction=nonstopmode',
                   '-halt-on-error', rf'\input plain \input {package}.dtx']
    else:
        command = ['luatex', '-ini', f'-jobname={package}', '-interaction=nonstopmode', '-halt-on-error',
                   rf'\input plain \directlua{{tex.enableprimitives("",tex.extraprimitives())}} \input {package}.dtx']
    with (directory / 'unpack.stdout').open('w') as stream:
        subprocess.run(command, cwd=directory, env=environment, stdout=stream,
                       stderr=subprocess.STDOUT, check=True)
    target = root / 'texmf' / 'tex' / 'latex' / package
    target.mkdir(parents=True, exist_ok=True)
    for source in directory.iterdir():
        if source.suffix in {'.cls', '.sty', '.def', '.clo', '.cfg', '.fd', '.dict', '.spa'}:
            shutil.copy2(source, target / source.name)

font_target = root / 'texmf' / 'fonts' / 'opentype' / 'public' / 'fandol'
font_target.mkdir(parents=True, exist_ok=True)
for source in (root / 'sources' / 'fandol').iterdir():
    if source.suffix == '.otf' or source.name in {'COPYING', 'README'}:
        shutil.copy2(source, font_target / source.name)
map_target = root / 'texmf' / 'fonts' / 'map' / 'pdftex' / 'local'
map_target.mkdir(parents=True, exist_ok=True)
map_files = [Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts') / filename
             for filename in ('cm.map', 'cmextra.map', 'latxfont.map', 'symbols.map', 'euler.map')]
map_files.append(Path('/usr/share/texmf/fonts/map/dvips/lm/lm.map'))
(map_target / 'pdftex.map').write_text(
    '% Isolated PDFTeX map from installed TeX Live 2023 font maps.\n' +
    '\n'.join(path.read_text() for path in map_files))

for engine, program in (('xetex', 'xelatex'), ('pdftex', 'pdflatex')):
    with (root / 'formats' / f'{program}-format.stdout').open('w') as stream:
        subprocess.run([engine, '-ini', '-etex', f'-progname={program}', f'-jobname={program}',
                        '-interaction=nonstopmode', '-halt-on-error', f'{program}.ini'],
                       cwd=root / 'formats', stdout=stream, stderr=subprocess.STDOUT, check=True)
print('Isolated TeX environment rebuilt:', root)
