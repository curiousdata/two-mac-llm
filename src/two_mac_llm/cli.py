import typer
from rich import print

from two_mac_llm.config import load_config
from two_mac_llm.network import ping, check_port
from two_mac_llm.runner import run_local_prompt

app = typer.Typer()


@app.command()
def netcheck(config_path: str = "config/settings.example.yaml") -> None:
    cfg = load_config(config_path)
    host = cfg["worker"]["host"]
    port = cfg["worker"]["port"]

    print(f"[bold]Pinging {host}[/bold]")
    ping_rc = ping(host)

    print(f"[bold]Checking port {host}:{port}[/bold]")
    port_rc = check_port(host, port)

    print({"ping_rc": ping_rc, "port_rc": port_rc})


@app.command()
def local(config_path: str = "config/settings.example.yaml") -> None:
    cfg = load_config(config_path)
    run_local_prompt(
        llama_cpp_bin=cfg["paths"]["llama_cpp_bin"],
        model_path=cfg["paths"]["model_path"],
        prompt=cfg["runtime"]["prompt"],
    )


if __name__ == "__main__":
    app()