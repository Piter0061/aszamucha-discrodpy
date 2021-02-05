####################################################
##            aszamucha bot for discrod           ##
##              || PYTHON EDITION ||              ##
##                    by peter                    ##
####################################################
import discord
import reddit as REE
import download_image_to_local_machine as download
import imgGO

f = open("token.txt", "r")
token = f.readline()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content

    if content.startswith('hentai'):
        henurl = REE.goReddit("hentai")
        await message.channel.send(henurl)
        download.download(henurl)

    elif content.startswith('huj'):
        await message.channel.send(REE.goReddit("gayporn"))

    elif content.startswith('porn'):
        await message.channel.send(REE.goReddit("porn"))

    elif content.startswith('img'):
        print(' '.join(message.content.split(' ')[1:]))
        print(imgGO.FETCH(str(message.content.split(' ')[1:])))
        await message.channel.send(imgGO.FETCH(' '.join(message.content.split(' ')[1:])))

    elif content.startswith('wiki'):
        await message.channel.send("ALSO TO DO, YA FOCKING CUNT")
    
client.run(token)
