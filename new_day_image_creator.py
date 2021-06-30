from PIL import Image, ImageFont, ImageDraw 
from datetime import datetime

def doTime():
    filename = "newday-1.png"
    my_image = Image.open(filename)

    title_font = ImageFont.truetype('Roboto/Roboto-Thin.ttf', 140)
    ##title_font2 = ImageFont.truetype('Roboto/Roboto-Regular.ttf', 90)


    now = datetime.now()
    month = now.strftime("%d %b")
    hour = now.strftime("%H:%M")

    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((700,40), month, (255, 235, 77), font=title_font)
    image_editable.text((100,400), hour, (255, 235, 77), font=title_font)

    my_image.save("time.png")

