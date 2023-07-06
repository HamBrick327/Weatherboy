import disnake
from disnake.ext import commands
from time import sleep
import asyncio
import os
import requests
import json


token = os.getenv('WEATHERTOKEN')
api_key = os.getenv('WEATHERAPIKEY')
baseurl = "https://api.openweathermap.org/data/2.5/weather?q=herriman&appid=" + api_key

'''
"This should not be very hard" - Famous last words, Isaac 6/13/23
'''


## bot settings
# I don't remember what this does
command_sync_flags = commands.CommandSyncFlags.none()
command_sync_flags.sync_commands = False
intents = disnake.Intents.default()
intents.message_content = False
intents.messages = True
intents.voice_states = False

bot = commands.Bot(
    command_prefix=disnake.ext.commands.when_mentioned,
    intents=intents,
    command_sync_flags=command_sync_flags
    )

@bot.event
async def on_ready():
    channel = bot.get_channel(1118235007136305293)
    print(f'{bot.user} is ready')
    print('--------------')

    while True:
        weather = requests.get(baseurl).json()['weather']
    
        print(weather)
        if weather[0]['main'] == 'Rain':
            await channel.send('It is raining in Ba Sing Se.')
            print("notified Caden")
        sleep(3600)

bot.run(token)