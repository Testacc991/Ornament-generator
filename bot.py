from PIL import Image, ImageDraw, ImageFont
from patterns import allshapes
import random
from mastodon import Mastodon
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

podurl = 'https://site.com'

textmessage = '#simple #abstract #random'

access_token = ""

visibility = "unlisted"
#Export to mastodon
mastodon = Mastodon(
    access_token = access_token,
    api_base_url = podurl 
)


cellsize = 10

def getcoord(x,y):
    x1 = x
    y1 = y
    x2 = x+cellsize
    y2 = y+cellsize
    return [x1,y1,x2,y2]

def drawshape(oneshape, offsetx,offsety):
    shapesize = oneshape.shape
    w = shapesize[0]
    h = shapesize[1]
    for i in range(w):
        for v in range(h):
            if(oneshape[i][v] == 1):
                t = getcoord(v*cellsize+offsetx,i*cellsize+offsety)
                d.rectangle(t,fill=(255,0,0),outline=None,width=0)   
# create an image
imageW = 400

imageH = 400

out = Image.new("RGB", (imageW, imageH), (255, 255, 255))

d = ImageDraw.Draw(out)

elements = random.randint(20,100)

for i in range(10,elements):
    randShapeIndex = random.randint(0,len(allshapes)-1)
    coordx = random.randint(0,40)
    coordy = random.randint(0,40)
    coordx = coordx*10
    coordy = coordy*10
    t = getcoord(coordx,coordy)
    drawshape(allshapes[randShapeIndex],coordx,coordy)
# Export to folder    
#out.show()
# Export to Mastodon
output_filename = rf'{ROOT_DIR}\output.png'
out.save(output_filename)

media_dict = mastodon.media_post(output_filename)
media_ids = [media_dict['id']]
mastodon.status_post(status=textmessage, media_ids=media_ids, visibility=visibility)
os.remove(output_filename)
