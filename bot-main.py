import discord
from discord.ext import commands
import os

bot = discord.Bot()

@bot.event
async def botLoad():
    print('Bot logged in as {0.user}'.format(client))

bot = commands.Bot(command_prefix='xkcd')

@bot.command
async def comic(context, *, args):
    await context.send 'https://xkcd.com/%s' % (args)

bot.run('pretend this is a token')
