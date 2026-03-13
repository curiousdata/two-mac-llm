#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../vendor/llama.cpp"
cmake -B build -DGGML_METAL=ON
cmake --build build --config Release -j