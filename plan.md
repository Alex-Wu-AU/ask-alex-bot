# 📝 Ask Alex Bot Development Plan (`plan.md`)

This is a **step-by-step TODO list** for building `ask-alex-bot`.  
Each step includes:

- **Task**
- **Operable AI prompt**
- **Test instructions**
- **Documentation update reminder**

Follow each step to reproduce the chatbot workflow.

---

## Stage 1 – MVP (FastAPI + OpenAI)

- [ ] **Create FastAPI skeleton**  
      **Prompt:** Generate a FastAPI project skeleton for a chatbot named "Ask Alex" with Python 3.11, uvicorn entry point, a `/ask` POST endpoint that receives a question, placeholder response "Hello, Ask Alex is working", and folder structure ready for future AI integration.  
      **Test:** POST `{"question":"test"}` to `/ask` → expect `"Hello, Ask Alex is working"`.  
      **Documentation Reminder:** After completing this step, update `STATUS.md` and `gpt.md` with today’s date.

- [ ] **Integrate OpenAI GPT API**  
      **Prompt:** Add OpenAI GPT integration to `/ask` endpoint using `gpt-3.5-turbo`. Return a fixed placeholder answer for now. Use environment variable `OPENAI_API_KEY`.  
      **Test:** Send POST request with sample question → confirm API call is made and a response is returned.  
      **Documentation Reminder:** Update `STATUS.md` and `gpt.md` with today’s date and note API integration.

- [ ] **Add Dockerfile**  
      **Prompt:** Generate a Dockerfile for the FastAPI project with Python 3.11, installing dependencies, setting working directory, and running uvicorn on container start.  
      **Test:** Build and run Docker container → POST to `/ask` → verify response.  
      **Documentation Reminder:** Update `STATUS.md` and `gpt.md` with today’s date.

- [ ] **Add basic README.md**  
      **Prompt:** Create README.md with project description, installation instructions, running instructions, and placeholder for future stages.  
      **Test:** Run `uvicorn app.main:app --reload` → verify server starts correctly.  
      **Documentation Reminder:** Update `STATUS.md` and `gpt.md` with today’s date.

---

## Stage 2 – Sheet Integration + Semantic Matching

- [ ] **Add Google Sheet / CSV integration**  
      **Prompt:** Generate Python code to read a Google Sheet or CSV containing columns: Category, Content/Link, Tutor Name, Tutor Email. Store data in memory as a list of dictionaries.  
      **Test:** Add 2-3 sample rows → fetch data → confirm correct rows and fields loaded.  
      **Documentation Reminder:** Update `STATUS.md` and `gpt.md`.

- [ ] **Compute embeddings for posts**  
      **Prompt:** Generate embeddings for each post’s Content/Link using OpenAI `text-embedding-3-small` and store embeddings alongside original rows.  
      **Test:** Verify each post has a non-empty embedding vector → print shape and length.  
      **Documentation Reminder:** Update `STATUS.md` and `gpt.md`.

- [ ] **Semantic search endpoint**  
      **Prompt:** Update `/ask` endpoint to receive a student question, generate its embedding, compute cosine similarity with all post embeddings, and return the Content/Link of the post with highest similarity.  
      **Test:** Send a test question → verify returned post matches expected closest post.  
      **Documentation Reminder:** Update `STATUS.md` and `gpt.md`.

- [ ] **Similarity threshold and fallback**  
      **Prompt:** If highest similarity < 0.8, retrieve the corresponding tutor for the question category and return message: "No official post found. Please contact {Tutor Name} ({Tutor Email})".  
      **Test:** Send unrelated question → verify bot returns correct tutor info.  
      **Documentation Reminder:** Update `STATUS.md` and `gpt.md`.

---

## Stage 3 – Logging & Analytics

- [ ] **Log questions and responses**  
      **Prompt:** Save each question, returned post, similarity score, and timestamp to JSON/CSV or optional MongoDB/Postgres.  
      **Test:** Ask 2-3 questions → check log file or DB contains correct question, answer, score, and timestamp.  
      **Documentation Reminder:** Update `STATUS.md` and `gpt.md`.

- [ ] **Analytics endpoint**  
      **Prompt:** Generate `/stats` endpoint summarizing number of questions by category and top 5 most asked questions.  
      **Test:** Send multiple questions across categories → GET `/stats` → verify counts and top questions.  
      **Documentation Reminder:** Update `STATUS.md` and `gpt.md`.

---

## Stage 4 – Microsoft Teams Integration

- [ ] **Deploy bot to Teams**  
      **Prompt:** Create a Microsoft Teams bot or incoming webhook integration. Connect `/ask` endpoint, receive messages from Teams, and return responses to chat.  
      **Test:** Send a question from Teams → verify bot responds and logs updated.  
      **Documentation Reminder:** Update `STATUS.md` and `gpt.md`.

- [ ] **Test end-to-end**  
      **Prompt:** Test full flow: student asks question in Teams → bot classifies, matches post, or escalates to tutor → response appears in Teams → logs updated.  
      **Test:** Simulate 3 different questions → confirm correct matching/escalation.  
      **Documentation Reminder:** Update `STATUS.md` and `gpt.md`.

---

## Stage 5 – Future Enhancements

- [ ] **Add optional AI fallback generation**  
      **Prompt:** If no matching post exists, generate answer using GPT API with prompt: "Provide a helpful and safe answer to the following student question: {question}".  
      **Test:** Ask a completely new question → verify AI generates plausible fallback answer.  
      **Documentation Reminder:** Update `STATUS.md` and `gpt.md`.

- [ ] **Allow unit chairs to add parameters**  
      **Prompt:** Update sheet to include optional JSON parameters per post. Bot reads parameters and can use them in responses.  
      **Test:** Add parameter like {"deadline": "2025-10-15"} → verify bot returns parameter when asked.  
      **Documentation Reminder:** Update `STATUS.md` and `gpt.md`.

- [ ] **Add frontend dashboard (optional)**  
      **Prompt:** Generate a simple React frontend to display sheet content, show logs, and allow unit chairs to edit categories and posts.  
      **Test:** Load frontend → verify sheet data renders → edit row → verify backend updates.  
      **Documentation Reminder:** Update `STATUS.md` and `gpt.md`.
