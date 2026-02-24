# Groq LLM Query API

A minimal, production-ready FastAPI application that exposes a single `POST /query` endpoint powered by the [Groq](https://groq.com) API.

---

## Project Structure

```
.
├── main.py           # FastAPI application
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variable template
├── render.yaml       # Render deployment config
└── README.md
```

---

## Local Setup

### 1. Clone / download the project

```bash
cd groq-fastapi
```

### 2. Create and activate a virtual environment

```bash
python3.11 -m venv venv
source venv/bin/activate      # macOS / Linux
# venv\Scripts\activate       # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
# Open .env and set your GROQ_API_KEY
```

Get your free API key at https://console.groq.com.

### 5. Run the server

```bash
uvicorn main:app --reload
```

The API is now live at `http://127.0.0.1:8000`.  
Interactive docs: `http://127.0.0.1:8000/docs`

---

## API Reference

### `POST /query`

**Request body**
```json
{
  "query": "What is the capital of France?"
}
```

**Success response** `200 OK`
```json
{
  "answer": "Paris is the capital of France."
}
```

**Error responses**

| Status | Reason |
|--------|--------|
| `422`  | Validation error (empty query) |
| `500`  | `GROQ_API_KEY` not set |
| `503`  | Cannot reach Groq API |
| `4xx`  | Groq returned an API error |

---

## Postman Example

| Field   | Value |
|---------|-------|
| Method  | `POST` |
| URL     | `http://127.0.0.1:8000/query` |
| Headers | `Content-Type: application/json` |
| Body (raw JSON) | `{ "query": "What is the capital of France?" }` |

---

## Deploy on Render

1. Push this project to a GitHub repository.
2. Go to [render.com](https://render.com) → **New Web Service** → connect your repo.
3. Render auto-detects `render.yaml`. Confirm the settings.
4. In **Environment Variables**, add:
   - `GROQ_API_KEY` → your actual key
5. Click **Deploy**. Your public URL will appear in the dashboard.

> **Note:** Render's free tier spins down after inactivity. Upgrade to a paid plan for always-on availability.

---

## Model

The app uses `llama3-8b-8192` by default. To change it, update the `MODEL` constant in `main.py`.

Other Groq-supported models: `llama3-70b-8192`, `mixtral-8x7b-32768`, `gemma2-9b-it`.

---

## License

MIT