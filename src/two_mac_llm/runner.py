from pathlib import Path
import os
import subprocess


def expand(path: str) -> str:
    return os.path.expanduser(path)


def run_local_prompt(llama_cpp_bin: str, model_path: str, prompt: str) -> int:
    llama_cli = Path(expand(llama_cpp_bin)) / "llama-cli"
    model = expand(model_path)

    result = subprocess.run(
        [
            str(llama_cli),
            "-m",
            model,
            "-p",
            prompt,
        ],
        check=False,
    )
    return result.returncode