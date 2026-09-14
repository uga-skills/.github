# uga-skills

個人的な[Claude Code](https://claude.ai/code) 向けのスキル置き場です。

## スキル一覧

| スキル | 説明 |
| --- | --- |
| [git-commit](https://github.com/uga-skills/git-commit) | ステージング済みの変更（git diff --cached）を解析してコミットを実行する。失敗した場合はそのまま実行できるコミットコマンドを提案する |
| [git-rebase](https://github.com/uga-skills/git-rebase) | 現在のブランチを指定したブランチの上に rebase する。競合時は git-resolve-conflicts に委譲する |
| [git-merge](https://github.com/uga-skills/git-merge) | 指定したブランチを現在のブランチ（または指定した別ブランチ）に merge する。競合時は git-resolve-conflicts に委譲する |
| [git-resolve-conflicts](https://github.com/uga-skills/git-resolve-conflicts) | rebase/merge で発生したコンフリクトをファイル種別ごとの方針で解決する。git-rebase / git-merge から呼ばれるほか、単体でも、GitHub PR URL を渡しても起動できる |
| [review-markup](https://github.com/uga-skills/review-markup) | HTML のセマンティクスとアクセシビリティを、WHATWG HTML Living Standard・WAI-ARIA・ARIA in HTML・APG Patterns に照らしてレビューする |
| [memory-cleanup](https://github.com/uga-skills/memory-cleanup) | macOS のメモリが重いときに安全に解放する。inactive メモリの purge、メモリ上位プロセスの可視化、Chrome/Safari 等を除外した長時間起動プロセスの候補提示とユーザー確認後の kill を行う |

各スキルのトークン使用量は、それぞれのリポジトリの README.md frontmatter に記載しています（SKILL.md 本文は日本語より少ないトークンで済む英語で記述し、`description` のみユーザーの発話（日本語）に合わせて日本語のままにしています）。

### スキルサイズの目安

Claude Code の [skill-creator](https://github.com/anthropics/skills) が示す目安に沿って、SKILL.md 本文は簡潔に保ち、詳細は必要時にだけ読み込む参照ファイルへ逃がす方針とします。

- **metadata（name + description）**：常にコンテキストに載るため約100語が目安
- **SKILL.md 本文**：スキル発火時のみコンテキストに載るため500行未満が目安。近づく場合は参照ファイルへ分割する
- **参照ファイル（>300行）**：目次を付ける

## 一括インストール

すべてのプロジェクトで使えるよう、ホームディレクトリにインストールする例です。

### シンプルパターン（Claude Code のみ）

```bash
git clone git@github.com:uga-skills/git-commit.git ~/.claude/skills/git-commit
git clone git@github.com:uga-skills/review-markup.git ~/.claude/skills/review-markup
git clone git@github.com:uga-skills/git-rebase.git ~/.claude/skills/git-rebase
git clone git@github.com:uga-skills/git-merge.git ~/.claude/skills/git-merge
git clone git@github.com:uga-skills/git-resolve-conflicts.git ~/.claude/skills/git-resolve-conflicts
git clone git@github.com:uga-skills/memory-cleanup.git ~/.claude/skills/memory-cleanup
```

### シンボリックリンクパターン（複数ツールで共有）

スキルの実体を `~/.agent/skills/` に置き、`~/.claude/skills/` からシンボリックリンクを張る方法です。他のAIツールとスキルを共有したい場合に適しています。

```bash
git clone git@github.com:uga-skills/git-commit.git ~/.agent/skills/git-commit
git clone git@github.com:uga-skills/review-markup.git ~/.agent/skills/review-markup
git clone git@github.com:uga-skills/git-rebase.git ~/.agent/skills/git-rebase
git clone git@github.com:uga-skills/git-merge.git ~/.agent/skills/git-merge
git clone git@github.com:uga-skills/git-resolve-conflicts.git ~/.agent/skills/git-resolve-conflicts
git clone git@github.com:uga-skills/memory-cleanup.git ~/.agent/skills/memory-cleanup
ln -s ~/.agent/skills/git-commit ~/.claude/skills/git-commit
ln -s ~/.agent/skills/review-markup ~/.claude/skills/review-markup
ln -s ~/.agent/skills/git-rebase ~/.claude/skills/git-rebase
ln -s ~/.agent/skills/git-merge ~/.claude/skills/git-merge
ln -s ~/.agent/skills/git-resolve-conflicts ~/.claude/skills/git-resolve-conflicts
ln -s ~/.agent/skills/memory-cleanup ~/.claude/skills/memory-cleanup
```

## 使い方

インストール後、Claude Code のチャットでスキル名をスラッシュコマンドとして実行します。

```
/git-commit
/review-markup
/git-rebase main
/git-merge main
/git-resolve-conflicts
/memory-cleanup
```

## ツール

Claude Code スキルではなく、単体で実行するユーティリティスクリプトです。

- [bin/calc-token.py](../bin/calc-token.py) — 指定したファイルのトークン数を Anthropic Messages API の `count_tokens` で実測します。`ANTHROPIC_API_KEY` が未設定の場合はエラーになります（[.env_template](../.env_template) 参照）。

  ```bash
  export ANTHROPIC_API_KEY=sk-ant-...
  python3 bin/calc-token.py path/to/SKILL.md
  ```
