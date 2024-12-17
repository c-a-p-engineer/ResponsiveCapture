# ベースイメージとしてPythonを使用
FROM mcr.microsoft.com/vscode/devcontainers/python:3.10

# 必要なパッケージのインストール
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y wget unzip

# 日本語フォントのインストール
RUN apt-get install -y fonts-noto-cjk fonts-ipafont-gothic fonts-ipafont-mincho
# 中華フォントを削除
RUN apt-get purge -y fonts-wqy-zenhei

# Playwrightのインストールとブラウザのセットアップ
RUN pip install --no-cache-dir playwright

# Playwrightのブラウザをインストール
RUN playwright install --with-deps

# フォントキャッシュの更新
RUN fc-cache -fv

# 作業ディレクトリの設定
WORKDIR /workspace

# 必要なPythonパッケージのインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# コンテナ起動時にbashをデフォルトシェルに設定
CMD ["bash"]
