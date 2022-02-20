from PIL import Image, ImageFont, ImageDraw 

def makeImage(lasagnias):
    filename = "garfel-profile-pic/I-ate.png"
    my_image = Image.open(filename)

    title_font = ImageFont.truetype('comicsans/COMIC.ttf', 140)

    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((440,30), str(lasagnias), (255, 8, 255), font=title_font)

    my_image.save("garfel-profile-pic/I-ate-made.png")

#makeImage(99)