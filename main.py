from instabot import Bot
from config import Config
import os
import schedule
def Uploading():
    bot = Bot()
    image_path = (os.getcwd()+ '/images/')
    images = os.listdir(Config.IMAGE_FOLDER_PATH)
    nextImage = image_path + images[0]
    nextCaption = Config.CAPTION_LIST[0]
    bot.login(username=Config.USERNAME,password=Config.PASSWORD)
    bot.upload_photo(nextImage,caption=nextCaption)
    print("uploaded")
    os.remove(nextImage)
    Config.CAPTION_LIST.pop(0)
schedule.every().day.at("11:00").do(Uploading)
while True:
    schedule.run_pending()