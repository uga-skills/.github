# uga-skills

[Claude Code](https://claude.ai/code) 向けのスキル集です。

## スキル一覧

| スキル | 説明 |
| --- | --- |
| [git-commit](https://github.com/uga-skills/git-commit) | ステージング済みの変更を見てコミットを試みる。失敗した場合はコミットメッセージを提案する |
| [review-markup](https://github.com/uga-skills/review-markup) | HTML のセマンティクスとアクセシビリティをレビューする |

## 一括インストール

すべてのプロジェクトで使えるよう、ホームディレクトリにインストールする例です。

### シンプルパターン（Claude Code のみ）

```bash
git clone git@github.com:uga-skills/git-commit.git ~/.claude/skills/git-commit
git clone git@github.com:uga-skills/review-markup.git ~/.claude/skills/review-markup
```

### シンボリックリンクパターン（複数ツールで共有）

スキルの実体を `~/.agent/skills/` に置き、`~/.claude/skills/` からシンボリックリンクを張る方法です。他のAIツールとスキルを共有したい場合に適しています。

```bash
git clone git@github.com:uga-skills/git-commit.git ~/.agent/skills/git-commit
git clone git@github.com:uga-skills/review-markup.git ~/.agent/skills/review-markup
ln -s ~/.agent/skills/git-commit ~/.claude/skills/git-commit
ln -s ~/.agent/skills/review-markup ~/.claude/skills/review-markup
```

## 使い方

インストール後、Claude Code のチャットでスキル名をスラッシュコマンドとして実行します。

```
/git-commit
/review-markup
```
