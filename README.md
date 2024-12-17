# ResponsiveCapture

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

## 概要
**ResponsiveCapture** は、自動化されたウェブサイトのスクリーンショット取得ツールです。異なるビューポートサイズでのスクリーンショットを効率的に取得し、レスポンシブデザインの確認やドキュメンテーションに役立てることができます。Docker環境で動作するため、セットアップが簡単で柔軟なカスタマイズが可能です。

※現在はchromiumにのみ対応

## プロジェクト構成
- `.devcontainer/`
  - Docker開発環境の設定ファイルが含まれます。
  - 主にVS CodeのDev Container設定を管理します。
  
- `config/`
  - プロジェクトの設定ファイルが格納されています。
  - 各種テストケースやブラウザ設定を定義します。
  
- `requirements.txt`
  - 必要なPythonパッケージをリスト化しています。
  - インストールコマンド例：
    ```bash
    pip install -r requirements.txt
    ```

- `logs/`
  - スクリーンショット取得の実行履歴を記録します。
  - 日付ごとのログファイル (`YYYYMMDD.log`) が保存されます。

- `screenshots/`
  - スクリーンショット画像が保存されます。
  - 各テストケースごとにディレクトリが作成され、画面サイズやタイムスタンプが付与されたファイル名で保存されます。

- `scripts/`
  - 自動化処理のためのスクリプトが含まれています。
  - 主なスクリプト:
    - `take_screenshots.py`: スクリーンショット取得のメインスクリプト

- `Dockerfile`
  - プロジェクトのDockerイメージをビルドするための設定ファイルです。

- `docker-compose.yml` (オプション)
  - Docker Composeを使用してコンテナを管理する設定ファイルです。

## 必要条件
- **ソフトウェア**
  - Python 3.8以上
  - Docker
  - Docker Compose (オプション)

- **ハードウェア**
  - ネットワーク接続環境（スクリーンショット対象のウェブサイトにアクセスするため）

## インストール手順

### 1. リポジトリをクローン
```bash
git clone https://github.com/c-a-p-engineer/ResponsiveCapture
cd ResponsiveCapture
```

### 2. Dockerイメージのビルド&起動
```bash
docker build -t responsive-capture . && \
docker run --rm -it -v ".:/workspace:rw" responsive-capture
```

### 4. 設定ファイルのコピーと編集
設定ファイルのサンプルをコピーして、必要に応じて編集します。

```bash
cp config/config.yaml.example config/config.yaml
```

コピー後、`config/config.yaml` を編集し、対象のURLやスクリーンショットの設定を行います。

### 5. スクリプトの実行
コンテナ内で以下のコマンドを実行してスクリーンショットを取得します。

```bash
python scripts/take_screenshots.py
```

#### デバッグモードでの実行
詳細なログを取得するためにデバッグモードで実行します。

```bash
DEBUG=pw:api python scripts/take_screenshots.py
```

### 6. スクリーンショットとログの確認
- **スクリーンショット**: `screenshots/` フォルダに保存されています。各テストケースごとにディレクトリが作成され、ファイル名にテスト名、回数、画面サイズ、タイムスタンプが含まれます。
- **ログファイル**: `logs/YYYYMMDD.log` ファイルに実行履歴やエラーが記録されています。

## カスタマイズ

### 設定変更
`config/` フォルダ内の `config.yaml` ファイルを編集して、テストケースやブラウザ設定をカスタマイズします。

```yaml
browsers:
  - name: chromium
    width: 575
    height: 1080
  - name: chromium
    width: 768
    height: 1080
  # 他のブラウザ設定...

tests:
  - name: チャット詳細
    url: https://www.ugtop.com/spill.shtml
    settings:
      wait_time: 3000
      cookies:
        - name: cookie_name
          value: "cookie_value"
          domain: "www.ugtop.com"
          path: "/"
```

### スクリプト編集
`scripts/` 内のスクリプトを編集して、スクリーンショット取得のロジックや処理内容を変更できます。

## スクリーンショット例
![Sample Screenshot](./screenshots/sample.png)

## トラブルシューティング
- **一部画像が表示されない**
  - ビューポートサイズ変更後の待機時間を増やしてみてください。
  - 非ヘッドレスモードでブラウザを起動し、実際の動作を確認します。
  - ログファイルを確認し、エラーメッセージを参考に問題を特定します。

- **フォントが正しく表示されない**
  - Dockerfileで日本語フォントが正しくインストールされているか確認します。
  - フォントキャッシュを更新して再ビルドします。

## ライセンス
このプロジェクトはMITライセンスのもとで公開されています。詳細は[LICENSE](./LICENSE)ファイルを参照してください。

## 貢献
貢献を歓迎します！以下の手順に従ってください。
1. リポジトリをフォークします。
2. 新しいブランチを作成します。
3. 変更をコミットします。
4. プルリクエストを送信します。

詳細なガイドラインは[CONTRIBUTING.md](./CONTRIBUTING.md)を参照してください。

## サポート
質問やバグ報告は[Issues](https://github.com/c-a-p-engineer/ResponsiveCapture/issues)でお願いします。

## 著者
[こぴぺたん](https://github.com/c-a-p-engineer/)
