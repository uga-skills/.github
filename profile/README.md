# uga-skills

[Claude Code](https://claude.ai/code) 向けのスキル集です。

## スキル一覧

| スキル | 説明 | トークン概算 |
| --- | --- | --- |
| [git-commit](https://github.com/uga-skills/git-commit) | ステージング済みの変更（git diff --cached）を解析してコミットを実行する。失敗した場合はそのまま実行できるコミットコマンドを提案する | ![tokens](https://img.shields.io/badge/tokens-529-blue) |
| [review-markup](https://github.com/uga-skills/review-markup) | HTML のセマンティクスとアクセシビリティを、WHATWG HTML Living Standard・WAI-ARIA・ARIA in HTML・APG Patterns に照らしてレビューする | ![tokens](https://img.shields.io/badge/tokens-8035-blue) |
| [git-rebase](https://github.com/uga-skills/git-rebase) | 現在のブランチを指定したブランチの上に rebase する。競合時は git-resolve-conflicts に委譲する | ![tokens](https://img.shields.io/badge/tokens-943-blue) |
| [git-merge](https://github.com/uga-skills/git-merge) | 指定したブランチを現在のブランチ（または指定した別ブランチ）に merge する。競合時は git-resolve-conflicts に委譲する | ![tokens](https://img.shields.io/badge/tokens-941-blue) |
| [git-resolve-conflicts](https://github.com/uga-skills/git-resolve-conflicts) | rebase/merge で発生したコンフリクトをファイル種別ごとの方針で解決する。git-rebase / git-merge から呼ばれるほか、単体でも、GitHub PR URL を渡しても起動できる | ![tokens](https://img.shields.io/badge/tokens-2516-blue) |

トークン概算値は SKILL.md を `cl100k_base` エンコーディングで計測したものです（`git-commit` のみ Anthropic Messages API の `count_tokens` による実測値、それ以外は [bin/calc-token.py](../bin/calc-token.py) による概算）。

## 一括インストール

すべてのプロジェクトで使えるよう、ホームディレクトリにインストールする例です。

### シンプルパターン（Claude Code のみ）

```bash
git clone git@github.com:uga-skills/git-commit.git ~/.claude/skills/git-commit
git clone git@github.com:uga-skills/review-markup.git ~/.claude/skills/review-markup
git clone git@github.com:uga-skills/git-rebase.git ~/.claude/skills/git-rebase
git clone git@github.com:uga-skills/git-merge.git ~/.claude/skills/git-merge
git clone git@github.com:uga-skills/git-resolve-conflicts.git ~/.claude/skills/git-resolve-conflicts
```

### シンボリックリンクパターン（複数ツールで共有）

スキルの実体を `~/.agent/skills/` に置き、`~/.claude/skills/` からシンボリックリンクを張る方法です。他のAIツールとスキルを共有したい場合に適しています。

```bash
git clone git@github.com:uga-skills/git-commit.git ~/.agent/skills/git-commit
git clone git@github.com:uga-skills/review-markup.git ~/.agent/skills/review-markup
git clone git@github.com:uga-skills/git-rebase.git ~/.agent/skills/git-rebase
git clone git@github.com:uga-skills/git-merge.git ~/.agent/skills/git-merge
git clone git@github.com:uga-skills/git-resolve-conflicts.git ~/.agent/skills/git-resolve-conflicts
ln -s ~/.agent/skills/git-commit ~/.claude/skills/git-commit
ln -s ~/.agent/skills/review-markup ~/.claude/skills/review-markup
ln -s ~/.agent/skills/git-rebase ~/.claude/skills/git-rebase
ln -s ~/.agent/skills/git-merge ~/.claude/skills/git-merge
ln -s ~/.agent/skills/git-resolve-conflicts ~/.claude/skills/git-resolve-conflicts
```

## 使い方

インストール後、Claude Code のチャットでスキル名をスラッシュコマンドとして実行します。

```
/git-commit
/review-markup
/git-rebase main
/git-merge main
/git-resolve-conflicts
```

## ツール

Claude Code スキルではなく、単体で実行するユーティリティスクリプトです。

- [bin/calc-token.py](../bin/calc-token.py) — 指定したファイルのトークン数を `cl100k_base` で概算します。

  ```bash
  python3 bin/calc-token.py path/to/SKILL.md
  ```
