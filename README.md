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

## LLMアプリ
langfuseによる監視を確認するためのサンプルLLMアプリ。
入力されたプロンプトをLLMに渡し、得られた回答を表示する。

### セットアップ
```bash
cp .env.example .env
```
.envのAPIキーを入力

### 実行
ルートディレクトリで以下のように実行
```bash
uv run python main.py "<任意のプロンプト>
# LLMの回答が表示される
```

-----------------

# 執筆中