#pip install pillow
#pip install qrcode

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
from datetime import datetime
import qrcode
import os
import json

#global
NameLen = 13
#functions
def getCurrentTime():
    today = datetime.today()
    year = today.year
    day = today.day
    month = today.month
    time = ""+str(day)+'/'+str(month)+'/'+str(year)+'  '
    time +=  str(datetime.now().strftime("%I:%M %p"))
    return time

def validatename(name):
    global NameLen
    if(len(name) > NameLen):
        name = name.split(' ')[0]
    return name

import os
def genrateId(vId,vName,vPerpose, vCollege):
    # #inputs 
    vName = str(vName)
    vId = str(vId)
    vPerpose = str(vPerpose)
    vTime = getCurrentTime()
    vCollege = str(vCollege)
    #bacode genrater
    content = { 'id' : vId , 'name' : vName , 'perpose' : vPerpose , 'collage' : vCollege }
    string = json.dumps(content)
    bar_img = qrcode.make(string)
    bar_img = bar_img.resize((330,330))
    #crop image
    
    # dirpath = os.getcwd()
    # print("current directory is : " + dirpath)


     #fill the details ...
    back_img = Image.open("vm/Extra_Tools/access.png")
    draw = ImageDraw.Draw(back_img)
    #name
    vaildName = validatename(vName) 
    #validate the name to 13 to 14 char.
    name_fnt = ImageFont.truetype("arial.ttf", 60)
    draw.text((370,150), vaildName.upper() , font=name_fnt , fill = (0,0,0,1))
    #id
    name_fnt = ImageFont.truetype("arial.ttf", 40)
    draw.text((870,230), vId , font=name_fnt , fill = (0,0,0,1))
    #purpose
    name_fnt = ImageFont.truetype("arial.ttf", 30)
    draw.text((350,380), vPerpose , font=name_fnt , fill = (0,0,0,1))
    #time
    name_fnt = ImageFont.truetype("arial.ttf", 30)
    draw.text((350,450), vTime , font=name_fnt , fill = (0,0,0,1))
    #college
    name_fnt = ImageFont.truetype("arial.ttf", 30)
    draw.text((350,510), vCollege , font=name_fnt , fill = (0,0,0,1))
    #marge image..
    final = Image.new('RGBA',(1150,660))
    #back
    final.paste(back_img,(0,0))
    #dp
    
    dp = Image.open("media/ids/display_pic/"+vId+'.png')
    dp = dp.resize((280,280))
    
    #     # Open the input image as numpy array, convert to RGB
    # img=Image.open("media/ids/display_pic/"+vId+'.png').convert("RGB")
    # npImage=np.array(img)
    # h,w=280,280

    # # Create same size alpha layer with circle
    # alpha = Image.new('L', img.size)
    # draw = ImageDraw.Draw(alpha)
    # draw.pieslice([0,0,h,w],0,360,fill=255)

    # # Convert alpha Image to numpy array
    # npAlpha = np.array(alpha)

    # # Add alpha layer to RGB
    # npImage = np.dstack((npAlpha,npImage))

    # # Save with alpha
    # dp = Image.fromarray(npImage)
    # im_square = crop_max_square(dp).resize((280, 280), Image.LANCZOS)
    # dp = mask_circle_transparent(im_square, 2)

    old_im = Image.open("media/ids/display_pic/"+vId+'.png').resize((280,280))
    old_size = old_im.size
    new_size = (286, 286)
    new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
    new_im.paste(old_im,(3,3))
    dp = new_im
    
    final.paste(dp, (70,60))
    #barcode #1070 #580,
    final.paste(bar_img, (745,270))
    # final.show() # show te image ....................
    #save to ids/1.png

    filename = 'media/ids/'+vId + '.png';
    final.save(filename)


# def crop_max_square(pil_img):
#     return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

# def mask_circle_transparent(pil_img, blur_radius, offset=0):
#     offset = blur_radius * 2 + offset
#     mask = Image.new("L", pil_img.size, 0)
#     draw = ImageDraw.Draw(mask)
#     draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
#     mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
#     result = pil_img.copy()
#     result.putalpha(mask)
#     return result

# def crop_center(pil_img, crop_width, crop_height):
#     img_width, img_height = pil_img.size
#     return pil_img.crop(((img_width - crop_width) // 2,
#                          (img_height - crop_height) // 2,
#                          (img_width + crop_width) // 2,
#                          (img_height + crop_height) // 2))




if __name__ == '__main__':
    genrateId('0074','kevin thoriya','meeting','pit')