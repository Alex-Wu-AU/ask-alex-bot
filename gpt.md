# 📝 Ask Alex Master Rulebook (`gpt.md`)

High-level policies only. Implementation detail lives in `plan.md` and stage prompt files.

---

## 1. Purpose (What & Why)

> **Summary:** Authoritative answers first; escalate safely when uncertain; evolve in controlled stages.

Single-source rules for the Ask Alex staged Q&A assistant: authoritative post answers first, safe escalation when uncertain, reproducible development cadence.

---

## 2. Tech Stack (Snapshot)

> **Keep lean until required.**

- **Backend:** FastAPI (Python 3.11)
- **Data (v1):** CSV / Google Sheet (future DB swap)
- **AI:** OpenAI Chat + Embeddings
- **Ops:** Docker (later CI)
- **Integration (later):** Microsoft Teams

---

## 3. Core Principles (Guiding Behaviors)

> **Operate small → verify → harden.**

1. **Stage order only** – never skip ahead.
2. **Minimum first** – build the smallest working piece.
3. **Test + doc every change** – even trivial.
4. **Determinism** – stable prompts, reproducible inputs.
5. **Human guardrails** – no silent AI fabrication.
6. **Mockable boundaries** – AI & IO behind abstractions.

---

## 4. Minimal Project Structure (Early Target)

> **Expand only through stage prompts.**

```
ask-alex-bot/
  app/            # runtime code (expand gradually)
  stage_prompts/  # per-stage detailed instructions
  docs/           # STATUS, plan, rulebook
  tests/          # per-stage verification
  requirements.txt
  README.md
```

Structure grows only via stage prompts; no speculative folders.

---

## 5. Stage Execution Rules (Flow)

> **Rhythm:** define → implement → test → document → commit.

Stage prompt defines scope → implement → run quick test → update `STATUS.md` → commit. Do **not** jump ahead. Promote only durable rules back into this file.

---

## 6. Naming & Conventions (Consistency)

> **Clarity > cleverness.**

- **Files / funcs:** `snake_case`
- **Models / classes:** `PascalCase`
- **Constants & env:** `UPPER_SNAKE` (e.g. `OPENAI_API_KEY`, `ANSWER_THRESHOLD`)
- **Routes:** short & literal (`/ask`, `/stats`)
- **Logs:** `snake_case` keys (fixed)
- **Settings module:** `config.py`
- **Branches:** `stageN-short-desc` (e.g. `stage2-embeddings`)

---

## 7. Escalation Philosophy (Fallback Logic)

> **Answer if confident; otherwise escalate transparently.**

If similarity ≥ answer threshold: return matched post. Otherwise attempt lightweight category guess; if weak, escalate generically (prefer human). AI fallback allowed only once explicitly enabled in its stage. No silent invention.

---

## 8. Core Thresholds (Tunable, Defaults)

> **Policy values; tune only via stage prompt unless policy changes.**

| Name                 | Default | Meaning                                                 |
| -------------------- | ------- | ------------------------------------------------------- |
| `ANSWER_THRESHOLD`   | 0.80    | Minimum similarity to return matched post               |
| `CATEGORY_THRESHOLD` | 0.60    | Below → category becomes `unknown` & generic escalation |

Adjust via stage prompt; update here only if philosophy changes.

---

## 9. Documentation Discipline (Updates)

> **Docs reflect current truth; no drift.**

Update `STATUS.md` after each checklist item. Edit this rulebook **only** for durable policy or naming shifts. Keep tactical how-to in stage prompt + `plan.md`.

---

## 10. Out-of-Scope (MVP Guardrails)

> **Intentionally delayed to reduce noise.**

Authentication, multi-tenancy, advanced dashboards, streaming responses, complex RBAC, heavy observability.

---

## 11. Change Log (Policy-Level Only)

- Initial concise policy set (previous detailed sections pruned)
- Added threshold table (Section 8) & explicit escalation philosophy (Section 7)
- Fixed constant typo (SIMILARITY_THRESHOLD) & locked log style to snake_case
- Added readability highlights & table formatting (Sections 1–10)
