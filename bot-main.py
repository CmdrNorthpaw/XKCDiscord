import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='xkcd ')

@bot.event
async def on_ready():
    print('Bot logged in.')




bot.run('NjYyOTc5Nzc1MDYwNjM5NzUx.XhR8aw.lELfhHQYp3o8gmKv1zisTOS6ePM')
