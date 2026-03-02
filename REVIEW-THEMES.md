# Review Themes

Last updated: Scaffolding — project structure, FastAPI app, health endpoint, pytest setup with placeholder test

1. **Dead code added speculatively** — Do not add logger variables, imports, or dependencies until the code that uses them is present; unused declarations signal incomplete work and add noise.
2. **No version pinning** — Always pin dependency versions in `requirements.txt`; unpinned deps produce non-reproducible builds that silently break across environments and over time.
3. **Overly broad type hints** — Use specific type annotations (`dict[str, str]`, `list[int]`, etc.) rather than bare `dict` or `list`; bare container types are no better than `Any` for tooling and readability.
4. **Module-level side effects at import time** — Never call `logging.basicConfig`, open files, or perform other side effects at module scope; these execute on every import including tests, causing interference with pytest log capture and library logging config.
