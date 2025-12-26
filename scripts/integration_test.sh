#!/usr/bin/env bash
set -euo pipefail
# For a library, integration test is often "install and import" in a clean env.
python -m pip install -e .
python -c "from mock_lib import greet; print(greet('integration'))"
echo "mock_lib integration OK"
