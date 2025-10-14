#!/bin/bash
set -e

if [ -z "$1" ]; then
  echo "Usage: $0 <service_name>"
  exit 1
fi

SERVICE_NAME="$1"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_DIR="$SCRIPT_DIR/../$SERVICE_NAME"

# Copy everything except create-service.sh
mkdir -p "$TARGET_DIR"
rsync -a --exclude 'create-service.sh' "$SCRIPT_DIR/" "$TARGET_DIR/"

# Copy env.example to .env if not exists
if [ -f "$TARGET_DIR/env.example" ] && [ ! -f "$TARGET_DIR/env" ]; then
  cp "$TARGET_DIR/env.example" "$TARGET_DIR/env"
fi

echo "✅ Service '$SERVICE_NAME' created at $TARGET_DIR"
