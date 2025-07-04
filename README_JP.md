# Copilot インストラクションジェネレーター

プロジェクトのGitHub Copilotの動作をカスタマイズするためのインストラクションファイルを生成するPythonユーティリティです。

## はじめに

このツールは、GitHub Copilot用の構造化されたインストラクションファイルを生成します。以下の内容が含まれます：
- 学習した教訓とベストプラクティス
- ツールの設定とパス
- タスク計画とスクラッチパッドエリア
- スクリーンショット検証ワークフロー
- Webスクレイピングと検索機能

## セットアップ

### Python仮想環境の作成

1. 新しい仮想環境を作成：
```bash
python -m venv venv
```

2. 仮想環境を有効化：
- macOS/Linuxの場合：
```bash
source venv/bin/activate
```
- Windowsの場合：
```bash
venv\Scripts\activate
```

3. 依存関係のインストール：
```bash
pip install -r requirements.txt
```

## 使用方法

### インストラクションファイルの生成

以下のコマンドを使用してCopilotインストラクションファイルを生成します：

```bash
python generate_copilot_instruction.py --tools-path tools/ --venv-path venv/ --output .github/copilot-instructions.md
```

パラメータ：
- `--tools-path`：ツールディレクトリのパス（デフォルト：tools/）
- `--venv-path`：仮想環境のパス（デフォルト：venv/）
- `--output`：出力ファイル名（デフォルト：global-copilot-instruction.md）

### IDEでの設定

#### Visual Studio Code
1. GitHub CopilotとGitHub Copilot Chat拡張機能をインストール
2. VS Code `settings.json`を開く（Ctrl/Cmd + Shift + P を押して "Open Settings (JSON)" と入力）
3. 以下の設定を追加：
```json
{
    "github.copilot.chat.codeGeneration.instructions": "インストラクションファイルへのパス"
}
```

#### JetBrains IDE
1. GitHub Copilotプラグインをインストール
2. 設定/環境設定を開く
3. Languages & Frameworks > GitHub Copilotに移動
4. "Custom Instructions"セクションを探す
5. 生成したインストラクションファイルのパスを設定

詳細な設定手順については、以下のドキュメントを参照してください：
- [GitHub Copilotドキュメント](https://docs.github.com/ja/copilot)
- [VS Code Copilot拡張機能](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [JetBrains Copilotプラグイン](https://plugins.jetbrains.com/plugin/17718-github-copilot)

## プロンプトの例

Copilot設定をテストするためのプロンプト例：

1. タスク計画：
```
Webスクレイピングとスクリーンショット検証を含む新機能の実装計画を立ててください。
```

2. コード生成：
```
スクリーンショット検証ツールを使用してWebページの外観をキャプチャして検証する関数を作成してください。
```

3. デバッグ支援：
```
日本語テキストを検索する際にエンコーディングエラーが発生しています。どのように修正すればよいですか？
```

4. ベストプラクティス：
```
このプロジェクトで複数行のgitコミットメッセージを扱う推奨方法は何ですか？
```

これらのプロンプトは、生成されたインストラクションファイルで定義されたカスタムインストラクションとツールを組み込んだ応答を引き出します。
