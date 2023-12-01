import bot
import os

cwd = os.getcwd()

name = os.listdir(cwd+"\\out")

for i in range(len(name)):
    name[i] = cwd+"\\out\\"+name[i]

if __name__ == '__main__':
    bot.send(name)