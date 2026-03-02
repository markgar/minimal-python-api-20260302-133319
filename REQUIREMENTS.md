# Project Requirements

> This document contains the project requirements as provided by the user.
> It may be updated with new requirements in later sessions.

# Minimal Python API

A Python FastAPI application with a single health endpoint.

## Tech Stack

- Python 3.12 with FastAPI and Uvicorn
- No database, no authentication

## Features

- `GET /health` returns `{ "status": "healthy" }` with a 200 status code
