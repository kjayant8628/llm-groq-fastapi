LLM Query API
Productionized FastAPI Microservice (Groq LLM)

A minimal, production-ready REST API that exposes a POST endpoint to query a Groq-hosted Large Language Model.

This project demonstrates the ability to:

Productionize an AI-backed service

Securely manage environment variables

Deploy to cloud infrastructure (Render)

Pin runtime and dependency versions

Expose a publicly accessible HTTPS endpoint

Maintain clean, minimal backend architecture

🌍 Live Deployment

Base URL

https://llm-groq-fastapi.onrender.com

Endpoint

POST /query
## 🧠 Architecture Overview

```text
        ┌───────────────┐
        │    Client     │
        │ (Postman /    │
        │  External App)│
        └───────┬───────┘
                │ HTTPS
                ▼
        ┌─────────────────┐
        │   Render Cloud  │
        │  (FastAPI App)  │
        └───────┬─────────┘
                │
                │ Groq SDK
                ▼
        ┌─────────────────┐
        │  Groq LLM API   │
        │ (Llama 3.1)     │
        └─────────────────┘

Client sends POST request to /query

FastAPI validates input using Pydantic

Server calls Groq LLM API

LLM response is returned as structured JSON

Client receives AI-generated answer

The application is stateless and does not store any data.

📌 Example Request
POST https://llm-groq-fastapi.onrender.com/query
Content-Type: application/json
{
  "query": "What is the capital of France?"
}
📌 Example Response
{
  "answer": "The capital of France is Paris."
}
🛠 Tech Stack

Python 3.11

FastAPI

Uvicorn

Groq API (Llama 3.1 model)

Render (Cloud deployment)

Pydantic (Validation)

🔐 Environment Configuration

Environment variables (managed securely in Render):

GROQ_API_KEY=your_api_key
GROQ_MODEL=llama-3.1-8b-instant

Secrets are not committed to version control.

🧪 Local Development
Clone
git clone https://github.com/kjayant8628/llm-groq-fastapi.git
cd llm-groq-fastapi
Create Virtual Environment
python -m venv venv
venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Run Locally
uvicorn main:app --reload

Server runs at:

http://127.0.0.1:8000
☁ Deployment Notes

Runtime pinned using .python-version (Python 3.11)

Dependencies version-locked for stability

Secure environment variable management

Public HTTPS endpoint

Stateless architecture

No database

No embeddings

No vector search

No local model hosting

🎯 Project Goal

To demonstrate the ability to productionize an AI-powered backend service using clean architecture, secure deployment practices, and industry-standard tools.