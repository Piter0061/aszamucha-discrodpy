import requests
import random
from bs4 import BeautifulSoup

def FETCH(img):

    site = 'https://www.google.com/search?q='+ img +'&tbm=isch&ved=2ahUKEwiD0uSA09LuAhVQyCoKHW29DjYQ2-cCegQIABAA&oq=kingus&gs_lcp=CgNpbWcQAzIECCMQJzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIAFCg6wNY-fADYJzyA2gAcAB4AIABYYgB8AOSAQE2mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=Ay0dYMPEGNCQqwHt-rqwAw&bih=966&biw=1903&hl=en'
    
    response = requests.get(site)

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')

    urls = [img['src'] for img in img_tags]

    randoompoost = int(random.random() * (len(urls) - 1))

    #print(len(urls))
    return(urls[randoompoost + 1])

if(__name__ == "__main__"):
    print(FETCH('cock'))