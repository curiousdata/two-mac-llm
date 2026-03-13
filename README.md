# two-mac-llm

Experimental two-Mac distributed inference project.

## Goal
Use:
- Mac 1 as coordinator/main machine
- Mac 2 as worker
- Thunderbolt Bridge for networking
- llama.cpp for inference
- Python for orchestration and utilities

## Planned phases
1. Local llama.cpp run on Mac 1
2. Thunderbolt Bridge connectivity
3. Worker RPC on Mac 2
4. Main-machine orchestration from Python
5. Optional local API / simple app