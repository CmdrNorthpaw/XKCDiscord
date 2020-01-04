import discord
from discord.ext import commands
import os

client = discord.Client()

@client.event
async def botLoad():
    print('Bot logged in as {0.user}'.format(client))

@client.event
async def recieveMessage(message):
    if message.author == client.user:
        return
    elif message.content.startswith('$hello'):
        await message.channel.send('Greetings, mortal')

client.run('NjYyOTc5Nzc1MDYwNjM5NzUx.XhDPjA.BTJyeqbCGRsBZZMu6eeQZxF8HGk')
