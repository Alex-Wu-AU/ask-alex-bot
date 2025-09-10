# Stage 1 – FastAPI Skeleton (Prompt Pack)

> Purpose: This file is a step‑by‑step prompt collection you can feed to an AI assistant to reproduce the Stage 1 skeleton exactly. Policies live in `gpt.md`; this file focuses on actionable generation.

---

## Global Context (Give to AI Once Up Front)

```
You are assisting in building the first stage of a staged project called "Ask Alex".
Return only what is asked per prompt. Do not add extra commentary unless explicitly requested.
High‑level policies come from gpt.md (authoritative answers first, staged development, no premature complexity).
Stage 1 goal: Minimal FastAPI service with a single /ask POST endpoint returning a deterministic placeholder JSON.
No AI (OpenAI) integration yet. No logging layer, no database, no embeddings.
Keep everything minimal, clean, and reproducible.
Use Python 3.12. Manage dependencies with requirements.txt.
Follow naming conventions: snake_case files, PascalCase models, UPPER_SNAKE constants.
All responses must be idempotent—running generated commands twice should not break the workspace.
```

---

## Prompt 1 – Project Scaffold

**When to Use:** Starting from an empty directory (or validating structure).  
**Goal:** Create minimal folder + base files without extra tooling.

```
Act as a shell architect. Generate a list of shell commands to:
1. Create project root files: README.md .gitignore requirements.txt
2. Create folders: app tests
3. Inside app create __init__.py and main.py (empty for now)
4. Initialize git (if not already) – skip if .git exists
5. (Optional) Create a virtual environment named .venv (Python 3.12)
Return ONLY a fenced bash block. No explanations.
```

**Success Criteria:** After execution, tree shows: `app/__init__.py`, `app/main.py`, `tests/`, and base files.

---

## Prompt 2 – Implement Placeholder Endpoint

**Goal:** Populate `app/main.py` with FastAPI app + `/ask` endpoint.

```
Write the complete content for app/main.py.
Requirements:
- Import FastAPI and Pydantic BaseModel
- Define QuestionRequest { question: str }
- Instantiate FastAPI() as app
- Implement POST /ask that accepts QuestionRequest and returns JSON:
  { "message": "Hello, Ask Alex is working", "source_type": "placeholder" }
- No business logic, no external calls, no global state beyond app instance.
Return ONLY a fenced python block with the file content.
```

**Success Criteria:** `uvicorn app.main:app --reload` starts; POST to `/ask` returns expected JSON.

---

## Prompt 3 – Minimal Dependencies

**Goal:** Populate `requirements.txt` with only what is needed now.

```
Provide a minimal requirements.txt for the current stage.
Include: fastapi, uvicorn, pydantic
No version pins unless strongly justified. No test dependencies yet.
Return ONLY a fenced text block.
```

**Success Criteria:** `pip install -r requirements.txt` succeeds; server runs.

---

## Prompt 4 – Basic Test (Optional but Recommended)

**Goal:** Introduce a minimal test to establish verification pattern.

```
Create tests/test_ask_placeholder.py content.
Use fastapi.testclient.TestClient.
Test that POST /ask returns 200 and JSON contains keys: message, source_type='placeholder'.
Return ONLY a fenced python block.
```

**Success Criteria:** After adding pytest to requirements, `pytest -q` passes.

---

## Prompt 5 – Extend Requirements for Testing (If Test Added)

**Goal:** Append testing libs without bloating earlier stage.

```
Return an updated requirements.txt that adds pytest ONLY IF not already present.
Preserve existing lines. Do not add unused libraries.
Return ONLY a fenced text block.
```

**Success Criteria:** pytest available; previous runtime unaffected.

---

## Prompt 6 – Run & Verify Checklist

**Goal:** Provide a concise run + verify set.

```
Output a concise, ordered checklist (no code blocks) to verify Stage 1:
- Create / activate venv
- Install dependencies
- Run uvicorn
- Curl or HTTPie POST example
- Expected JSON response
Keep it to <=7 bullets.
```

**Success Criteria:** Human can follow list and confirm success quickly.

---

## Prompt 7 – Documentation Update Snippet

**Goal:** Provide a ready-to-paste STATUS.md entry.

```
Generate a STATUS.md entry for completion of Stage 1.
Include: date placeholder (YYYY-MM-DD), summary sentence, verification note.
Return a single fenced markdown block with a heading 'Stage 1 – Completed'.
```

**Success Criteria:** Entry is concise (<6 lines) and matches policies.

---

## Prompt 8 – Git Commit Message

**Goal:** Supply standardized commit message(s).

```
Return a single line conventional commit style message summarizing Stage 1 completion.
Format: stage1: fastapi skeleton with placeholder ask endpoint
Return plain text only.
```

**Success Criteria:** Message conforms to pattern `stage1: ...`.

---

## Prompt 9 – Idempotent Rerun Guard (Optional)

**Goal:** Ask AI to produce bash that safely re-applies Stage 1 without overwriting user changes.

```
Produce bash commands that:
- Create missing files only (do not overwrite existing ones)
- Warn (echo) if app/main.py already exists instead of replacing it
- Exit non-zero if Python version < 3.11
Return ONLY a fenced bash block.
```

**Success Criteria:** Running twice does not destroy existing content.

---

## Constraints Recap (Remind AI if Drift Occurs)

- No AI / OpenAI usage in Stage 1 code
- Keep dependencies minimal
- No Dockerfile yet (later stage if needed)
- No logging layer or thresholds implementation here
- Use consistent naming per `gpt.md`

---

## Exit Criteria

All deliverables checked; `/ask` stable; optional test passes; `STATUS.md` updated; commit applied.

---

## Next Stage Teaser (Do NOT Implement Now)

Stage 2 introduces: CSV/Sheet ingestion, embeddings, similarity scoring, escalation path logic.

---
