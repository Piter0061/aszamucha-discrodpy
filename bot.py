####################################################
##            aszamucha bot for discrod           ##
##              || PYTHON EDITION ||              ##
##                    by peter                    ##
####################################################
import discord
import gO as REE
import download_image_to_local_machine as download
import imgGO

f = open("token.txt", "r")
token = f.readline()

f1 = open("coolusers.txt", "r")
coolusers = f1.readlines()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("aszysko")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content
    mess = ' '.join(message.content.split(' ')[1:])

    if content.startswith('hentai'):
        henurl = REE.goReddit("hentai")
        await message.channel.send(henurl)
        download.download(henurl)

    elif content.startswith('huj'):
        await message.channel.send(REE.goReddit("gayporn"))

    elif content.startswith('porn'):
        await message.channel.send(REE.goReddit("porn"))

    elif content.startswith('gogoreddit'):
        try:
            await message.channel.send(REE.goReddit(mess))
        except:
            await message.channel.send('nie')
    
    elif content.startswith('gpt'):
        try:
            await message.channel.send(REE.goGpt(mess))
        except:
                await message.channel.send('nie')
    elif content.startswith('img'):
        print(mess)
        print(imgGO.FETCH(str('https://www.google.com/search?q='+ mess +'&tbm=isch&ved=2ahUKEwiD0uSA09LuAhVQyCoKHW29DjYQ2-cCegQIABAA&oq=kingus&gs_lcp=CgNpbWcQAzIECCMQJzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIAFCg6wNY-fADYJzyA2gAcAB4AIABYYgB8AOSAQE2mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=Ay0dYMPEGNCQqwHt-rqwAw&bih=966&biw=1903&hl=en')))
        await message.channel.send(imgGO.FETCH('https://www.google.com/search?q='+ mess +'&tbm=isch&ved=2ahUKEwiD0uSA09LuAhVQyCoKHW29DjYQ2-cCegQIABAA&oq=kingus&gs_lcp=CgNpbWcQAzIECCMQJzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIAFCg6wNY-fADYJzyA2gAcAB4AIABYYgB8AOSAQE2mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=Ay0dYMPEGNCQqwHt-rqwAw&bih=966&biw=1903&hl=en'))

    elif content.startswith('wiki'):
        await message.channel.send("ALSO TO DO, YA FOCKING CUNT")

    elif content.startswith('changepresence'):
        await message.channel.send("changing")
        game = discord.Game(mess)
        await client.change_presence(status=discord.Status.idle, activity=game)
    
    elif content.startswith('lickasza'):
        await message.channel.send(":kissing_heart:")
        game = discord.Game(mess)
        await client.change_presence(status=discord.Status.idle, activity=game)
    
    elif content.startswith('killasza'):
        print(message.author)
        if str(message.author)+"\n" in coolusers:
            await message.channel.send("die")
            await client.change_presence(status=discord.Status.offline)
            quit()
        else:
            await message.channel.send("spierdalaj gnoju")

    elif content.startswith('shibe'):
        await message.channel.send(REE.goShibe())
    
    elif content.startswith('biblia'):
        await message.channel.send(REE.bibblia())

    elif content.startswith('fromwebsite'):
        await message.channel.send(imgGO.FETCH(mess))
client.run(token)
