import time
import telepot
from telepot.loop import MessageLoop
import sys

file = open(sys.argv[1], "r")
token = str(file.read())
file.close()

bot = telepot.Bot(token)
print(bot.getMe())
print("************************")
print("Messages start from here")
print("************************")

def handle(msg):
    print(msg["text"])

while 1:
    MessageLoop(bot, handle).run_as_thread()
    time.sleep(5)

