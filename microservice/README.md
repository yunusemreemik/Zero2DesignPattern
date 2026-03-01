# POST Sample Microservice

This microservice is a simple Python HTTP server that demonstrates how to handle `POST` requests with JSON payloads.

## Endpoints

- `GET /health` -> basic health check.
- `POST /api/v1/messages` -> creates a message.
- `GET /api/v1/messages` -> lists stored messages.

## Request body sample

```json
{
  "name": "Ada",
  "message": "Hello from POST sample"
}
```

## Run

```bash
python microservice/app.py
```

## Try with curl

```bash
curl -X POST http://127.0.0.1:8080/api/v1/messages \
  -H 'Content-Type: application/json' \
  -d '{"name":"Ada","message":"Hello from curl"}'
```

Or open `microservice/samples.http` with an HTTP client that supports `.http` files.
