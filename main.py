import discord
import os
import requests
import json


client = discord.Client()

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_res = json.loads(response.text)
    quote = json_res[0]['q'] + ' -' + json_res[0]['a']
    return quote


@client.event
async def on_ready():
    print("Welcome {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
        await message.channel.send(get_quote())

client.run(os.getenv('TOKEN'))


