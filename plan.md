# 📝 Ask Alex Bot Development Plan (`plan.md`)

Step-by-step TODO list to build `ask-alex-bot`. Keep this concise; core policies live in `gpt.md`.

Each step lists:

- Task
- Operable AI prompt
- Test instructions
- Documentation reminder

Update `STATUS.md` after each completed item.

---

## Conventions Quick Reference

- File / function names: snake_case
- Models (Pydantic / classes): PascalCase
- Constants / env vars: UPPER_SNAKE (e.g. ANSWER_THRESHOLD, CATEGORY_THRESHOLD)
- Branch naming: stageN-short-desc (e.g. stage2-embeddings)
- Default thresholds: ANSWER_THRESHOLD=0.80, CATEGORY_THRESHOLD=0.60

---

## Stage 1 – FastAPI Skeleton (Complete)

- [x] **Create FastAPI skeleton**  
       **Prompt:** Generate minimal FastAPI project with `/ask` POST endpoint returning placeholder JSON `{"message":"Hello, Ask Alex is working", "source_type":"placeholder"}`.  
       **Test:** POST `{ "question":"test" }` → verify placeholder response.  
       **Docs:** Update `STATUS.md` (mark Stage 1 complete).

- [x] **Basic README & requirements**  
       **Prompt:** Provide README summary (purpose, run instructions) + minimal requirements (fastapi, uvicorn, pydantic).  
       **Test:** Fresh clone + install + run works.  
       **Docs:** `STATUS.md` updated.

(Any OpenAI logic deferred to Stage 2.)

---

## Stage 2 – Data & Semantic Matching

- [ ] **Add CSV / Sheet ingestion**  
       **Prompt:** Load CSV with columns: Category, ContentOrLink, Marking Tutor Name, Marking Tutor Email, Seminar Tutor Name, Seminar Tutor Email, Unit Chair Name, Unit Chair Email. Provide in-memory list of dicts + reload function.  
       **Test:** Sample 3-row file loads; missing optional fields handled.  
       **Docs:** Update `STATUS.md`.

- [ ] **Integrate OpenAI embeddings (abstraction)**  
       **Prompt:** Add embedding service with function `embed_texts(list[str]) -> list[list[float]]` using `text-embedding-3-small`; store vectors on records. Mock-friendly design.  
       **Test:** All records receive non-empty embedding vectors.  
       **Docs:** Update `STATUS.md`.

- [ ] **Semantic search in /ask**  
       **Prompt:** Update `/ask` to embed question, compute cosine similarity, return best match if ≥ ANSWER_THRESHOLD.  
       **Test:** Query similar to known post returns that post + similarity.  
       **Docs:** Update `STATUS.md`.

- [ ] **Category inference & escalation**  
       **Prompt:** If top similarity < ANSWER_THRESHOLD, aggregate by category; if best < CATEGORY_THRESHOLD → category `unknown`. Return escalation payload with available roles; avoid fabrication.  
       **Test:** Unrelated question triggers escalation; weak signal yields `unknown`.  
       **Docs:** Update `STATUS.md`.

- [ ] **Minimal request logging**  
       **Prompt:** Append JSONL entries: timestamp, question, outcome (`match|escalation`), top_similarity, category_guess.  
       **Test:** Two queries → two well-formed lines.  
       **Docs:** Update `STATUS.md`.

---

## Stage 3 – Logging & Analytics Expansion

- [ ] **Structured logging upgrade**  
       **Prompt:** Extract logging into module; add answer_type, roles_offered count. Optional persistence (SQLite/CSV rotation).  
       **Test:** 3 queries logged with new fields.  
       **Docs:** Update `STATUS.md`.

- [ ] **/stats endpoint**  
       **Prompt:** Return total_questions, by_outcome, by_category (top 5), unresolved_escalations (placeholder).  
       **Test:** Simulated queries → correct aggregates.  
       **Docs:** Update `STATUS.md`.

---

## Stage 4 – Microsoft Teams Integration

- [ ] **Teams adapter**  
       **Prompt:** Simple handler translating Teams message payload to internal `/ask` call & formatting response.  
       **Test:** Simulated Teams POST → formatted reply.  
       **Docs:** Update `STATUS.md`.

- [ ] **End-to-end scripted test**  
       **Prompt:** Script sends: (match, category escalation, unknown) scenarios.  
       **Test:** Output matches expected outcomes.  
       **Docs:** Update `STATUS.md`.

---

## Stage 5 – Enhancements & Fallbacks

- [ ] **Optional AI fallback generation**  
       **Prompt:** If enabled via `ENABLE_FALLBACK`, generate GPT answer with safety preamble; set `source_type: fallback`.  
       **Test:** Flag on + unmatched question returns fallback answer.  
       **Docs:** Update `STATUS.md`.

- [ ] **Per-post parameters**  
       **Prompt:** Support Parameters JSON column merged into match responses.  
       **Test:** Row with `{ "deadline":"2025-10-15" }` returns deadline.  
       **Docs:** Update `STATUS.md`.

- [ ] **Frontend dashboard (optional)**  
       **Prompt:** React page listing posts, logs summary, reload button.  
       **Test:** Page loads data & triggers reload successfully.  
       **Docs:** Update `STATUS.md`.

---

## General Testing Notes

- Keep prior stage tests green
- Prefer pytest + mocks (no live API in unit tests)
- Embed services & OpenAI client must be mockable

---

## Documentation Reminders

After each completed checklist item:

1. Update `STATUS.md` with date + short note
2. Update `gpt.md` ONLY if a core policy changes
3. Commit with message: `stageX: <short-desc>`
