import bot
import FileConverter

def upload():
    dir = "D:\Other Things\PyCharm Crack.zip"
    FileConverter.split(dir)
    bot.send(dir)

def download():
    file = "Leo (2023) Tamil HQ HDRip - 1080p.mkv"
    bot.down(file)
    FileConverter.join(file)

def delete():
    file = "Leo (2023) Tamil HQ HDRip - 1080p.mkv"
    bot.dele(file)

#upload()
#download()
#delete()