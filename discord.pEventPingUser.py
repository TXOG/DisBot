#event
@client.event
#read messages
async def on_message(message): 
#ingore bot text
    if message.author == client.user:
     return
    #prefix is ~ - look for ping command
    if message.content.startswith("~ping"):
        #ping user
        await message.channel.send(f"{message.author.mention}"
