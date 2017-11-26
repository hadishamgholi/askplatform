import telepot
import time
from Utils import *
from Private import *
import AskHandler
from model import *

msg_id = None


def on_chat_message(msg):
    global msg_id
    content_type, chat_type, chat_id = telepot.glance(msg)
    pp_json(msg)
    msg_body = msg["text"]

    AskHandler.msg_controller(msg_body, chat_id, bot)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    AskHandler.callback_controller(query_data, from_id, bot)


bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_message,
                  'callback_query': on_callback_query})

print('Listening ...')
while 1:
    time.sleep(10)
