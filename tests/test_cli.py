from typer.testing import CliRunner
from main import app
from unittest.mock import patch


def test_cli_send_success():
    runner = CliRunner()
    # patch the imported send_prompt in main
    with patch("main.send_prompt", return_value="Mocked response"):
        result = runner.invoke(app, ["send", "Hello"])
        assert result.exit_code == 0
        assert "Mocked response" in result.output


def test_cli_send_empty():
    runner = CliRunner()
    result = runner.invoke(app, ["send", "   "])
    assert result.exit_code != 0
