import requests
import os


def download(url):
    path = "img/"
    response = requests.get(url)

    filename = url.split('/')[3]

    fullfilename = path + filename
    if os.path.isfile(fullfilename) == True:
        print("jest jusz owo")
        return 1
    else:

        file = open(fullfilename, "wb")

        file.write(response.content)

        file.close()

if(__name__ == "__main__"):
    print("starting to download")
    download("https://i.imgur.com/ExdKOOz.png")
    print("DONE!!! i guess")