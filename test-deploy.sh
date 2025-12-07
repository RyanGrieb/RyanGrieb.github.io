#!/bin/bash

# Ensure act is in PATH
export PATH=$PATH:~/.local/bin

# Check if act is installed
if ! command -v act &> /dev/null; then
    echo "❌ 'act' is not installed or not in PATH."
    echo "   Please install it first."
    exit 1
fi

echo "🚀 Starting local GitHub Action run..."
echo "reusing 'ubuntu-latest=catthehacker/ubuntu:act-latest' image"

# Run act
# -P: Platform mapping
# -W: Workflow file (optional, defaults to .github/workflows)
# --secret: Mock secrets
act push \
    -P ubuntu-latest=catthehacker/ubuntu:act-latest

