import discord
import asyncio
import tokenfile #where we store my bots token code so it isn't on public display

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
    
client.run(tokenfile.token)