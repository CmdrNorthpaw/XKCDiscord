import discord
from discord.ext import commands
from googlesearch import search
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

@bot.command()
async def find(ctx, arg):
    ctx.send('`Searching for xkcd comic...`')
    queryResult = search(arg, tld=com, num=1 stop=1, pause=2))
    ctx.send(queryResult)


bot.run('Pretend this is a token')
