from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from message_text import text_for_buttons, text_for_button_1

empty_keyboard = ReplyKeyboardMarkup(
    keyboard=[],
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=text_for_buttons['button_1']),
         KeyboardButton(text=text_for_buttons['button_2'])],

        [KeyboardButton(text=text_for_buttons['button_3']),
         KeyboardButton(text=text_for_buttons['button_4'])],

        [KeyboardButton(text=text_for_buttons['button_5']),
         KeyboardButton(text=text_for_buttons['button_6'])],

        [KeyboardButton(text=text_for_buttons['button_7']),
         KeyboardButton(text=text_for_buttons['button_8'])]
    ],
    resize_keyboard=True
)

menu_button_1 = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text=text_for_button_1['button_1']),
             KeyboardButton(text=text_for_button_1['button_2'])],

            [KeyboardButton(text=text_for_button_1['button_3']),
             KeyboardButton(text=text_for_button_1['button_4'])],

            [KeyboardButton(text=text_for_button_1['button_5']),
             KeyboardButton(text=text_for_button_1['button_6'])]

        ], resize_keyboard=True

)


def get_main_question_menu(dict_question):

    var_1 = dict_question['var_1']
    var_2 = dict_question['var_2']
    var_3 = dict_question['var_3']
    var_4 = dict_question['var_4']

    main_question_menu = ReplyKeyboardMarkup(
        keyboard=[
                [KeyboardButton(text=var_1, callback_data=var_1),
                 KeyboardButton(text=var_2, callback_data=var_2)],

                [KeyboardButton(text=var_3, callback_data=var_3),
                 KeyboardButton(text=var_4, callback_data=var_4)],
            ]
    )
    return main_question_menu
