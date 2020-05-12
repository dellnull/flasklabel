#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
import sys

try:
    label = Image.open("submarine.png")

except:
    print("Unable to load image")
    sys.exit(1)
    
drawheader = ImageDraw.Draw(label)
text = "Flask-Soda"

font = ImageFont.truetype("Hack-Regular.ttf", size=60)

drawheader.text((270, 10), text, font=font, fill=(255,120,100,255))

drawfooter = ImageDraw.Draw(label)
text = "Pwn Sauce"

font = ImageFont.truetype("Hack-Regular.ttf", size=30)

drawfooter.text((370, 460), text, font=font)
 
label.save('MySodaLabel.png')