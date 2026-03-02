# Milestone 1: Scaffolding — project structure, FastAPI app, health endpoint, pytest setup with placeholder test

> **Validates:**
> - `GET /health` returns HTTP 200 with JSON body `{"status": "healthy"}`
> - Application starts without errors via `uvicorn app.main:app`
> - `pytest` exits 0 with at least one passing test

> **Reference files:**
> - `app/main.py` — FastAPI app entry point (to be created in this milestone)

- [ ] Create `requirements.txt` declaring `fastapi`, `uvicorn[standard]`, and `pytest` as dependencies
- [ ] Create `app/__init__.py` to make `app` a Python package
- [ ] Create `app/routers/__init__.py` to make `app/routers` a Python package
- [ ] Create `app/routers/health.py` with an `APIRouter` and a `GET /health` handler returning `{"status": "healthy"}`
- [ ] Create `app/main.py` that instantiates `FastAPI`, imports and registers the health router with `app.include_router(...)`
- [ ] Install dependencies with `pip install -r requirements.txt`
- [ ] Create `tests/__init__.py` to make `tests` a Python package
- [ ] Create `tests/test_placeholder.py` with one trivial passing test (`assert True`) to verify pytest is functional
