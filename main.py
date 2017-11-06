import telepot
import time
import json
from Private import *


def pp_json(json_thing, sort=False, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    pp_json(msg)
    msg_body = msg["text"]


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')


bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_message,
                  'callback_query': on_callback_query})

print('Listening ...')
while 1:
    time.sleep(10)
