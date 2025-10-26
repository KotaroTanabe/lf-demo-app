"""Small wrapper around OpenAI calls using environment variables.

Provides:
- ConfigError: raised when configuration is missing
- send_prompt(prompt, model=None, timeout=None) -> str
"""
from dotenv import load_dotenv
import os
from openai import OpenAI
# from langfuse.openai import OpenAI

load_dotenv()


class ConfigError(Exception):
    pass


def _get_config():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ConfigError("OPENAI_API_KEY が設定されていません。`.env` を作成してください。")
    model = os.getenv("OPENAI_MODEL", "gpt-5-nano")
    timeout_env = os.getenv("OPENAI_TIMEOUT", 30)
    try:
        timeout = int(timeout_env) if timeout_env is not None else None
    except ValueError:
        timeout = None
    return api_key, model, timeout


def send_prompt(prompt: str, model: str | None = None, timeout: int | None = None) -> str:
    """Send the prompt to OpenAI and return the response text.

    Raises ConfigError if API key is missing.
    Raises RuntimeError on network / API errors.
    """
    api_key, default_model, default_timeout = _get_config()
    model = model or default_model
    req_timeout = timeout or default_timeout or 10

    try:
        client = OpenAI()

        response = client.responses.create(
            model=model,
            input=prompt
        )
        content = getattr(response, "output_text", None)

        return (content or "").strip()
    except Exception as e:
        raise RuntimeError(f"通信エラー: {e}")
