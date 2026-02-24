import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, field_validator
from groq import Groq, APIConnectionError, APIStatusError
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="LLM Query API",
    description="A minimal FastAPI app to query an LLM via Groq.",
    version="1.0.0",
)

MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
# --------------------------------------------------------------------------- #
# Pydantic models
# --------------------------------------------------------------------------- #

class QueryRequest(BaseModel):
    query: str

    @field_validator("query")
    @classmethod
    def query_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("query must not be empty or whitespace.")
        return v.strip()


class QueryResponse(BaseModel):
    answer: str


# --------------------------------------------------------------------------- #
# LLM logic
# --------------------------------------------------------------------------- #

def get_groq_client() -> Groq:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY is not set. Configure it as an environment variable.",
        )
    return Groq(api_key=api_key)


def query_llm(user_query: str) -> str:
    """Send a query to Groq and return the assistant's reply."""
    client = get_groq_client()

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Answer clearly and concisely.",
                },
                {
                    "role": "user",
                    "content": user_query,
                },
            ],
            model=MODEL,
        )
        return chat_completion.choices[0].message.content

    except APIConnectionError as e:
        raise HTTPException(
            status_code=503,
            detail=f"Could not connect to Groq API: {str(e)}",
        )
    except APIStatusError as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=f"Groq API error: {e.message}",
        )


# --------------------------------------------------------------------------- #
# Endpoints
# --------------------------------------------------------------------------- #

@app.get("/", include_in_schema=False)
def root():
    return {"status": "ok", "message": "LLM Query API is running. POST to /query."}


@app.post("/query", response_model=QueryResponse)
def query_endpoint(request: QueryRequest):
    """
    Accepts a natural-language query and returns the LLM's answer.
    """
    answer = query_llm(request.query)
    return QueryResponse(answer=answer)


# --------------------------------------------------------------------------- #
# Error handlers
# --------------------------------------------------------------------------- #

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": f"Unexpected server error: {str(exc)}"},
    )
