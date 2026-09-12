---
name: create-skill
description: uga-skills組織に新しいClaude Codeスキルを追加する。ユーザーが「スキルを作って」「新しいスキルにして」等と発言した場合に使う。skill-creatorへのバイパスとして動作し、対話でスキルを設計した上で新規GitHubリポジトリを作成・pushし、.github側のREADMEも更新する。
---

# create-skill

`git@github.com:anthropics/skills.git` の `skill-creator` を土台に、uga-skills 組織の運用ルールに沿って新規スキルリポジトリを作るスキル。

## 手順

### 1. skill-creator の準備

このリポジトリ（`.github`）直下の `skills/` ディレクトリに、本家 `anthropics/skills` をクローンする（`.gitignore` 対象）。

```bash
if [ -d skills/.git ]; then
  git -C skills pull --ff-only
else
  git clone git@github.com:anthropics/skills.git skills
fi
```

### 2. スキル設計（軽量フロー）

`skills/skills/skill-creator/SKILL.md` の「Creating a skill」節（Capture Intent / Interview and Research / Write the SKILL.md / Skill Writing Guide）に従い、ユーザーと対話してスキルを設計する。

- デフォルトでは同ファイルの「Running and evaluating test cases」以降（テストケース作成・サブエージェント並列評価・ベンチマーク）は**実施しない**。テストケース数に比例してサブエージェントのトークン消費が増えるため、単純なスキルでは費用対効果が低い。
- ユーザーに「テスト評価・ベンチマークも実施しますか？」と確認し、希望があれば `skills/skills/skill-creator/SKILL.md` の当該節にそのまま従う（`eval-viewer/generate_review.py` を使う、等）。この場合の成果物（テストケース・ベンチマーク結果）はどのリポジトリにもコミットしない。
- 500行目安・progressive disclosure（scripts/references/assets への分離）は必ず踏襲する。

### 3. ローカルにスキル一式を作成

`~/.claude/skills/<name>/` に以下を作成する。

- `SKILL.md` — 本文は英語で書く（日本語よりトークン消費が少ないため）。`description` はユーザーの発話言語（基本は日本語）に合わせる。
- `LICENSE` — MITライセンス。既存スキル（例: `~/.claude/skills/git-commit/LICENSE`）と同じ文面、`Copyright (c) <実行年> Hiroya UGA`。
- `README.md` — 既存スキルと同じ構成（概要・Install・使い方・注意）。frontmatterは以下のフラット形式:

  ```yaml
  ---
  トークン使用量推定値: <数値>
  計測方法: "Anthropic Messages API count_tokens (claude-sonnet-5)"
  ---
  ```

  トークン数は `.github/bin/calc-token.py` で実測する（`ANTHROPIC_API_KEY` が必要。未設定ならユーザーに確認を求め、エラーで止まる）。

  ```bash
  set -a && source /path/to/.github/.env && set +a
  python3 /path/to/.github/bin/calc-token.py ~/.claude/skills/<name>/SKILL.md
  ```

### 4. GitHubリポジトリの作成とpush

```bash
cd ~/.claude/skills/<name>
git init -q
git add SKILL.md README.md LICENSE
git commit -m "Initial commit"
gh repo create uga-skills/<name> --public --source=. --remote=origin --push
```

### 5. `.github/profile/README.md` の更新

以下3箇所に新スキルを反映する。

- 「スキル一覧」の表に1行追加（リンク＋説明はREADME.mdやSKILL.mdのdescriptionと矛盾しないよう要約する）
- 「一括インストール」のシンプルパターン・シンボリックリンクパターン両方に `git clone` / `ln -s` 行を追加
- 「使い方」のスラッシュコマンド例に `/<name>` を追加

編集後、`.github` リポジトリでコミット・pushする。

### 6. 報告

- 作成したリポジトリのURL
- SKILL.mdのトークン数
- `.github` と新規スキルリポジトリ、双方の push 結果（ahead/behind/dirty）

## 禁止事項

- `ANTHROPIC_API_KEY` なしでトークン数を推測値のまま記載すること（必ず実測する）。
- ユーザーの確認なしにベンチマーク評価ループへ進むこと。
- `gh repo create` の可視性をユーザー指示なく `--private` に変更すること（既存スキルは全て `--public`）。
