#!/bin/bash
echo "====================================================================="
echo " SmartCity Traffic Simulator — Grand Tunis (FastAPI Port 8001)"
echo "====================================================================="
cd "$(dirname "$0")"

if [ -d "venv" ]; then
    source venv/bin/activate
fi

python3 -m uvicorn main:app --host 127.0.0.1 --port 8001 --reload
