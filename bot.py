####################################################
##            aszamucha bot for discrod           ##
##              || PYTHON EDITION ||              ##
##                    by peter                    ##
####################################################
import discord     #discord[voice]  needed!!
import gO as REE
import download_image_to_local_machine as download
import imgGO
##import giveMeYourHentai as uwugive
import new_day_image_creator
import musicalbaba

f = open("token.txt", "r")
token = f.readline()

f1 = open("coolusers.txt", "r")
coolusers = f1.readlines()

client = discord.Client()

#uwugive.start()


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
        await message.channel.send(REE.bibbliaPol())

    elif content.startswith('fromwebsite'):
        await message.channel.send(imgGO.FETCH(mess))
    
    elif content.startswith('time'):
        new_day_image_creator.doTime()
        await message.channel.send(file=discord.File('time.png'))
    ############# music!!! ##############################

    elif content.startswith('grajgrajgraj'):
        await message.channel.send("pobieram!")
        musicFilename = musicalbaba.downloadVideo(mess)            #download the song, ough that gotta hurt the space. limited to 15MB in musicalbaba.py ;)
        if musicFilename != 1:                                     #if didnt fail
            await message.channel.send("granie panie.")
            #######################################################
            if message.author.voice is None:                       #no one in voice, why connect
                await message.channel.send("10101010100001 nie ma cie nigdzie :sex: ")
                return
            #######################################################
            if message.guild.voice_client is None:                #if NOT connected then..
                await message.author.voice.channel.connect()      #connect
            try:
                message.guild.voice_client.play(discord.FFmpegOpusAudio(musicFilename)) #TRY to play downloaded music
            except:
                await message.channel.send("nje.")                                    #didnt work
                #await message.guild.voice_client.disconnect()
        else:
            await message.channel.send("za grube")

    elif content.startswith('icsobie'):
        if message.guild.voice_client is None:
            return
        await message.guild.voice_client.disconnect()
        #await message.channel.send("pubum")

client.run(token)
