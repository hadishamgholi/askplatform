from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

a1 = "پرسش شما پیرامون کدام موضوع است؟"


def ask_handler(text, chat_id, bot):
    msg_id = bot.sendMessage(chat_id, a1, reply_markup=keyboard1)


def subject_controller(text, chat_id, bot):
    if text == ahkam.name:
        bot.sendMessage(chat_id, ahkam.response_text)
    elif text == moshavereh.name:
        bot.sendMessage(chat_id, moshavereh.response_text)
    elif text == eteghdi.name:
        bot.sendMessage(chat_id, eteghdi.response_text)


class Subject:
    def __init__(self, name, response_text):
        self.name = name
        self.response_text = response_text


ahkam = Subject("احکام", "پرسش شرعی خود را وارد کنید")
moshavereh = Subject("مشاوره", "متن خود را وارد کنید تا مشاوران ما در سریعترین زمان پاسخ دهند")
eteghdi = Subject("اعتقادی", "پرسش اعتقادی خود را وارد کنید")

keyboard1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=ahkam.name, callback_data=ahkam.name)],
    [InlineKeyboardButton(text=moshavereh.name, callback_data=moshavereh.name)],
    [InlineKeyboardButton(text=eteghdi.name, callback_data=eteghdi.name)]])
