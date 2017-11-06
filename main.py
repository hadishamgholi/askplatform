import telepot
import time
import json
from Private import *
from AskHandler import *

msg_id = None

START = '/start'
keyboard_start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="پرسیدن سوال", callback_data="ask")]])


def pp_json(json_thing, sort=False, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


def on_chat_message(msg):
    global msg_id
    content_type, chat_type, chat_id = telepot.glance(msg)
    pp_json(msg)
    msg_body = msg["text"]
    if msg_body == START:
        bot.sendMessage(chat_id, "چه درخواستی دارید", reply_markup=keyboard_start)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    ask_handler(query_data, from_id, bot)


bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_message,
                  'callback_query': on_callback_query})

print('Listening ...')
while 1:
    time.sleep(10)
