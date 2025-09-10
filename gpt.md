# 📝 Ask Alex Master Rulebook (`gpt.md`)

This is the **core rulebook** for the `ask-alex-bot` project.  
All developers should refer to this document when stopping at a stage and returning later.

---

## 1. Purpose

Ask Alex is a **student Q&A chatbot** designed to:

- Provide answers to students’ questions based on official posts.
- Escalate questions to the corresponding tutor if no official answer exists.
- Allow unit chairs to customize categories and content.
- Integrate AI to assist with classification and semantic matching, not replace human oversight.

---

## 2. Tech Stack

- **Backend:** Python 3.11 + FastAPI
- **Frontend (optional):** React (Vite)
- **Database / Storage:** Google Sheet or CSV (initial), MongoDB/Postgres (future)
- **AI:** OpenAI GPT (`gpt-3.5-turbo`), text embeddings for semantic search
- **DevOps:** Docker, CI/CD pipelines
- **Integration:** Microsoft Teams bot or webhook

---

## 3. Core Principles

1. **Clean, maintainable code** – code should be readable and modular.
2. **Stage-by-stage development** – follow `plan.md` and complete tasks sequentially.
3. **Documentation updates** – after completing any step, update:
   - `STATUS.md` for task completion
   - `gpt.md` for any rule updates or clarifications
   - Optional stage prompt file for detailed instructions
4. **Testing at every stage** – each feature must include a simple verification test.
5. **Reproducibility** – steps in `plan.md` + stage prompt files should allow anyone to replicate the bot.

---

## 4. Project Structure

ask-alex-bot/
├── app/
│ ├── init.py
│ └── main.py
├── tests/
│ └── test_placeholder.py
├── docs/
│ ├── gpt.md
│ ├── STATUS.md
│ └── plan.md
├── stage_prompts/
│ ├── stage1_fastapi.md
│ ├── stage2_sheet_integration.md
│ ├── stage3_logging.md
│ ├── stage4_teams_integration.md
│ └── stage5_future_enhancements.md
├── requirements.txt
├── Dockerfile
└── README.md

---

## 5. Stage Prompt Files

- Detailed prompts for AI-assisted code generation are stored in `stage_prompts/`.
- Each file corresponds to a development stage:

  - `stage1_fastapi.md` – FastAPI skeleton
  - `stage2_sheet_integration.md` – Sheet / semantic matching
  - `stage3_logging.md` – Logging & analytics
  - `stage4_teams_integration.md` – Teams integration
  - `stage5_future_enhancements.md` – Optional AI fallback, frontend dashboard, parameters

- **Purpose:** keep `plan.md` clean while allowing reproducible, detailed AI instructions.

---

## 6. Rules for Contributors

1. Always **update documentation** after completing any task.
2. Follow the **plan in `plan.md`** sequentially.
3. Use **stage prompts** when generating code or instructions.
4. Ensure **test verification** is performed for each step.
5. For any modifications or additions, update `gpt.md` with clear notes.
