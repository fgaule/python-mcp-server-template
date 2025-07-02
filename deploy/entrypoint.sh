#!/bin/sh

echo ">> Running main:app"
exec python3 -m uvicorn main:app --port 8080 --host 0.0.0.0 --log-config /app/config/base_uvicorn_log_config.json
