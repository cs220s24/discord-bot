import discord
import os
from dotenv import load_dotenv
from db import RedisHandler  
from quotes import MOTIVATIONAL_QUOTES

load_dotenv()

token = os.getenv('BOT_TOKEN')

# Initialize the RedisHandler with default parameters
redis_handler = RedisHandler()

# Set motivational quotes in the Redis database
redis_handler.set_motivational_quotes(MOTIVATIONAL_QUOTES)

# Define a custom Discord client class
class MyClient(discord.Client):
    # Event handler for when the bot is ready
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    # Event handler for incoming messages
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

    # Greeting ability
        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')

    # Command to get a motivational quote
        if message.content.startswith('!motivate'):
            quote = redis_handler.get_random_quote()
            await message.channel.send(quote)

intents = discord.Intents.default()
intents.message_content = True


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)


