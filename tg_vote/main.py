import telebot
from telebot import types
import os

from config import \
    PREF_TOPICS_ANSWERS, \
    Q_SELECT_PREF, \
    Q_SELECT_YEAR, \
    DEPARTMENT_NAMES, \
    YEAR_NAMES, \
    Q_SELECT_DEP
from functions import \
    get_keyboard_pref, \
    get_proof_pref_text, \
    log, \
    get_keyboard_proof_pref, \
    get_keyboard_deps, \
    get_keyboard_years

# TG_TOKEN = os.environ.get('TG_TOKEN', '')
TG_TOKEN = "7903066824:AAEMHyOeP9jOAq4sa8hLP-CINg8iNnGVYhk"
bot = telebot.TeleBot(TG_TOKEN)

name = ''
surname = ''
department_name = ""
year_name = ""
age = 0
flag = 0
is_in = 0

dict_users = {
    "kristal.as@phystech.edu": "Кристаль Александр \nБ02-003 ЛФИ",
    "reymove.ar@phystech.edu": "321"
}

PREF_ARRAY = {}


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start_voting':

        keyboard = types.InlineKeyboardMarkup()

        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes_reg')
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no_reg')

        keyboard.add(key_yes)
        keyboard.add(key_no)

        question = "Хочешь зарегистрироваться в боте?"
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, 'Напиши /start_voting для участия в опросах')


def get_email(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id,
                     "Напиши почту в формате: \n <strong style='color: white'>ivanov.ii@phystech.edu?</strong>",
                     parse_mode='HTML')
    bot.register_next_step_handler(message, proof_email)


def proof_email(message):
    global surname, dict_users, is_in
    email = message.text
    print(email)

    if email in dict_users.keys():
        is_in = 1
        question = 'Тебе , тебя зовут ' + dict_users[email] + '?'
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes_is_in')
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no_is_in')
    else:
        is_in = 0
        # bot.send_message(message.from_user.id, "Вы не были найдены в системе. Хотите указать свой курс и Физтех-школу?")

        question = "Хотите зарегистрироваться или продолжить без регистрации?"
        key_yes = types.InlineKeyboardButton(text='Зарегистрироваться', callback_data='yes_new_reg')
        key_no = types.InlineKeyboardButton(text='Продолжить без регистрации', callback_data='no_new_reg')

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(key_yes)
    keyboard.add(key_no)

    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global PREF_ARRAY, department_name
    if \
            call.data == "yes_is_in" \
            or call.data == "no_reg" \
            or call.data == "no_new_reg" or call.data in YEAR_NAMES.keys():
        if call.data == "yes_is_in":
            log(f"Регистрация пользователя завершена", log_type="i")
            bot.send_message(call.message.chat.id, 'Выши данные есть в системе. Укажите темы, которые вы бы хотели получать в опросах:')
        bot.send_message(call.message.chat.id, Q_SELECT_PREF, reply_markup=get_keyboard_pref(PREF_ARRAY))
    elif call.data == "no_is_in":
        log(f"Неудачная попытка регистрации", log_type="i")
        bot.send_message(call.message.chat.id, 'Зарегистрируйтесь ещё раз')
    elif call.data == "yes_reg":
        log(f"Начало регистрации пользователя", log_type="i")
        bot.send_message(call.message.chat.id, 'Вы начали регистрацию')
        bot.send_message(call.message.chat.id,
                         "Напиши почту в формате: \n <strong>ivanov.ii@phystech.edu?</strong>",
                         parse_mode='HTML')
        bot.register_next_step_handler(call.message, proof_email)
    elif call.data == "yes_new_reg":
        bot.send_message(call.message.chat.id, Q_SELECT_DEP, reply_markup=get_keyboard_deps())
    elif call.data in DEPARTMENT_NAMES.keys():
        department_name = call.data
        bot.send_message(call.message.chat.id, Q_SELECT_YEAR, reply_markup=get_keyboard_years())
    elif call.data == "proof_pref_yes":
        pass
    elif call.data == "proof_pref_no":
        bot.send_message(call.message.chat.id, Q_SELECT_PREF, reply_markup=get_keyboard_pref(PREF_ARRAY))
    elif call.data in PREF_TOPICS_ANSWERS.keys():
        print(call.data)
        if call.data == "select_proof":
            print("Выбор завершён")
            bot.send_message(
                call.message.chat.id,
                f"{get_proof_pref_text(PREF_ARRAY)}",
                reply_markup=get_keyboard_proof_pref())
        else:
            if call.data not in PREF_ARRAY.keys():
                PREF_ARRAY[call.data] = PREF_TOPICS_ANSWERS[call.data]
            else:
                del PREF_ARRAY[call.data]
            bot.edit_message_reply_markup(
                chat_id=call.message.chat.id,
                message_id=call.message.id,
                reply_markup=get_keyboard_pref(PREF_ARRAY))


bot.polling(none_stop=True, interval=0)

