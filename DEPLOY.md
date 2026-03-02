# Deploy Guide

## Overview

Minimal Python FastAPI application with a single health endpoint.

## Dockerfile

- Location: `./Dockerfile`
- Base image: `python:3.12-slim`
- Build: installs `requirements.txt`, copies source, exposes port 8000
- No build arguments or multi-stage setup needed

## Docker Compose

- File: `./docker-compose.yml`
- Single service: `app`
- Container port: `8000`
- Host port: `8724` (mapped as `8724:8000`)

## Environment Variables

None required. Application uses no configuration via environment variables.

## Startup Sequence

1. `export COMPOSE_PROJECT_NAME=minimal-python-api-20260302-133319`
2. `docker compose build`
3. `docker compose up -d`
4. App is healthy in ~3 seconds

## Health Check

- Endpoint: `GET /health`
- Expected response: HTTP 200, `{"status": "healthy"}`

## Running Tests

```
docker compose exec app pytest tests/ -v
```

Pytest runs successfully with 1 passing placeholder test.

## Known Gotchas

- No database or external services required — single container is sufficient.
- Remember to set `COMPOSE_PROJECT_NAME` before any `docker compose` command to avoid port conflicts with other projects.
