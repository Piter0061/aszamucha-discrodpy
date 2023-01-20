####################################################
##            aszamucha bot for discrod           ##
##              || PYTHON EDITION ||              ##
##                    by peter                    ##
####################################################
import discord     #discord[voice]  needed!!
from discord.ext import commands
import gO as REE
import download_image_to_local_machine as download
import imgGO
##import giveMeYourHentai as uwugive
import new_day_image_creator
import musicalbaba
import asyncio

f = open("token.txt", "r")
token = f.readline()

#f1 = open("coolusers.txt", "r")
coolusers = "pie"

#new in discordpy 1.5
#client = discord.Client()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
#uwugive.start()

#d = {'guild': ["song1", "song2", "song3"]}
queye = {'754731874097823916': [" "]}

class Buttons(discord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Button",style=discord.ButtonStyle.gray)
    async def gray_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.response.edit_message(content=f"This is an edited button response!")

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

   


    elif content.startswith('sk ') or content.startswith('grajgrajgraj'):
        guild = str(message.guild.id)
        #queye[guild] = []
        print(f'line 114 guild: {guild}')
        #if guild in queye:
        #    queye[guild].append(mess)
        #else:
        #    queye[guild] = [mess]
        print(f'line 119: {queye[guild]}')
        await message.channel.typing()
        if message.author.voice is None:                       
            await message.channel.send("co ty pierdolisz") ##10101010100001 nie ma cie nigdzie :sex: 
            return

        if message.guild.voice_client is None:
            voice = await message.author.voice.channel.connect()
            #if queye[guild] == []:
            #    song = mess
            #else:
            #    song = queye[guild]
        
        if not message.guild.voice_client.is_playing():
            if queye[guild] == [" "]:
                await message.channel.send("pobieram!")
                musicFilename = musicalbaba.downloadVideo(mess)            
                if musicFilename != 1:                                    
                    try:
                        await message.channel.send("granie panie.")
                        voice.play(discord.FFmpegOpusAudio(musicFilename), after=lambda e: play_next(voice, guild))
                        print(message.guild.voice_client.channel)
                    except:
                        await message.channel.send("nje.") #  ¯\_(ツ)_/¯
                else:
                    await message.channel.send("błąd jakiś")
            else:
                play_next(voice, guild)
        else:
            #if len(queye[guild]) == 1:
            #    queye[guild] = [mess]
            #else:
            queye[guild].append(mess)
            await message.channel.send(f'dodaje **"{mess}"** do KOLEJKI (*WHATT????* tego typu)')
            print(f'line 153: {queye[guild]}')


    elif content.startswith('pobierz'):
        await message.channel.send("pobieram!")
        musicFilename = musicalbaba.downloadVideo(mess)            
        if musicFilename != 1:                                    
            try:
                await message.channel.send(file=discord.File(musicFilename))
            except:
                await message.channel.send("nje.")
        else:
            await message.channel.send("błąd pobierania")
        

    elif content.startswith('icsobie'):
        if message.guild.voice_client is None:
            return
        await message.guild.voice_client.disconnect()
        queye[str(message.guild.id)] = [" "]
        #await message.channel.send("pubum")

    elif content.startswith('skip'):
        print("skipuje")
        if message.guild.voice_client is None:
            return
        await message.channel.send("skipuje")
        await message.guild.voice_client.stop()
        play_next(message.guild.voice_client, str(message.guild.id))
    
    elif content.startswith('aszysko'):
        if message.guild.voice_client is None or not message.guild.voice_client.is_playing():
            embed=discord.Embed(title="** **", url="https://discord.gg/D7R2aqJCX6", description="** **", color=0xea48e7)
            embed.set_author(name="Nic nie gra")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/759853703397769246/1041140275436859573/IMG_0650.jpg")
            embed.set_footer(text="asza mucha")
            embed.add_field(name="** **", value="** **", inline=True)
            await message.channel.send(embed=embed,view=Buttons())
        else:
            embed=discord.Embed(title="Moc, energia, amfetamina", url="", description="** **", color=0xff0000)
            embed.set_author(name="Obecnie gra:")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/759853703397769246/1041140275436859573/IMG_0650.jpg")
            embed.set_footer(text="asza mucha")
            embed.add_field(name="next:", value="moc, energia, amfetamina", inline=True)
            await message.channel.send(embed=embed)

def play_next(voice, guild):
    print("play_next")
    if queye[guild] == [" "]:
        print("end of quellelele")
        #coro = some_channel.send('Song is done!')
        #fut = asyncio.run_coroutine_threadsafe(coro, client.loop)
        #try:
        #    fut.result()
        #except:
        #    # an error happened sending the message
        #    pass
    else:
        musicFilename = musicalbaba.downloadVideo(queye[guild][1]) ##queye[guild][len(queye[guild])-1]
        if not len(queye[guild]) == 1:
            queye[guild].remove(queye[guild][1])
        else:
            queye[guild] = [" "]
        print(f'line 193 queue: {queye[guild]}')

        voice.play(discord.FFmpegOpusAudio(musicFilename), after=lambda e: play_next(voice, guild))
    

client.run(token)
