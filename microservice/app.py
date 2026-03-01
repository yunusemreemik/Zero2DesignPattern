"""Simple sample microservice that accepts POST requests.

Run:
    python microservice/app.py

Then send a request:
    curl -X POST http://127.0.0.1:8080/api/v1/messages \
      -H 'Content-Type: application/json' \
      -d '{"name":"Ada","message":"Hello"}'
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any


HOST = "127.0.0.1"
PORT = 8080


@dataclass
class Message:
    id: int
    name: str
    message: str
    created_at: str


class MessageStore:
    """In-memory store for demo purposes only."""

    def __init__(self) -> None:
        self._items: list[Message] = []

    def create(self, name: str, message: str) -> Message:
        created = Message(
            id=len(self._items) + 1,
            name=name,
            message=message,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
        self._items.append(created)
        return created

    def all(self) -> list[Message]:
        return self._items


store = MessageStore()


class RequestHandler(BaseHTTPRequestHandler):
    server_version = "PostSampleMicroservice/1.0"

    def _send_json(self, status_code: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/health":
            self._send_json(200, {"status": "ok"})
            return

        if self.path == "/api/v1/messages":
            self._send_json(200, {"items": [asdict(item) for item in store.all()]})
            return

        self._send_json(404, {"error": "Not Found"})

    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/api/v1/messages":
            self._send_json(404, {"error": "Not Found"})
            return

        length_header = self.headers.get("Content-Length")
        if not length_header:
            self._send_json(411, {"error": "Content-Length header is required"})
            return

        try:
            raw_body = self.rfile.read(int(length_header))
            payload = json.loads(raw_body.decode("utf-8"))
        except (ValueError, json.JSONDecodeError):
            self._send_json(400, {"error": "Body must be valid JSON"})
            return

        name = str(payload.get("name", "")).strip()
        message = str(payload.get("message", "")).strip()

        if not name or not message:
            self._send_json(400, {"error": "Fields 'name' and 'message' are required"})
            return

        created = store.create(name=name, message=message)
        self._send_json(201, {"item": asdict(created)})


def run() -> None:
    server = ThreadingHTTPServer((HOST, PORT), RequestHandler)
    print(f"Server running on http://{HOST}:{PORT}")
    print("POST sample endpoint: /api/v1/messages")
    server.serve_forever()


if __name__ == "__main__":
    run()
