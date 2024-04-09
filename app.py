# This example requires the 'message_content' intent.
import discord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('BOT_TOKEN')

# Define a custom Discord client class
class MyClient(discord.Client):
    # Event handler for when the bot is ready
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    # Event handler for incoming messages
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

# Set up intents to listen for specific events
intents = discord.Intents.default()
intents.message_content = True

# Create an instance of the custom client class with specified intents
client = MyClient(intents=intents)

client.run(token)
