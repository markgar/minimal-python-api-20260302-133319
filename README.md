# Minimal Python API

A lightweight FastAPI application exposing a single health endpoint.

## Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) or pip

## Build & Run

```bash
pip install fastapi uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`. See `SPEC.md` for acceptance criteria and `REQUIREMENTS.md` for full feature details.

## Development

Install dependencies, make changes, and run the server with `--reload` for hot-reloading during development.
