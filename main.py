#!/usr/bin/env python3
"""Typer CLI entrypoint - uses app.openai_client.send_prompt to talk to OpenAI."""
from typing import Optional
import typer
from langfuse import observe

from app.openai_client import send_prompt, ask_prompt, ConfigError

app = typer.Typer(help="Simple CLI to send a prompt to OpenAI and print the response")

@app.command(name="send")
@observe  # Langfuseのトラッキングを有効化
def send(
    prompt: str = typer.Argument(..., help="Prompt to send to the LLM"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Model to use"),
):
    """Send PROMPT to the configured OpenAI model and print the response."""
    if not prompt or not prompt.strip():
        typer.echo("エラー: 空のプロンプトです。", err=True)
        raise typer.Exit(code=1)

    try:
        answer = send_prompt(prompt, model=model)
        # 回答が\rで区切られないよう削除
        typer.echo(answer.replace('\r', ''))
        return answer
    except ConfigError as ce:
        typer.echo(f"設定エラー: {ce}", err=True)
        raise typer.Exit(code=2)
    except Exception as e:
        typer.echo(f"エラー: {e}", err=True)
        raise typer.Exit(code=1)


@app.command(name="ask")
@observe
def ask(
    prompt: str = typer.Argument(..., help="Question to ask the LLM"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Model to use"),
):
    """Ask PROMPT (friendly) to the configured OpenAI model and print the response."""
    if not prompt or not prompt.strip():
        typer.echo("エラー: 空のプロンプトです。", err=True)
        raise typer.Exit(code=1)

    try:
        answer = ask_prompt(prompt, model=model)
        # 回答が\rで区切られないよう削除
        typer.echo(answer.replace('\r', ''))
    except ConfigError as ce:
        typer.echo(f"設定エラー: {ce}", err=True)
        raise typer.Exit(code=2)
    except Exception as e:
        typer.echo(f"エラー: {e}", err=True)
        raise typer.Exit(code=1)
    return answer


if __name__ == "__main__":
    app()

