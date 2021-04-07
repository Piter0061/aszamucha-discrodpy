####################################################
##       aszamucha bot for facebook messenger     ##
##              || PYTHON EDITION ||              ##
##                    by peter                    ##
####################################################

import gO as REE
import download_image_to_local_machine as download
import imgGO
#import pickle

from fbchat import Client
#from fbchat import *

f = open("login.txt", "r")
login = f.readlines()


#message_id = client.send(Message(text='message'), thread_id=pioter, thread_type=ThreadType.USER)
#client.reactToMessage(message_id, MessageReaction.LOVE)


class CustomClient(Client):
     
    def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
        #self.markAsDelivered(thread_id, message_object.uid)
        #self.markAsRead(thread_id)
        if author_id != self.uid:
            import fbchat
            messagee = message_object.text
            pref = str(message_object.text).split()[0]
            print(messagee)
            print(pref)
            mess = ' '.join(str(message_object.text).split(' ')[1:])

            if pref == 'hentai':
                self.sendRemoteImage(
                    REE.goReddit("hentai"),
                    message=fbchat.Message(text="JEdzcie i pijcie z teg0 wszyscy"),
                    thread_id=thread_id,
                    thread_type=thread_type,
                )

            elif pref == 'huj':
                self.sendRemoteImage(
                    REE.goReddit("gayporn"),
                    message=None,
                    thread_id=thread_id,
                    thread_type=thread_type,
                )

            elif pref == 'porn':
                self.sendRemoteImage(
                    REE.goReddit("porn"),
                    message=None,
                    thread_id=thread_id,
                    thread_type=thread_type,
                )

            elif pref == 'img':
                self.sendRemoteImage(
                    imgGO.FETCH('https://www.google.com/search?q='+ mess +'&tbm=isch&ved=2ahUKEwiD0uSA09LuAhVQyCoKHW29DjYQ2-cCegQIABAA&oq=kingus&gs_lcp=CgNpbWcQAzIECCMQJzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIAFCg6wNY-fADYJzyA2gAcAB4AIABYYgB8AOSAQE2mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=Ay0dYMPEGNCQqwHt-rqwAw&bih=966&biw=1903&hl=en'),
                    message=None,
                    thread_id=thread_id,
                    thread_type=thread_type,
                )
            
            elif pref == 'shibe':
                self.sendRemoteImage(
                    REE.goShibe(),
                    message=None,
                    thread_id=thread_id,
                    thread_type=thread_type,
                )

            elif pref == 'helloo':
                self.send(fbchat.Message(text='HI GUYSSS'), thread_id=thread_id, thread_type=thread_type)
        pass

client = CustomClient(login[0][:-1], login[1], user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36")

client.listen()
#client.logout()