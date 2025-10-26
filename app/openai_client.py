"""Small wrapper around OpenAI calls using environment variables.

Provides:
- ConfigError: raised when configuration is missing
- send_prompt(prompt, model=None, timeout=None) -> str
"""
from dotenv import load_dotenv
import os
# from openai import OpenAI
from langfuse.openai import OpenAI  # Langfuseのトラッキング付き
from langfuse import observe

# langfuse, OpenAIの環境変数の読み込み
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


# @observe  # Langfuseのトラッキングを有効化
def send_prompt(prompt: str, model: str | None = None) -> str:
    """Send the prompt to OpenAI and return the response text.

    Raises ConfigError if API key is missing.
    Raises RuntimeError on network / API errors.
    """
    api_key, default_model, default_timeout = _get_config()
    model = model or default_model

    try:
        client = OpenAI()

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Speak in Japanese."},
                {"role": "user", "content": prompt}
            ]
        )
        content = response.choices[0].message.content

        return (content or "").strip()
    except Exception as e:
        raise RuntimeError(f"通信エラー: {e}")


# @observe  # Langfuseのトラッキングを有効化
def ask_prompt(prompt: str, model: str | None = None) -> str:
    """Ask for the prompt to OpenAI and return the response text.

    Raises ConfigError if API key is missing.
    Raises RuntimeError on network / API errors.
    """
    api_key, default_model, default_timeout = _get_config()
    model = model or default_model

    try:
        client = OpenAI()

        user_prompt = "What is {name}?".format(name=prompt)

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Speak in Japanese."},
                {"role": "user", "content": user_prompt}
            ]
        )
        content = response.choices[0].message.content

        return (content or "").strip()
    except Exception as e:
        raise RuntimeError(f"通信エラー: {e}")
