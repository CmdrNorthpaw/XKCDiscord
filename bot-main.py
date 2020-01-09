# Imports the modules for operation and gets the key from the environment
import discord
from discord.ext import commands
import qwant
from time import sleep
from os import environ
key = environ.get('discordKey')

bot = commands.Bot(command_prefix='xkcd ')

searchList = []
searchListIndice = 0
search = ''
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
    await ctx.send('`Searching for xkcd comic...`')
    query = f'site:www.xkcd.com {arg}'
    global searchList = qwant.items(query, count=10)
    global searchListIndice = 0
    global search = searchList[0]
    global search = str(search['url'])
    global search = search.replace('www.', '')
    print(search)
    await ctx.send(search)
    await ctx.send('Wrong comic? React with ❎ to tell me!')

@bot.event
async def on_reaction_add(reaction, user):
    print(reaction.emoji)
    print(user.name)
    if reaction.emoji == '❎' and user.name != 'XKCDiscord':
        global searchListIndice = searchListIndice + 1
        if searchListIndice > 10:
            print("Sorry, that's all the comics I have! Try a different search term.")
        else:
            global search = searchList[searchListIndice]
            global search = str(search['url'])
            global search = search.replace('www.', '')
            await ctx.send(search)
            await ctx.send('Wrong comic? React with ❎ to tell me!')


# Actually runs the bot, using the key from line 6 as an argument
bot.run(key)
