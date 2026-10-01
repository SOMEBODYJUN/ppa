#!/usr/bin/env bash
set -euo pipefail

# Workspace-local workaround for this image's absent generated TeX databases.
# No package installation or system modification is performed.
build_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
cd "$build_dir"
mkdir -p tex-cache qa
export TEXMF='{/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf}'
export TEXMFVAR="$build_dir/tex-cache"
export TEXMFCONFIG="$build_dir/tex-cache"

if [[ ! -f tex-cache/pdflatex.fmt ]]; then
  (
    cd tex-cache
    pdflatex -ini -etex -interaction=nonstopmode -halt-on-error \
      -jobname=pdflatex pdflatex.ini > format-build.log 2>&1
  )
fi

tex_input='\pdfmapfile{=lm.map}\pdfmapfile{+cm.map}\pdfmapfile{+symbols.map}\input{main.tex}'
for pass in 1 2 3 4; do
  pdflatex -fmt=tex-cache/pdflatex.fmt -jobname=main \
    -interaction=nonstopmode -halt-on-error -file-line-error \
    "$tex_input" > "compile-pass-$pass.log" 2>&1
  if [[ "$pass" == 1 ]]; then
    bibtex main > bibliography-build.log 2>&1
  fi
done

/usr/bin/pdfinfo main.pdf
/usr/bin/pdftoppm -r 85 -png main.pdf qa/page
/usr/bin/pdftotext -layout main.pdf qa/main-layout.txt
