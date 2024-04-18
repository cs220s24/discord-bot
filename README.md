# Discord Bot

### Members
* Brian Demyan
* Deni Velasquez
* Kaleb Missmer

## Description
This Discord bot is a simple example bot that can be used to interact with users in a Discord server. It can respond to various commands and events, such as greeting users when they send a specific message.

## Tutorial Used for Project
[Discord Bot Youtube Tutorial](https://www.youtube.com/watch?v=lLvCfSETihk&list=PLESMQx4LeD3N0-KKPPDaToZhBsom2E_Ju&index=2)

## Features
- Greeting users with a response when they send `!hello` in a text channel.
- Providing inspiring quotes to users who send `!motivate` command.

## Getting Started
### Prerequisites
- Python 3.6 or higher
- Discord.py library
- Redis database

### Installation
1. Clone or download this repository to your local machine.
2. Install dependencies by running:
   ```
   pip install -r requirements.txt
   ```
3. Create a Discord bot and obtain its token. You can follow the official Discord documentation on how to create a bot and obtain its token.
4. Create a `.env` file in the project directory and add the following line to it:
   ```
   BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN
   ```
### Redis Database Setup (MacOS)
1. Install Redis using Homebrew:
   ```
   brew install redis
   ```
2. Start the Redis server:
   ```
   brew services start redis
   ```
3. Confirm the server is running:
   ```
   redis-cli ping
   ```
   If it responds with PONG, then the server is running successfully.

### Usage
1. Make the run_bot.sh script executable by running:
   ```
   chmod +x run_bot.sh
   ```   
2. Run the bot by executing the `run_bot.sh` script:
   ```
   ./run_bot.sh
   ```

3. Run the bot by executing the `app.py` file:
   ```
   python app.py
   ```
4. The bot will log in and be ready to respond to commands and events in the Discord server.

### Commands
- `!hello`: Greet the user who sends the command with a response.
- `!motivate`: Gives the user who sends the command an inspiring quote.

### SSL Verification Error MacOS Solution 
1. Install Certifi
   ```
   pip install certifi
   ```
2. Run the script
   ```
   /Applications/Python\ 3.12/Install\ Certificates.command 
   ```