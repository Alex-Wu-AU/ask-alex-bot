# Stage 1 – FastAPI Skeleton (Granular Prompts)

Each step below is a **small prompt**. Run them sequentially, test the output, and update documentation after each step.

---

## Step 1 – Create Project Folder

**Prompt:**  
"Provide detailed instructions to create a new Python 3.11 project folder named `ask-alex-bot` and explain why this folder is needed. Include notes on versioning and virtual environment setup, but do not provide terminal commands yet."

**Test:** Confirm developer understands the folder purpose and setup.

**Documentation Reminder:** Update `STATUS.md` and `gpt.md` after completion.

---

## Step 2 – Create App Folder and Files

**Prompt:**  
"Provide instructions to create an `app/` folder with `__init__.py` and `main.py`. Explain the role of each file and why `__init__.py` is needed. Include advice on organizing backend code for FastAPI projects."

**Test:** Ensure developer understands file roles.

**Documentation Reminder:** Update `STATUS.md` and `gpt.md`.

---

## Step 3 – Create Tests Folder

**Prompt:**  
"Provide instructions to create a `tests/` folder with `test_placeholder.py`. Explain why we include tests from the start and suggest what the first placeholder test could do."

**Test:** Developer can write a simple placeholder test.

**Documentation Reminder:** Update `STATUS.md` and `gpt.md`.

---

## Step 4 – Create Docs Folder

**Prompt:**  
"Provide instructions to create a `docs/` folder with `gpt.md`, `STATUS.md`, and `plan.md`. Explain the purpose of each documentation file in the project workflow."

**Test:** Confirm understanding of documentation workflow.

**Documentation Reminder:** Update `STATUS.md` and `gpt.md`.

---

## Step 5 – Create Placeholder Files

**Prompt:**  
"Provide instructions to create `requirements.txt`, `Dockerfile`, and `README.md` as placeholders. Explain what content will eventually go in each file and why they are needed."

**Test:** Developer understands purpose of placeholder files.

**Documentation Reminder:** Update `STATUS.md` and `gpt.md`.

---

## Step 6 – Add Minimal FastAPI App

**Prompt:**  
"Provide instructions to write a minimal FastAPI app in `main.py` with a `/ask` POST endpoint. Include example JSON payload and a placeholder response: 'Hello, Ask Alex is working'. Explain uvicorn entry point and why it is needed."

**Test:** Start the server with uvicorn and POST a sample request to `/ask`.

**Documentation Reminder:** Update `STATUS.md` and `gpt.md`.

---

## Step 7 – Verify Skeleton

**Prompt:**  
"Provide instructions to verify that the FastAPI skeleton works. Include starting the server, sending a test POST request, and checking the response."

**Test:** Confirm server runs and `/ask` returns the placeholder response.

**Documentation Reminder:** Update `STATUS.md` and `gpt.md`.
