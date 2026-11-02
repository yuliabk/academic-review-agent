# Academic Review Agent for Codex

Open this repository as a Codex workspace (desktop app / IDE / CLI). Root `AGENTS.md` provides permanent instructions. The skill is in `.agents/skills/academic-peer-review-revision/SKILL.md`.

## Start
1. Clone or open the repository in Codex.
2. Put manuscript files and editor/reviewer letters in `projects/my-paper/input/`. **Do not commit confidential manuscripts into this public repository.** Use a private workspace or untracked local files.
3. Ask: `Use $academic-peer-review-revision to audit projects/my-paper/input, create a reviewer matrix, and write results to projects/my-paper/output. Do not invent missing evidence.`
4. Review outputs. Authorize any submission separately.

You may copy the skill folder to `~/.agents/skills/` to use it globally.

## Verification
Run `python scripts/check_structure.py`. Structural verification does not guarantee academic correctness.

## Privacy
This GitHub repository is PUBLIC. It contains generic instructions and an anonymized methodological case summary only. Never commit unpublished manuscripts, datasets, reviewer correspondence or personally identifiable content.