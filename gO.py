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
    print(goReddit("hentai"))
    print(goGpt('Kill me'))
##################################################################