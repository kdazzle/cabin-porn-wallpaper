import os
import random
import cStringIO
import urllib
from ctypes import windll

from win32con import *
import requests
import Image  # From Pil
from bs4 import BeautifulSoup


NUMBER_OF_CABIN_PORN_PAGES = 111
IMAGE_PATH = './cabin_porn.jpg'


def get_random_cabin_porn_image():
    random_page = random.randint(1, NUMBER_OF_CABIN_PORN_PAGES)
    url = 'http://www.cabinporn.com/page/' + str(random_page)
    page = requests.get(url)
    image_url = get_random_image_from_html(page.content)
    image_file = cStringIO.StringIO(urllib.urlopen(image_url).read())
    image = Image.open(image_file)
    image.save(IMAGE_PATH)
    
    return image
    
def get_random_image_from_html(html):
    soup = BeautifulSoup(html)
    photo_divs = soup.find_all('div', class_='photo_div')
    random_div = random.randint(0, len(photo_divs) - 1)
    photo_div = photo_divs[random_div]
    image_div = photo_div.find_all('img')[0]
    return image_div['src']
    

# This function is by AKM licensed under the BSD license
# 
def setWallPaper():
    image = get_random_cabin_porn_image()
    result = windll.user32.SystemParametersInfoA(
        SPI_SETDESKWALLPAPER, 0,
        IMAGE_PATH,
        SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
    )

setWallPaper()
