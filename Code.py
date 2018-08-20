import discord
import asyncio
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
from random import randint
client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('copy paste this in your browser to authorize bot https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=0'.format(os.environ['CLIENTID']))
    print('------')

@client.event
async def on_message(message):
  await client.change_presence(game=discord.Game(name="&commands"))

if message.content.startswith('&help'):
    await client.send_message(message.channel,'{0.author.mention} check your DM's ')

if message.content.startswith('&help'):
    await client.send_messageuser(message.channel,'I'm @Aimbot . Heres what I can do:  \n')
  

client.run(os.environ['TOKEN'])
