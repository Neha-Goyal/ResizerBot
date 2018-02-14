import math
import os
from PIL import Image
from telegram.ext import Updater

def photo_resize(bot,update,width,height):
    img=Image.open("document.jpg")
    h=math.floor(0.65*height)
    w=math.floor(0.65*width)    
    img=img.resize((w,h),Image.ANTIALIAS)
    img.save("document.jpg",optimize=True,quality=95)
    bot.send_photo(chat_id=update.message.chat_id,photo=open("document.jpg",'rb'))
    os.remove("document.jpg")

def doc_resize(bot,update,ext):
    doc=Image.open("document."+ext)
    (w,h)=doc.size
    h=math.floor(0.65*h)
    w=math.floor(0.65*w)    
    doc=doc.resize((w,h),Image.ANTIALIAS)
    doc.save("document."+ext,optimize=True,quality=95)
    bot.send_document(chat_id=update.message.chat_id,document=open("document."+ext,'rb'))
    os.remove("document."+ext)
