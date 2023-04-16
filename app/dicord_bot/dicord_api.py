from dotenv import load_dotenv
import discord
import os
from app.chatgpt_ai.openaiFetch import chatgpt_response

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class myClient(discord.Client):
    async def on_ready(self):
        print("Succesfully logged in as: ", self.user)

    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return

        command, user_msg = None, None

        for text in ['/ai', '/bot', '/chatgpt']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_msg = message.content.replace(text, '')
                print(command, user_msg)

        if command == '/ai' or command == '/bot' or command == '/chatgpt':
            bot_response = chatgpt_response(user_msg)
            await message.channel.send(f"Answer: {bot_response}")
            
intents = discord.Intents.default()
intents.message_content = True

client = myClient(intents = intents)