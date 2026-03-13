import subprocess


def ping(host: str) -> int:
    result = subprocess.run(["ping", "-c", "3", host], check=False)
    return result.returncode


def check_port(host: str, port: int) -> int:
    result = subprocess.run(["nc", "-vz", host, str(port)], check=False)
    return result.returncode