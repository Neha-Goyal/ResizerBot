from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from PIL import Image
import math
import os

token="515189610:AAHrVWce3diDaw6StmOHN9O7pmnNVwLcH6s"

def start(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text=("Hi %s. Send me jpg/png file, I'll reduce its size!" %update.message.from_user.name))

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

def photoHandler(bot,update):
    file=bot.getFile(update.message.photo[-1].file_id)
    print("file_id: "+str(update.message.photo[-1].file_id))    
    width=update.message.photo[-1].width
    height=update.message.photo[-1].height
    file.download('document.jpg')    
    photo_resize(bot,update,width,height)

def docHandler(bot,update):
    file=bot.getFile(update.message.document.file_id)
    print("file_id: "+str(update.message.document.file_id))    
    ext=str(update.message.document.file_name)[-3:]
    file.download('document.'+ext)  
    doc_resize(bot,update,ext)

def main():
    updater=Updater(token);
    dp=updater.dispatcher

    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(MessageHandler(Filters.document,docHandler))
    dp.add_handler(MessageHandler(Filters.photo,photoHandler))

    updater.start_polling()
    print("================================")
    print("========= Bot Running ==========")
    print("================================")

    updater.idle()

if __name__ == "__main__":
    main()
