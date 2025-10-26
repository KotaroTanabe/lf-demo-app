[WIP]
# What is this
[Langfuse](https://langfuse.com/jp)を試すためのデモ用LLMアプリ

（執筆中）

# Prerequisites
- 動作環境: WSL Ubuntu 24.04
- 前提条件
  - uv
  - docker
  - OpenAI API endpoint + key

# How to start

## Langfuseの起動（ローカル）

([Langfuse](https://langfuse.com/jp)のドキュメントに従う)

```bash
git clone https://github.com/langfuse/langfuse.git
cd langfuse
docker compose up
```

https://localhost:3000/ からアクセス。
Sign Upして適当なアカウントを作成

## Langfuse キー取得
organization, projectを適当に作成する。
Settingsを開き、public key, secret key, urlを取得する。

## LLMアプリ
langfuseによる監視を確認するためのサンプルLLMアプリ。
入力されたプロンプトをLLMに渡し、得られた回答を表示する。

### 環境変数セットアップ

```bash
cp .env.example .env
```

.envにOpenAI, Langfuseの設定（APIキーなど）を入力

### 実行

ルートディレクトリでmain.pyを実行する

```bash
# 入力プロンプトを加工せず送信
uv run python main.py send "<任意のプロンプト>"

# 入力文字列について尋ねる
uv run python main.py ask "<任意のプロンプト>"
# "<任意のプロンプト>とはなんですか？"という文字列が送信される
```

-----------------

# 執筆中