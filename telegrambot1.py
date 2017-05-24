import time
import telepot
import sys

file = open(sys.argv[1], "r")
token = str(file.read())
file.close()

bot = telepot.Bot(token)
print(bot.getMe())
print("************************")
print("Messages start from here")
print("************************")
update_id = 0

while 1:
    response = bot.getUpdates(update_id+1)
    n_messages = len(response)
    if n_messages > 0:
        message = response[-1]["message"]
        update_id = response[-1]["update_id"]
        print(str(update_id) + ": " + message["text"] + "; Messages: " + str(n_messages))
    time.sleep(5)
