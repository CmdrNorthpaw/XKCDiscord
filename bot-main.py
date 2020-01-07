import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='xkcd ')

@bot.event
async def on_ready():
    print('Bot logged in.')

@bot.command()
async def fetch(ctx, arg):
    if arg == 'latest':
        await ctx.send('https://xkcd.com')
    else:
        await ctx.send('https://xkcd.com/%s' % str(arg))


bot.run('Pretend this is a token')
