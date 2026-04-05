# uga-skills

[Claude Code](https://claude.ai/code) 向けのスキル集です。各スキルは Git サブモジュールとしてプロジェクトに追加して使用します。

## スキル一覧

| スキル                                                                       | 説明                                                                                       |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [create-commit-message](https://github.com/uga-skills/create-commit-comment) | ステージング済みの変更を解析し、`git commit` コマンドを提案する                            |
| [review-markup](https://github.com/uga-skills/review-markup)                 | WHATWG・WAI-ARIA などの仕様に照らし、HTML のセマンティクスとアクセシビリティをレビューする |

## 一括インストール

```bash
git submodule add git@github.com:uga-skills/create-commit-comment.git .claude/skills/create-commit-message
git submodule add git@github.com:uga-skills/review-markup.git .claude/skills/review-markup
```

## 使い方

インストール後、Claude Code のチャットでスキル名をスラッシュコマンドとして実行します。

```
/create-commit-message
/review-markup
```
