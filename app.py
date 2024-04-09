import discord
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('BOT_TOKEN')


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')


intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
client.run(token)


