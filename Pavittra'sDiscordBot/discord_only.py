from dotenv import load_dotenv
import discord
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

clients = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(clients))

@client.event
async def on_message(message):
    if message.author == client.user:
        return None
    if message.content.startswith("$hello"):
        await messahe.channel.send("Hello!")

client.run(os.getenv("TOKEN"))