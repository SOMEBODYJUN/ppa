#!/usr/bin/env bash
# Source this file before running TeX. All generated state stays in tex-support.
TEX_SUPPORT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
export TEX_SUPPORT_ROOT
export TEXMF="{$TEX_SUPPORT_ROOT/texmf,$TEX_SUPPORT_ROOT/var,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
export TEXMFHOME="$TEX_SUPPORT_ROOT/texmf"
export TEXMFVAR="$TEX_SUPPORT_ROOT/var"
export TEXMFCONFIG="$TEX_SUPPORT_ROOT/config"
export TEXFORMATS="$TEX_SUPPORT_ROOT/formats:"
export TEXMFOUTPUT="$TEX_SUPPORT_ROOT/build"
export VARTEXFONTS="$TEX_SUPPORT_ROOT/var/fonts"
export XDG_CACHE_HOME="$TEX_SUPPORT_ROOT/cache"
