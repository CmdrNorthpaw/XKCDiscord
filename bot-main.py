# Imports the modules for operation and gets the key from the environment
import discord
from discord.ext import commands
import qwant
from time import sleep
from os import environ
key = environ.get('discordKey')

bot = commands.Bot(command_prefix='xkcd ')

# Tells me when the bot logs in.
@bot.event
async def on_ready():
    print('Bot logged in.')

# Controls the bot's fetch command
@bot.command()
async def fetch(ctx, arg):
    if arg == 'latest':
        await ctx.send('https://xkcd.com')
    else:
        await ctx.send('https://xkcd.com/%s' % str(arg))

#Controls the bot's find command
@bot.command()
async def find(ctx, *, arg):
    search = 'Null'
    await ctx.send('`Searching for xkcd comic...`')
    query = f'site:www.xkcd.com {arg}'
    search = qwant.items(query, count=1)
    search = search[0]
    search = str(search['url'])
    search = search.replace('www.', '')
    print(search)
    await ctx.send(search)

# Actually runs the bot, using the key from line 6 as an argument
bot.run(key)
