# Stage 1 – FastAPI Skeleton Tracker

This file tracks detailed progress for Stage 1.  
Record for each step: date, status, notes, issues. Use statuses: ✅ done / ⏳ in progress / ❌ blocked.

---

## Step 1 – Project Scaffold

- **Date:** 2025-09-11
- **Status:** ✅
- **Notes:** Created base files + folders (`app/`, `tests/`, README, .gitignore, venv)
- **Issues:**

---

## Step 2 – Placeholder Endpoint

- **Date:** 2025-09-11
- **Status:** ✅
- **Notes:** Implemented `app/main.py` with `/ask` returning placeholder JSON
- **Issues:** Initial Python 3.12 + pydantic-core wheel friction resolved by using proper CPython env

---

## Step 3 – Minimal Requirements

- **Date:** 2025-09-11
- **Status:** ✅
- **Notes:** Added fastapi, uvicorn (pydantic transitively). Later expanded for tests.
- **Issues:** N/A

---

## Step 4 – Basic Test (Optional)

- **Date:** 2025-09-11
- **Status:** ✅
- **Notes:** Added `tests/test_ask_placeholder.py` verifying placeholder response
- **Issues:** Missing httpx dependency initially

---

## Step 5 – Test Dependencies (If Added)

- **Date:** 2025-09-11
- **Status:** ✅
- **Notes:** Added pytest + httpx (for TestClient)
- **Issues:** Path import issue fixed via `tests/conftest.py`

---

## Step 6 – Run & Verify

- **Date:** 2025-09-11
- **Status:** ✅
- **Notes:** Manual POST (Invoke-RestMethod + curl) returns expected JSON; pytest 1 passed
- **Issues:** Initial 422 due to PowerShell quoting fixed

---

## Step 7 – Documentation Update

- **Date:** 2025-09-11
- **Status:** ✅
- **Notes:** STATUS.md updated; stage1 prompt pack stable; Python version references aligned to 3.12
- **Issues:** N/A

---

## Step 8 – Commit & Tag

- **Date:** 2025-09-11
- **Status:** ✅
- **Notes:** Commit `stage1: fastapi skeleton with placeholder /ask endpoint and basic test` pushed
- **Issues:** N/A

---

## Exit Criteria Review

- Placeholder endpoint stable ✅
- Dependencies install cleanly ✅
- Optional test passes ✅
- Docs updated ✅
- Commit applied ✅

---

## Retro Notes (Optional)

- What went well: Clear staged prompts reduced ambiguity; fast resolution of env issues
- What to improve next stage: Start directly with official CPython to avoid wheel build friction
- Tooling debt (if any): None critical; consider adding a Makefile / task runner in Stage 2

---

## Next Session Pickup Notes

Focus: Begin Stage 2.
First Actions (planned):

1. Define ingestion format (CSV schema) and add sample data file.
2. Add embedding dependency (openai or alternative) but keep calls stubbed initially.
3. Create service module for semantic match (placeholder logic until embeddings wired).
   Open Questions: Decide on local vs remote embedding call strategy; file naming for data source.
   Reminder: Update `plan.md` and add Stage 2 status tracker file before coding.
