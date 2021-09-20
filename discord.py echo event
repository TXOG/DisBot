#import shlex module
import shlex

#event 
@client.event
async def on_message(message): 
    #ignores messages from bot
    if message.author == client.user:
    return
    
    #~ is the prefix used in this example
    if message.content.startswith("~echo"):
        #ignores bot text again (see lines 7 -9)
        if message.author == client.user:
            return
        #bot will have admin perms, stop bot from pinging everyone
        elif "everyone" in message.content:
            #deletes command useage
            await message.delete()
            #pings the user with message saying they can't use everyone in their echo
            await message.channel.send(f"{message.author.mention} you can't use `everyone` in your echo")
        elif "here" in message.content:
            #deletes command useage
            await message.delete()
            #pings the user with message saying they can't use here in their echo
            await message.channel.send(f"{message.author.mention} you can't use `here` in your echo")
        else:
            #lines 29 - 32 copy message and remove ~echo from the copied message
            arguments = message.content.lstrip("~echo")
            arguments = message.content.split(" ", 1)
            arguments = shlex.split(message.content)[1:]
            arguments = message.content[len("~echo"):]
            #saves variable msg as the old message - ~echo
            msg = arguments
            #deletes command useage
            await message.delete()
            #sends final responce
            await message.channel.send(msg)
