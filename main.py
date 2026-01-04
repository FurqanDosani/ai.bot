# This example requires the 'message_content' intent.

import discord
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
discord_key= os.getenv("discord_token")
google_key= os.getenv("g_key")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if client.user != message.author:
        if client.user in message.mentions:
        

          # The client gets the API key from the environment variable `GEMINI_API_KEY`.
          client_google = genai.Client(api_key=google_key)
          response = client_google.models.generate_content(
          model="gemini-2.5-flash", contents=message.content
          )
          print(response.text)
          await message.channel.send(response.text)

client.run(discord_key)

