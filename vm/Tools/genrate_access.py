#pip install pillow
#pip install qrcode
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import qrcode
import os

#global
NameLen = 13

def getCurrentTime():
    today = datetime.today()
    year = today.year
    day = today.day
    month = today.month
    time = ""+str(day)+'/'+str(month)+'/'+str(year)+'  '
    time +=  str(datetime.now().strftime("%H:%M:%S"))
    return time
#functions
def EgetCurrentTime():
    time = ''
#   time += str(datetime.today())
#    time += ' '
#    time = datetime.now().strftime("%H:%M:%S")
    today = datetime.today()
    if(today.hour > 12):
        hour = int(12 - int(today.hour))
    else:
        hour = today.hour
    minute = today.minute
    month = today.month
    year = today.year
    day = today.day
    hour = str(hour)[1:]
    time = ""+str(day)+'/'+str(month)+'/'+str(year)+'  '+str(hour)+':'+str(minute)
    return time

def validatename(name):
    global NameLen
    if(len(name) > NameLen):
        name = name.split(' ')[0]
    return name

def genrateId():
    #inputs 
    vName = input("enter Visiter's Name  :")
    vId = input("enter the Id  :")
    vPerpose = input("enter perpose  :")
    vTime = getCurrentTime()
    vCollege = input("enter a collage  :")

    #bacode genrater
    string = (vName + " " + vId + " " + vTime)
    bar_img = qrcode.make(string)
    bar_img = bar_img.resize((330,330))
    #crop image


    #fill the details ...
    back_img = Image.open("access.png")
    draw = ImageDraw.Draw(back_img)


    #name
    vaildName = validatename(vName) #validate the name to 13 to 14 char.
    name_fnt = ImageFont.truetype("arial.ttf", 60)
    draw.text((370,150), vaildName.upper() , font=name_fnt , fill = (0,0,0,1))


    #id
    name_fnt = ImageFont.truetype("arial.ttf", 40)
    draw.text((870,230), vId , font=name_fnt , fill = (0,0,0,1))


    #perpose
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

    #barcode #1070 #580
    final.paste(bar_img, (745,270))

    final.show()


    #save to ids/1.png
    filename = '../../media/ids/'+vId + '.png';
    final.save(filename)
    

if __name__ == '__main__':
    genrateId()