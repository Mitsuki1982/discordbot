import discord
from discord import activity
from discord.ext import commands

import time
import random as rnd
import string

bot = commands.Bot(command_prefix = '!')
bot.remove_command('help')

# Delay before next commend is 2-3 seconds
delay = 0

@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching, name="a movie")
    await bot.change_presence(activity=activity)
    
    print('[BOT] bot is online..')

@bot.event
async def on_message(message):
    global delay

    if message.author != bot:
        if message.content.startswith(bot.command_prefix):

            if delay + 3 <= round(time.time()):

                if message.content == '<@!887413177925664860>':
                    await message.channel.send('My prefix "!"')

                elif message.content == bot.command_prefix + 'psc':
                    psc_code = rnd.randint(int("1"*15), int("9"*15))
                    author = message.author

                    await message.channel.send("Check DM!")
                    await author.send(f"Your generated psc code: 0{psc_code}")

                elif message.content == bot.command_prefix + 'nitro':
                    chars = string.ascii_lowercase + string.ascii_uppercase
                    author = message.author
                    nitro_code = ''

                    for _ in range(16):
                        nitro_code += rnd.choice(chars)

                    await message.channel.send("Check DM!")
                    await author.send(f"Your generated nitro code: https://discord.gift/{nitro_code}")

                elif message.content == bot.command_prefix + 'stock':
                    embed = discord.Embed(title='My Commands', color=0x00ff00)
                    embed.add_field(name='psc', value='Generate your psc code')
                    embed.add_field(name='nitro', value='Generate your nitro code')
                    await message.channel.send(embed=embed)

                elif message.content == bot.command_prefix + 'clearallmessages':
                    await message.channel.purge(limit=100000000000000)

                else:
                    await message.channel.send('Such a command does not exist')

                delay = round(time.time())

            else:
                await message.channel.send('Wait a moment before the next command')

bot.run('ODg3NDEzMTc3OTI1NjY0ODYw.YUDx7A.6kD57I5sP2wiZPmEiL8eQTINZD4')
