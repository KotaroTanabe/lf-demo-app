#!/usr/bin/env python3
"""Typer CLI entrypoint - uses app.openai_client.send_prompt to talk to OpenAI."""
from typing import Optional
import typer

from app.openai_client import send_prompt, ConfigError

app = typer.Typer(help="Simple CLI to send a prompt to OpenAI and print the response")

@app.command()
def send(
    prompt: str = typer.Argument(..., help="Prompt to send to the LLM"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Model to use"),
    timeout: Optional[int] = typer.Option(None, "--timeout", "-t", help="Timeout in seconds"),
):
    """Send PROMPT to the configured OpenAI model and print the response."""
    if not prompt or not prompt.strip():
        typer.echo("エラー: 空のプロンプトです。", err=True)
        raise typer.Exit(code=1)

    try:
        answer = send_prompt(prompt, model=model, timeout=timeout)
        typer.echo(answer)
    except ConfigError as ce:
        typer.echo(f"設定エラー: {ce}", err=True)
        raise typer.Exit(code=2)
    except Exception as e:
        typer.echo(f"エラー: {e}", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
