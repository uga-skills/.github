---
name: update-skill
description: uga-skills組織の既存Claude Codeスキル（git-commit, git-rebase, git-merge, git-resolve-conflicts, review-markup等）を、skill-creatorの改善方針に従って更新する。ユーザーが「このスキルを直して」「〇〇スキルをアップデートして」等と発言した場合に使う。
---

# update-skill

`~/.claude/skills/<name>/` にある既存スキルを、skill-creator の改善方針に沿って更新するスキル。

## 手順

### 1. skill-creator の準備

`.github` リポジトリ直下の `skills/` に本家 `anthropics/skills` をクローン済みか確認し、なければクローン、あれば最新化する（`create-skill` の手順1と同じ）。

```bash
if [ -d skills/.git ]; then
  git -C skills pull --ff-only
else
  git clone git@github.com:anthropics/skills.git skills
fi
```

### 2. 対象スキルの特定とスナップショット

- 対象は `~/.claude/skills/<name>/`。存在しなければユーザーに確認する。
- 変更前の状態を一時ディレクトリにコピーしておく（あとで比較評価する場合の baseline、および作業ミス時の復元用）。

  ```bash
  cp -r ~/.claude/skills/<name> /tmp/<name>-before
  ```

### 3. 改善方針の検討

`skills/skills/skill-creator/SKILL.md` の「Improving the skill」節（How to think about improvements / The iteration loop）に従う。

- ユーザーからの具体的な要望（バグ・不足している分岐・トリガー精度など）を起点に、SKILL.md本文を修正する。
- descriptionを変更する場合は「Description Optimization」節の考え方（発火条件を明示的かつやや押し出し気味に書く）を踏まえる。
- デフォルトでは評価ループ（テストケース・サブエージェント比較・ベンチマーク）は実施しない。ユーザーに「旧版と比較するベンチマークも取りますか？」と確認し、希望があれば同ファイルの「Running and evaluating test cases」以降に従い、`/tmp/<name>-before` を baseline として使う。成果物はコミットしない。

### 4. トークン数の再計測

SKILL.mdを変更した場合は必ず `.github/bin/calc-token.py` で再計測し、README.mdのfrontmatterを更新する。

```bash
set -a && source /path/to/.github/.env && set +a
python3 /path/to/.github/bin/calc-token.py ~/.claude/skills/<name>/SKILL.md
```

```yaml
---
トークン使用量推定値: <再計測値>
計測方法: "Anthropic Messages API count_tokens (claude-sonnet-5)"
---
```

### 5. コミット・push

`~/.claude/skills/<name>/` はそのリポジトリ自身が作業コピーなので、そのままコミットし `origin main` へpushする。

### 6. `.github/profile/README.md` の反映

説明文（表・使い方セクション）が変わる更新の場合のみ、該当箇所を合わせて修正しコミット・pushする。挙動は変えたがユーザー向けの説明文は変わらない更新（バグ修正等）では触らない。

### 7. 報告

- 変更差分の要約
- 再計測後のトークン数（変化があれば旧値との比較）
- 対象スキルリポジトリと（触った場合は）`.github` リポジトリ、双方の push 結果（ahead/behind/dirty）

## 禁止事項

- ユーザーの確認なしにベンチマーク評価ループへ進むこと。
- SKILL.mdを変更したのにトークン数を再計測せず古い値のまま残すこと。
- `/tmp/<name>-before` のスナップショットを使わずに独断で `git checkout --` 等の破壊的操作で元に戻そうとすること（作業ツリーの復元が必要な場合は先にユーザーへ確認する）。
