####################################################
##            gayfield  bot for discrod           ##
##              || PYTHON EDITION ||              ##
##                    by peter                    ##
####################################################
import discord
import random
import i_ate_lasagnias
import time

f = open("token.txt", "r")
token = f.readline()


changeprofile = False
feed_lasagnia = 1         #how much one FEED HIM commad gives
hunger = 50               #every x messages garfield looses one lasagnia
hunger_treshold = 5       #if lasagnia lower than that value then he is starving
playSoudnWhenEat = True   #if FEED HIM   connect to a voice chat and play eat sound

################ random name on boot lol #############
f1 = open("garfel-profile-pic/names.txt", "r")
namess = f1.readlines()
#namesss = namess.splitlines()
randomn = int(random.random() * len(namess))
print("tody name: " + namess[randomn])
######################################################

################ random pic on boot lol ##############
how_many_photos = 3
randomp = int(random.random() * how_many_photos + 1)
f2 = open("garfel-profile-pic/garfel-"+ str(randomp) +".png", "rb")

######################################################

#################### lasagna count ###################
f3 = open("garfel-profile-pic/lasagnas.txt", "r")
lasagnas = f3.readlines()
#print(lasagnas)
lasagnascount = int(lasagnas[0])
print("I remember lasagnias: " + str(lasagnascount))
f3.close()

#f1.write(str(lasagnas + 1))
######################################################

client = discord.Client()


#uwugive.start()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("with "+ str(lasagnascount) +" lasagnas")
    await client.change_presence(status=discord.Status.online, activity=game)
    try:
        if changeprofile:
            await client.user.edit(avatar=f2.read(), username=namess[randomn])
        else:
            await client.user.edit(username=namess[randomn])
    except:
        print("cant change username and pic yet")
    
countmessages = 0
@client.event
async def on_message(message):
    global countmessages
    global lasagnascount
    global hunger
    countmessages+= 1

    if countmessages % hunger == 0: 
        lasagnascount-= 1
        save_lasagnia_to_file()
        game = discord.Game("with "+ str(lasagnascount) +" lasagnas")
        await client.change_presence(status=discord.Status.online, activity=game)


    if message.author == client.user:
        return
    
    content = message.content
    mess = ' '.join(message.content.split(' ')[1:])
        
    #mention = f'<@{client.user.id}>'

    if content.startswith('garfield'):
        if lasagnascount >= hunger_treshold:
            i_ate_lasagnias.makeImage(lasagnascount)
            await message.channel.send(file=discord.File('garfel-profile-pic/I-ate-made.png'))
            #await message.channel.send("humanity lever normal")
        else:
            await message.channel.send(file=discord.File('garfel-profile-pic/przyklad.png'))
    
    elif content.startswith('FEED HIM'):
        last_lasagnia = lasagnascount
        lasagnascount += feed_lasagnia
        if lasagnascount >= hunger_treshold and last_lasagnia < hunger_treshold:
            await message.channel.send(file=discord.File('garfel-profile-pic/garfel-1.png'))
            await message.channel.send("humanity restored")
        else:
            await message.channel.send(file=discord.File('garfel-profile-pic/eats-lasagna/' + str((int(random.random() * 4)+1)) +'.jpg'))
        save_lasagnia_to_file()
        game = discord.Game("with "+ str(lasagnascount) +" lasagnas")
        await client.change_presence(status=discord.Status.online, activity=game)
        if playSoudnWhenEat:          #PLAY SOUND WHEN EAT
            if message.author.voice is None:
                return
            else:
                if message.guild.voice_client is None:
                    await message.author.voice.channel.connect()
                message.guild.voice_client.play(discord.FFmpegOpusAudio("cateat.m4a"))
                time.sleep(10)
                await message.guild.voice_client.disconnect()

    ###################### VOICE ####################
    elif content.startswith('rawr'):
        if message.author.voice is None:
            await message.channel.send("dzie niby")
            return
        
        if message.guild.voice_client is None:
            await message.author.voice.channel.connect()

        try:
            message.guild.voice_client.play(discord.FFmpegOpusAudio("glass.mp3"))
        except:
            await message.channel.send("nje.")
        #await message.guild.voice_client.disconnect()


    elif content.startswith('icsobie'):
        if message.guild.voice_client is None:
            #await message.channel.send("Not connected.")
            return
        #Disconnect
        await message.guild.voice_client.disconnect()
        await message.channel.send("ide sobie")
    ###################### VOICE ######################

def save_lasagnia_to_file():
    f4 = open("garfel-profile-pic/lasagnas.txt", "w")
    f4.write(str(lasagnascount))
    f4.close()
    print(lasagnascount)

client.run(token)
