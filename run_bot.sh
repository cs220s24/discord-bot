#!/bin/bash

# Check if the virtual environment directory exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate the virtual environment
source .venv/bin/activate

# Install Redis using Homebrew
brew install redis

# Start Redis server
brew services start redis

# Confirm Redis server is running
redis-cli ping

# Install Python dependencies
pip install -r requirements.txt

# Run the Python script
python app.py
