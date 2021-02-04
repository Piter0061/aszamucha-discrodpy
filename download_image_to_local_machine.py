import requests

def download(url):
    path = "img/"
    response = requests.get("https://i.imgur.com/ExdKOOz.png")

    filename = url.split('/')[3]

    fullfilename = path + filename
    file = open(fullfilename, "wb")

    file.write(response.content)

    file.close()

if(__name__ == "__main__"):
    print("starting to download")
    download("https://i.imgur.com/ExdKOOz.png")
    print("DONE!!! i guess")