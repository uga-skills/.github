---
description: uga-skills org の profile/README.md をスキル一覧に基づいて更新する
---

# Skill: update-readme

`gh` コマンドで uga-skills org のリポジトリ一覧を取得し、各リポジトリの SKILL.md を参照して `profile/README.md` を最新の状態に更新する。

## トリガー

- `/update-readme` を実行したとき

## 実行手順

1. Bash で以下を実行し、org のリポジトリ一覧を取得する（`.github` は除外）:

   ```bash
   gh repo list uga-skills --json name,description --limit 100 | jq -r '.[] | select(.name != ".github") | .name'
   ```

2. 各リポジトリについて、SKILL.md の `description` フィールドを取得する:

   ```bash
   gh api repos/uga-skills/{repo}/contents/SKILL.md --jq '.content' | base64 -d | grep '^description:' | sed 's/^description: //'
   ```

3. リポジトリ名からスキル名（コマンド名）を決定する。SKILL.md の `# Skill:` 行があればそちらを優先する:

   ```bash
   gh api repos/uga-skills/{repo}/contents/SKILL.md --jq '.content' | base64 -d | grep '^# Skill:' | sed 's/^# Skill: //'
   ```

4. 取得した情報をもとに `profile/README.md` を以下の構成で書き直す:

```markdown
# uga-skills

[Claude Code](https://claude.ai/code) 向けのスキル集です。

## スキル一覧

| スキル                                           | 説明          |
| ------------------------------------------------ | ------------- |
| [スキル名](https://github.com/uga-skills/{repo}) | {description} |
| ...                                              | ...           |

## 一括インストール

すべてのプロジェクトで使えるよう、ホームディレクトリにインストールする例です。

### シンプルパターン（Claude Code のみ）

\`\`\`bash
git clone git@github.com:uga-skills/{repo}.git ~/.claude/skills/{skill-name}
...
\`\`\`

### シンボリックリンクパターン（複数ツールで共有）

スキルの実体を `~/.agent/skills/` に置き、`~/.claude/skills/` からシンボリックリンクを張る方法です。他のAIツールとスキルを共有したい場合に適しています。

\`\`\`bash
git clone git@github.com:uga-skills/{repo}.git ~/.agent/skills/{skill-name}
...
ln -s ~/.agent/skills/{skill-name} ~/.claude/skills/{skill-name}
...
\`\`\`

## 使い方

インストール後、Claude Code のチャットでスキル名をスラッシュコマンドとして実行します。

\`\`\`
/{skill-name}
...
\`\`\`
```

5. Write ツールで `profile/README.md` を上書き保存する。

## 注意

- `description` が取得できないリポジトリはスキップしてよい
- スキル名（コマンド名）は SKILL.md の `# Skill:` 行から取得する。存在しない場合はリポジトリ名をそのまま使う
- `~/.claude/skills/{skill-name}` のパスはスキル名（コマンド名）に合わせる
