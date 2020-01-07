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
    await ctx.send('`Searching for xkcd comic...`')
    for query in search(arg, tld=com, num=1, stop=1, pause=2):
        await ctx.send(query)


bot.run('NjYyOTc5Nzc1MDYwNjM5NzUx.XhSJQg.N9qHbgvC3bfy7ufWPoMucTYJCHo')
