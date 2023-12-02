import bot
import FileConverter

def upload():
    dir = "D:\Movies\Leo (2023) Tamil HQ HDRip - 1080p.mkv"
    FileConverter.split(dir)
    bot.send(dir)

def download():
    file = "Leo (2023) Tamil HQ HDRip - 1080p.mkv"
    bot.down(file)
    FileConverter.join(file)

#upload()
download()