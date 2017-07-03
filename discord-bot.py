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
    
    
#called when somebody joins or leaves a voice channel. also when they mute/unmute.
@client.event
async def on_voice_state_update(before, after):
    #before The Member whose voice state changed prior to the changes
    #after The Member whose voice state changed after the changes
    
    #make sure no cross server shennanegains happens
    if before.server == after.server:
        #filters out mute/unmutes
        if not before.voice.voice_channel == after.voice.voice_channel:
            #print('{} joined voice channel "{}" from "{}"'.format(after, after.voice.voice_channel, before.voice.voice_channel))
            
            role_list = before.roles #make a list of the users old roles
            value_changed = False
            
            try:
                #add new role to user
                if not after.voice.voice_channel is None:
                    rolename = after.voice.voice_channel.name + '-textchannel' #the role we will create for the channel
                    role = discord.utils.get(before.server.roles, name=rolename)
                    if(not role is None):
                        role_list.append(role)
                        value_changed = True
            except:
                pass
            
            try:
                #remove old role from user, if it exists
                if not before.voice.voice_channel is None:
                    rolename = before.voice.voice_channel.name + '-textchannel' #the role we will create for the channel
                    role = discord.utils.get(before.server.roles, name=rolename)
                    if role in role_list:
                        role_list.remove(role)
                    
                    value_changed = True
            except:
                pass
                
            try:
                if value_changed == True:
                    await client.replace_roles(after, *role_list)
            except:
                pass
            
            #we opt to copy, change and replace the users rolelist instead of manually
            #adding and removing roles because, for whatever reason, you can't both
            #client.add_role and client.remove_role in the same function, it only do one.
        

#simple check to see if a voice channels text channel role exists, if not it creates it
async def check_role_exists(desired_server, role_name):
    try:
        role = discord.utils.get(desired_server.roles, name=role_name)
        if role == None:
            return False
        else:
            return True
    except:
        pass
        
client.run(tokenfile.token)