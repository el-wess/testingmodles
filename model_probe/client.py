"""Thin OpenAI-compatible client with retry/backoff and raw logging."""
from __future__ import annotations

import json
import os
import random
import threading
import time
from pathlib import Path

import requests

BASE_URL = os.environ.get("RADOX_BASE_URL", "https://radoxai.com/v1")
RETRYABLE = ("overloaded", "rate", "timeout", "temporarily", "unavailable")


def api_key() -> str:
    key = os.environ.get("RADOX_API_KEY")
    if not key:
        raise SystemExit("Set RADOX_API_KEY (see .env.example)")
    return key


class Client:
    def __init__(self, log_path: Path, max_retries: int = 10):
        self.session = requests.Session()
        self.session.headers.update(
            {"Authorization": f"Bearer {api_key()}", "Content-Type": "application/json"}
        )
        self.log_path = log_path
        self.max_retries = max_retries
        self._lock = threading.Lock()
        log_path.parent.mkdir(parents=True, exist_ok=True)

    def list_models(self) -> list[str]:
        r = self.session.get(f"{BASE_URL}/models", timeout=30)
        r.raise_for_status()
        return [m["id"] for m in r.json().get("data", [])]

    def chat(self, model: str, messages: list[dict], probe: str, **params) -> dict:
        """Returns a record dict; never raises for API errors."""
        payload = {"model": model, "messages": messages, **params}
        attempts = 0
        while True:
            attempts += 1
            start = time.perf_counter()
            status, body, err = None, None, None
            try:
                r = self.session.post(f"{BASE_URL}/chat/completions", json=payload, timeout=600)
                status = r.status_code
                try:
                    body = r.json()
                except ValueError:
                    err = r.text[:2000]
            except requests.RequestException as e:
                err = f"{type(e).__name__}: {e}"
            latency = time.perf_counter() - start

            if body and "error" in body:
                err = json.dumps(body["error"])
            retryable = err is not None and (
                status in (None, 429, 500, 502, 503, 504, 529)
                or any(s in err.lower() for s in RETRYABLE)
            )
            if retryable and attempts < self.max_retries:
                time.sleep(min(60, 2 ** attempts) * (0.5 + random.random()))
                continue
            break

        rec = {
            "ts": time.time(),
            "probe": probe,
            "model": model,
            "params": params,
            "messages": messages,
            "status": status,
            "attempts": attempts,
            "latency": round(latency, 3),
            "error": err,
            "response": body if not err else None,
        }
        with self._lock, self.log_path.open("a") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        return rec


def content(rec: dict) -> str | None:
    try:
        return rec["response"]["choices"][0]["message"].get("content")
    except (TypeError, KeyError, IndexError):
        return None


def usage(rec: dict) -> dict:
    try:
        return rec["response"].get("usage") or {}
    except (TypeError, AttributeError):
        return {}
