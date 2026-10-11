#!/usr/bin/env bash
set -euo pipefail
PAPER_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
mkdir -p "$PAPER_DIR/build"
if [[ -n "${PPA_TEX_SUPPORT:-}" ]]; then
  bash "$PPA_TEX_SUPPORT/compile.sh" "$PAPER_DIR/main.tex" "$PAPER_DIR/build" xelatex
elif kpsewhich xelatex.fmt >/dev/null 2>&1 && kpsewhich xeCJK.sty >/dev/null 2>&1; then
  cd "$PAPER_DIR"
  xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
  BIBINPUTS="$PAPER_DIR//:" bibtex build/main
  xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
  xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
else
  SUPPORT_DIR="$PAPER_DIR/tools/tex-support"
  if [[ ! -f "$SUPPORT_DIR/formats/xelatex.fmt" ]]; then
    bash "$SUPPORT_DIR/bootstrap.sh"
  fi
  bash "$SUPPORT_DIR/compile.sh" "$PAPER_DIR/main.tex" "$PAPER_DIR/build" xelatex
fi
cp "$PAPER_DIR/build/main.pdf" "$PAPER_DIR/RLEB_中文修订稿.pdf"
