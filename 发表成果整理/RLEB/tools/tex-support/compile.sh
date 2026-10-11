#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/env.sh"
if [[ $# -lt 1 || $# -gt 3 ]]; then
  printf 'Usage: %s SOURCE.tex [OUTPUT_DIRECTORY] [xelatex|pdflatex]\n' "$0" >&2
  exit 2
fi
SOURCE_FILE="$(realpath -- "$1")"
SOURCE_DIR="$(dirname -- "$SOURCE_FILE")"
JOB_NAME="$(basename -- "$SOURCE_FILE" .tex)"
OUTPUT_DIR="${2:-$TEX_SUPPORT_ROOT/build/$JOB_NAME}"
mkdir -p -- "$OUTPUT_DIR"
OUTPUT_DIR="$(realpath -- "$OUTPUT_DIR")"
ENGINE="${3:-xelatex}"
case "$ENGINE" in xelatex|pdflatex) ;; *) printf 'Unsupported engine: %s\n' "$ENGINE" >&2; exit 2 ;; esac
export TEXINPUTS="$SOURCE_DIR//:${TEXINPUTS:-}"
export BIBINPUTS="$SOURCE_DIR//:${BIBINPUTS:-}"
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-1791676800}"
export FORCE_SOURCE_DATE=1
export TZ=UTC
run_latex() {
  local pass="$1"
  if ! (cd -- "$SOURCE_DIR" && "$ENGINE" -no-shell-escape -interaction=nonstopmode \
      -halt-on-error -file-line-error -recorder -output-directory="$OUTPUT_DIR" \
      "$SOURCE_FILE") >"$OUTPUT_DIR/$JOB_NAME.pass-$pass.stdout" 2>&1; then
    tail -n 70 "$OUTPUT_DIR/$JOB_NAME.pass-$pass.stdout" >&2
    return 1
  fi
}
run_latex 1
if rg -q '\\bibdata\{' "$OUTPUT_DIR/$JOB_NAME.aux"; then
  if ! (cd -- "$OUTPUT_DIR" && bibtex "$JOB_NAME") >"$OUTPUT_DIR/$JOB_NAME.bibtex.stdout" 2>&1; then
    cat "$OUTPUT_DIR/$JOB_NAME.bibtex.stdout" >&2
    exit 1
  fi
fi
run_latex 2
run_latex 3
if rg -q 'Rerun to get cross-references right|Label\(s\) may have changed' "$OUTPUT_DIR/$JOB_NAME.log"; then
  run_latex 4
fi
printf '%s\n' "$OUTPUT_DIR/$JOB_NAME.pdf"
