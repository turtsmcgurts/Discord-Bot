import discord
from discord.ext import commands
import asyncio
import tokenfile #where we store my bots token code so it isn't on public display

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
    
#when somebody joins a voice channel
@client.event
async def on_voice_state_update(before, after):
    #before The Member whose voice state changed prior to the changes
    #after The Member whose voice state changed after the changes
    print('{} joined voice channel "{}"'.format(after, after.voice.voice_channel))

    
client.run(tokenfile.token)