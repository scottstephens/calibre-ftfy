#!/usr/bin/env bash

venv=$(poetry env info --path)
packages="$venv/Lib/site-packages"

rm -rf deps
mkdir -p deps
cp -R "$packages/ftfy" deps
cp -R "$packages/wcwidth" deps
find deps -name "__pycache__" -exec rm -rf ./{} \;