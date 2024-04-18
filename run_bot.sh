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

# Create .env file and add the bot token
echo "BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN" > .env

# Install Python dependencies
pip install -r requirements.txt

# Run the Python script
python app.py
