import discord
import random
import asyncio
import requests
import os
from os.path import join, dirname
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
  await client.change_presence(game=discord.Game(name="&help"))

  if message.content.startswith('&help'):
    await client.send_message(message.channel,":e_mail: <@%s> check your DM's " % (message.author.id))
		 
  
 if message.content.startswith('&src'):
    await client.send_message(message.channel,'https://github.com/FreddyMarsden/Aimbot')
                              
  if message.content.startswith('&log'):
    await client.send_message(message.channel,'') 

  if message.content == "test role":
           role = discord.utils.get(server.roles, name="test role")
           await client.add_roles(message.author.id, role)


  
token = os.environ.get("TOKEN")
client.run(token)

