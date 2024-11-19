from telebot import types
from config import \
    PREF_TOPICS_ANSWERS, \
    DEPARTMENT_NAMES, \
    YEAR_NAMES
import logging
import datetime


def log(string, log_type="w"):
    _ = f"{str(datetime.datetime.now())[:-7]} {string}"
    if log_type == "d":
        logging.debug(_)
    elif log_type == "i":
        logging.info(_)
    elif log_type == "w":
        logging.warning(_)
    elif log_type == "e":
        logging.error(_)
    elif log_type == "c":
        logging.critical(_)
    else:
        logging.debug(_)


def get_keyboard_pref(PREF_ARRAY):
    markup = types.InlineKeyboardMarkup()
    for answer in PREF_TOPICS_ANSWERS.keys():
        text = ""
        if answer in PREF_ARRAY.keys():
            text = " ✅"
        button = types.InlineKeyboardButton(
            text=PREF_TOPICS_ANSWERS[answer] + text,
            callback_data=answer)
        markup.add(button)
    return markup


def get_keyboard(data=None):
    markup = types.InlineKeyboardMarkup()
    if data is None:
        data = {"yes": "Да", "no": "Нет"}
    for keyboard_button in data.keys():
        button_yes = types.InlineKeyboardButton(
            text=data[keyboard_button],
            callback_data=keyboard_button)
        markup.add(button_yes)
    return markup


def get_keyboard_proof_pref():
    data = {
        "proof_pref_yes": "Подтвердить",
        "proof_pref_no": "Отметить ещё"
    }
    return get_keyboard(data)


def get_keyboard_deps():
    data = DEPARTMENT_NAMES
    return get_keyboard(data)


def get_keyboard_years():
    data = YEAR_NAMES
    return get_keyboard(data)


def get_proof_pref_text(PREF_ARRAY):
    res = f"Подтвердите ваши предпочтения:"
    for pref in PREF_ARRAY.keys():
        res += f"\n - {PREF_ARRAY[pref]}"
    res += f"\n* все опросы на эти темы будут приходить в этот чат"
    return res
