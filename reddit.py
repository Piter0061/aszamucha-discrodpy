################################################################
# this is just an api wrapper to fetch requested reddit images #
################################################################
import requests
import json
import random

headers = {
	        "Accept": "text/html",
	        "User-Agent": "Chrome"
	    }

def goReddit(sub):
    randoompoost = int(random.random() * 20)
    url = "http://reddit.com/r/"+ sub +".json"
    r = requests.get(url, headers=headers)
    if(r.status_code != 200):
        return(r.status_code)
    y = r.json()
    try:
        link = y["data"]["children"][randoompoost]["data"]["url_overridden_by_dest"]
    except:
        link = y["data"]["children"][randoompoost+2]["data"]["url_overridden_by_dest"]
    finally:
        return(link)
#################### RUN IF IN STANALONE MODE ####################
if(__name__ == "__main__"):
    print(goReddit("hentai"))
##################################################################