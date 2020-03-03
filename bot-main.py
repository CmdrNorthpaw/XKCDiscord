# Imports the modules for operation and gets the key from the environment
import discord
from discord.ext import commands
import qwant
from time import sleep
from os import environ
key = environ.get('discordKey')

bot = commands.Bot(command_prefix='xkcd ')
bot.remove_command('help')

searchList = []
searchListIndice = 0
search = ''
searchResult = ''
postMessage = ''
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
    global search
    global searchList
    global searchListIndice
    global searchResult
    global postMessage
    global preMessage
    preMessage = await ctx.send('`Searching for xkcd comic...`')
    query = f'site:xkcd.com {arg}'
    searchList = qwant.items(query, count=10)
    searchListIndice = 0
    search = searchList[0]
    search = str(search['url'])
    search = search.replace('www.', '')
    print(search)
    searchResult = await ctx.send(search)
    postMessage = await ctx.send('`Wrong comic? React with ❎ to tell me!`')
    await postMessage.add_reaction('❎')

@bot.event
async def on_reaction_add(reaction, user):
    global searchList
    global searchListIndice
    global search
    global searchResult
    global postMessage
    global preMessage
    channel = reaction.message.channel
    if reaction.emoji == '❎' and user.name != 'XKCDiscord':
        searchListIndice = searchListIndice + 1
        if searchListIndice > len(searchList):
            await channel.send('Sorry, that\'s all the comics I have! Try a different search term')
        else:
            await searchResult.delete()
            await postMessage.delete()
            search = searchList[searchListIndice]
            search = str(search['url'])
            search = search.replace('www.', '')
            searchResult = await channel.send(search)
            postMessage = await channel.send('`Wrong comic? React with ❎ to tell me`')
            await postMessage.add_reaction('❎')

@bot.command
async def help(ctx):
    embed = discord.Embed(
    color=discord.colour.Purple()
    title='XKCDiscord Help'
    description='Thank you for using XKCDiscord! Here are some commands to help you along the way'
    )
    embed.set_thumbnail(url='https://what-if.xkcd.com/imgs/a/14/short_answers_headscratch.png')
    embed.set_author(name='XKCDiscord, by CmdrNorthpaw', icon_url='https://cdn.discordapp.com/avatars/662979775060639751/7a44d391e0bd8c02ce9a00b7e7b53b3e.png')
    embed.add_field(
    name='xkcd fetch'
    value='This command takes the cartoon number as an argument (say 1646) and posts that comic to chat. You can also fetch the latest comic with `xkcd fetch latest`'
    )
    embed.add_field(
    name='xkcd find'
    value='This command is used to search for a cartoon (say twitter bot). Perfect for when you know what cartoon you want but you can\'t remember the exact number. Don\'t worry if it doesn\'t get the right cartoon first time, just click the ❎ to see the next result'
    )

# Actually runs the bot, using the key from line 6 as an argument
bot.run(key)
