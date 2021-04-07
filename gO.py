################################################################
# this is just an api wrapper to fetch requested reddit images #
################################################################
import requests
import json
import random

def goReddit(sub):
    randoompoost = int(random.random() * 20)
    url = "http://reddit.com/r/"+ sub +".json"
    y = fetchJSON(url)
    try:
        link = y["data"]["children"][randoompoost]["data"]["url_overridden_by_dest"]
    except:
        link = y["data"]["children"][randoompoost+2]["data"]["url_overridden_by_dest"]
    finally:
        return(link)


def bibblia():
    url = "https://labs.bible.org/api/?passage=random"
    headers = {
	        "Accept": "text/html",
	        "User-Agent": "Chrome"
	    }
    r = requests.get(url, headers=headers)
    if(r.status_code != 200):
        return('https://http.cat/' + r.status_code + '.jpg')
    return r.text.split('>')[2]

def bibbliaPol():
    a = int(random.random() * 10)
    b = int(random.random() * 29)
    url = "https://api.scripture.api.bible/v1/bibles/1c9761e0230da6e0-01/verses/JER."+ str(a) +"."+ str(b) +"?content-type=text&include-notes=false&include-titles=false&include-chapter-numbers=false&include-verse-numbers=true&include-verse-spans=false&use-org-id=false"
    headers = {
	        "Accept": "text/html",
	        "User-Agent": "Chrome",
            "api-key": "c210e5a07b06449eeb52e5a10f5e0260"
	    }
    r = requests.get(url, headers=headers)
    if(r.status_code != 200):
        return('https://http.cat/' + str(r.status_code) + '.jpg')
    
    #print(r.text)
    retrn = r.json()
    return retrn['data']['content']
    
def goShibe():
    randoom = int(random.random() * 20)
    url = "http://shibe.online/api/shibes?count=21"
    y = fetchJSON(url)
    try:
        link = y[randoom]
    except:
        link = "i dunno what happend"
    finally:
        return link

def goGpt(mess):
    try:
        r = requests.post(
            "https://api.deepai.org/api/text-generator",
        data={
            'text': mess,
        },
        headers={'api-key': '44aed190-70e4-4487-aed4-4675178e2df2'}
        )
        #print(r.json())
        y = r.json()
        retrn = y["output"]
        #print(y["output"])
        retrn = retrn[:500]
        #retrn = r.json()
    except:
        #r.json()
        #print('die in gO.py, goGpt, line 42 :)')
        retrn = 'die in gO.py, goGpt, line 42 :)'
    finally:
        return retrn
########################### FETCH JSON ###########################
def fetchJSON(url):
    headers = {
	        "Accept": "text/html",
	        "User-Agent": "Chrome"
	    }
    r = requests.get(url, headers=headers)
    if(r.status_code != 200):
        return('https://http.cat/' + r.status_code + '.jpg')
    return r.json()

#################### RUN IF IN STANALONE MODE ####################
if(__name__ == "__main__"):
    #print(goReddit("hentai"))
    #print(goGpt('Kill me'))
    print(bibbliaPol())
##################################################################