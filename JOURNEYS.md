# User Journey Tests

## J-1: API startup and health smoke check
<!-- after: 1 -->
<!-- covers: api.startup, health -->
<!-- tags: smoke -->
Start the application with `uvicorn app.main:app` → wait for server to be ready → send `GET /health` → verify response status is 200 → verify response body is `{"status": "healthy"}`.

## J-2: Health endpoint response format validation
<!-- after: 1 -->
<!-- covers: health, api.response -->
Send `GET /health` → verify `Content-Type` header is `application/json` → parse response body as JSON → verify the JSON object contains exactly the key `status` with value `"healthy"` → verify no extra keys are present.

## J-3: Health endpoint repeated calls for stability
<!-- after: 1 -->
<!-- covers: health, api.stability -->
Send `GET /health` three times in sequence → verify each response returns status 200 → verify each response body is identical `{"status": "healthy"}` → confirm the server remains responsive across all calls.

## J-4: Unknown route returns structured JSON error
<!-- after: 1 -->
<!-- covers: api.errors, api.response -->
Send `GET /unknown-path` → verify response status is 404 → verify response body is JSON → verify JSON contains a `detail` field → confirm the server remains reachable after the error response.

## J-5: Unsupported HTTP method on health endpoint
<!-- after: 1 -->
<!-- covers: health, api.errors -->
Send `POST /health` with an empty body → verify response status is 405 (Method Not Allowed) → verify response body is JSON with a `detail` field → then send `GET /health` immediately after → verify it still returns 200 with `{"status": "healthy"}`.

## J-6: Health endpoint with query parameters ignored
<!-- after: 1 -->
<!-- covers: health, api.response -->
Send `GET /health?foo=bar` → verify response status is 200 → verify response body is `{"status": "healthy"}` → confirm unknown query parameters do not affect the response.

## J-7: Health endpoint with extra request headers
<!-- after: 1 -->
<!-- covers: health, api.response -->
Send `GET /health` with custom headers (`X-Custom-Header: test`, `Accept: application/json`) → verify response status is 200 → verify response body is `{"status": "healthy"}` → confirm extra request headers are tolerated.

## J-8: Root path returns JSON error, health path still works
<!-- after: 1 -->
<!-- covers: api.errors, health, api.startup -->
Send `GET /` → verify response status is 404 and body is JSON → then send `GET /health` → verify response status is 200 and body is `{"status": "healthy"}` → confirm the API routes requests correctly and the health endpoint is reachable even after navigating to an undefined root path.
