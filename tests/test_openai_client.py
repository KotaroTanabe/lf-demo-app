import os
from unittest.mock import patch
import pytest

from app.openai_client import send_prompt, ConfigError


def test_send_prompt_no_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(ConfigError):
        send_prompt("hi")


def test_send_prompt_success(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_MODEL", "test-model")

    fake_resp = {"choices": [{"message": {"content": "hello from model"}}]}

    with patch("openai.ChatCompletion.create", return_value=fake_resp):
        out = send_prompt("hi")
        assert "hello from model" in out
