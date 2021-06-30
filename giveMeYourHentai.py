import download_image_to_local_machine as download
import time
from timeloop import Timeloop
from datetime import timedelta
import requests
import json

link = "nie"

def gohentai(whe):
    #sub = "hentai"
    url = "https://www.reddit.com/r/hentai.json"
    y = fetchJSON(url)
    try:
        link = y["data"]["children"][whe]["data"]["url_overridden_by_dest"]
        return(link)
    except:
        #link = y["data"]["children"][hen+2]["data"]["url_overridden_by_dest"]
        print("i dont fookin know")
        return 0
        

def fetchJSON(url):
    headers = {
	        "Accept": "text/html",
	        "User-Agent": "Chrome"
	    }
    r = requests.get(url, headers=headers)
    if(r.status_code != 200):
        return('https://http.cat/' + r.status_code + '.jpg')
    return r.json()

###################################################################################
for whe in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]:
        download.download(gohentai(int(whe)))
        print("bu bu, hentai downloded")
###################################################################################

tl = Timeloop()

@tl.job(interval=timedelta(minutes=5))
def dodo():
    for whe in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]:
        download.download(gohentai(int(whe)))
        print("bu bu, hentai downloded")

if __name__ == "__main__":
    tl.start(block=True)

def start():
    tl.start(block=True)