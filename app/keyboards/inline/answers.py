from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



def first_question() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='10-50', callback_data='answer_q1_a')],
        [InlineKeyboardButton(text='50-100', callback_data='answer_q1_b')],
        [InlineKeyboardButton(text='более 100', callback_data='answer_q1_c')],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)

    return keyboard.as_markup()

def second_question() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='1000 руб.', callback_data='answer_q2_a')],
        [InlineKeyboardButton(text='1500 руб.', callback_data='answer_q2_b')],
        [InlineKeyboardButton(text='более 1500 руб.', callback_data='answer_q2_c')],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)

    return keyboard.as_markup()

def third_question() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='Москва', callback_data='answer_q3_a')],
        [InlineKeyboardButton(text='Санкт-Петербург', callback_data='answer_q3_b')],
        [InlineKeyboardButton(text='Другой город РФ', callback_data='answer_q3_c')],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)

    return keyboard.as_markup()