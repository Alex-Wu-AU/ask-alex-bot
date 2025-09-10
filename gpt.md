# 📘 Ask Alex – Master Rulebook (`gpt.md`)

This document defines the **core principles, tech stack, and roadmap** for the Ask Alex chatbot.
It is the **master reference**: all development stages, design choices, and docs must align with this file.

---

## 🛠️ Tech Stack (Fixed)

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python 3.11)
- **AI Provider**: [OpenAI GPT API](https://platform.openai.com/docs/)
  - Default model: `gpt-3.5-turbo`
  - Embeddings: `text-embedding-3-small` for semantic matching
  - Purpose: semantic linking of questions and optional fallback
- **Data Storage**:
  1. Google Sheet / CSV: FAQ posts, categories, tutor info (sheet-driven, editable by unit chairs)
  2. Optional DB (Postgres/MongoDB) for logging & analytics
- **Containerization**: Docker
- **Integrations**: Microsoft Teams (Incoming Webhook → MVP, Azure Bot Framework → future)
- **Version Control & Open Source**: GitHub repository (`ask-alex-bot`)

---

## 🔑 Core Principles

1. **Sheet-first principle**
   - Bot uses **sheet-defined posts** as authoritative answers.
   - Unit chairs can edit **Category, Content/Link, Tutor info** only.
2. **Semantic Linking**
   - AI generates embeddings of questions and posts.
   - Finds **closest match** based on cosine similarity.
3. **Intent Classification**
   - Optional step to assign question category.
   - Helps narrow post search and route tutor escalation.
4. **Tutor Escalation**
   - If similarity < threshold, bot escalates question to **assigned tutor**.
5. **Minimal Setup**
   - Run locally: `uvicorn app.main:app --reload` with `.env` (`OPENAI_API_KEY`)
6. **Security**
   - No hardcoded secrets. Use `.env` or cloud secret manager.
7. **Extensibility**
   - Modular design: add new FAQ sources, integrations, categories.
8. **Open Source Quality**
   - Docs: `README.md`, `ARCHITECTURE.md`, `ROADMAP.md`, `CONTRIBUTING.md`
   - MIT License
   - Community-friendly: clear PRs, simple design

---

## 🚦 Development Stages

### Stage 1 – MVP

- FastAPI backend `/ask` endpoint
- OpenAI GPT integration (embedding-based semantic linking)
- Dockerfile + GitHub setup
- Test via Postman

### Stage 2 – Sheet Integration & Tutor Escalation

- Google Sheet / CSV for posts, categories, and tutor info
- Semantic search using embeddings
- Tutor escalation when no match

### Stage 3 – Logging & Analytics

- Optional DB logging of questions & responses
- Analytics: top questions, category stats

### Stage 4 – Full Teams Bot

- Azure Bot Framework deployment
- Optional role-based answers & dashboards

---

## 📌 Rules of Engagement

- **`gpt.md` is the master rulebook**; all other docs must align.
- Update `gpt.md` only for fundamental changes to rules or architecture.
- Before starting a stage, confirm alignment with this file.
