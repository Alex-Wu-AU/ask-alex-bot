"""Stage 1 FastAPI placeholder app.

Provides a single POST /ask endpoint that returns a deterministic
placeholder response. No external integrations or business logic.
"""

from fastapi import FastAPI
from pydantic import BaseModel


class QuestionRequest(BaseModel):
	question: str


app = FastAPI(title="Ask Alex", version="0.1.0")


@app.post("/ask")
def ask(request: QuestionRequest):  # type: ignore[valid-type]
	"""Placeholder endpoint returning a static response.

	Args:
		request: Incoming question payload.

	Returns:
		Dict with static message and source_type placeholder marker.
	"""
	return {
		"message": "Hello, Ask Alex is working",
		"source_type": "placeholder",
	}

