#!/bin/bash
set -euo pipefail
echo "Setting up Release Management Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
