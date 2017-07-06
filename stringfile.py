#this is here just so I don't clutter up the main file with shit. would be noticable if I expand on the project

#HELP RESPONSES
generic_help_response = 'Bot created by turtsmcgurts for general use. https://github.com/turtsmcgurts/Discord-Bot'
uses_help_response = 'Currently the only use is for giving voice channels their own private text channels, similar to mumble or any other VoIP really.'
help_commands = 'For more detail: "!help textchannel"'
textchannel_help_response = ('In order to add a text channel to a voice channel, create a text channel (same name as voice; hyphens instead of spaces), then create '
                             'a role of the same name as the voice channel, then suffix it with "-textchannel". '
                             '\n\nIf you wish for the bot to purge text channels of all text when their corresponding voice channel is empty, simply give the bot access to the channel. (Give it the role you create)'
                             '\n\nExample setup: voice channel named "General Voice". Text channel named "General-Voice". Role named "General Voice-textchannel". Make it so only that role sees the text channel.')