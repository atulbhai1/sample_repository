from dotenv import load_dotenv
from openai import OpenAI
import discord
import os

os.environ["OPENAI_API_KEY"] = "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"
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
oa_client = OpenAI(api_key = OPENAI_KEY)
intents = discord.Intents.default()
intents.message_content = True

clients = discord.Client(intents=intents)

def call_openai(question):
    completion = oa_client.completions.create(
        model="gpt-4o",
        prompt=f"Respond like a pirate to the following question: {question}"
    )
    response = completion.choices[0].message.content
    print(response)
    return response

@clients.event
async def on_ready():
    print("We have logged in as {0.user}".format(clients))

@clients.event
async def on_message(message):
    if message.author == clients.user:
        return None
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")
    if message.content.startswith("$question"):
        print(f"Message: {message.content}")
        message_content = message.content.split("$question")[1]
        print(f"Question: {message_content}")
        response = call_openai(message.content)
        print(f"Assistant: {response}")
        print("--")
        await message.channel.send(response)


clients.run(os.getenv("TOKEN"))