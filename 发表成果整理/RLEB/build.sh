#!/usr/bin/env bash
set -euo pipefail
PAPER_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
mkdir -p "$PAPER_DIR/build"
compile_document() {
  local source_name="$1"
  if [[ -n "${PPA_TEX_SUPPORT:-}" ]]; then
    bash "$PPA_TEX_SUPPORT/compile.sh" "$PAPER_DIR/$source_name.tex" "$PAPER_DIR/build" xelatex
  elif kpsewhich xelatex.fmt >/dev/null 2>&1 && kpsewhich xeCJK.sty >/dev/null 2>&1; then
    (
      cd "$PAPER_DIR"
      xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build "$source_name.tex"
      BIBINPUTS="$PAPER_DIR//:" bibtex "build/$source_name"
      xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build "$source_name.tex"
      xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build "$source_name.tex"
    )
  else
    local support_dir="$PAPER_DIR/tools/tex-support"
    if [[ ! -f "$support_dir/formats/xelatex.fmt" ]]; then
      bash "$support_dir/bootstrap.sh"
    fi
    bash "$support_dir/compile.sh" "$PAPER_DIR/$source_name.tex" "$PAPER_DIR/build" xelatex
  fi
}
compile_document main
cp "$PAPER_DIR/build/main.pdf" "$PAPER_DIR/RLEB_中文修订稿.pdf"
compile_document supplement
cp "$PAPER_DIR/build/supplement.pdf" "$PAPER_DIR/RLEB_中文完整稿.pdf"
