from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from bot_dp import dp, bot
from functions import check_chat_id
import os
from handlers import testing

import keyboards
import message_text
import functions
import sqlite3


@dp.message_handler(Command("start"), state=None)
async def show_menu(message: Message):
    fio = check_chat_id(message.chat.id)
    await message.answer(text=message_text.START_TEXT + str(fio), reply_markup=keyboards.menu)


@dp.message_handler(Command("stop_test"), state=None)
async def stop_test(message: Message, state: FSMContext):
    await state.finish()


# FIRST_MENU_HANDLER
@dp.message_handler(Text(equals=(message_text.text_for_buttons.values())))
async def send_menu(message: Message):
    # BUTTON_1
    if message.text == message_text.text_for_buttons['button_1']:
        await message.answer(text=message.text,
                             reply_markup=keyboards.menu_button_1)

    # BUTTON_2
    elif message.text == message_text.text_for_buttons['button_2']:
        await message.answer(text=message_text.callback_for_b1_b2)

    # BUTTON_3
    elif message.text == message_text.text_for_buttons['button_3']:
        await message.answer(text=message_text.callback_for_b1_b3)
        await testing.start_test(message)


    # BUTTON_4
    elif message.text == message_text.text_for_buttons['button_4']:
        await message.answer(text=message_text.callback_for_b1_b4)

        path_ = os.path.join(os.getcwd(), './sources', 'sources_1_4')
        file_generator = functions.get_list_with_files_from_directory(path_)

        while True:
            try:
                file = next(file_generator)
                await bot.send_document(chat_id=message.from_user.id,
                                        document=file)

            except StopIteration:
                break

    # BUTTON_5
    elif message.text == message_text.text_for_buttons['button_5']:
        await message.answer(text=message_text.callback_for_b1_b5)

        path_ = os.path.join(os.getcwd(), './sources', 'sources_1_5')
        file_generator = functions.get_list_with_files_from_directory(path_)

        while True:
            try:
                file = next(file_generator)
                await bot.send_document(chat_id=message.from_user.id,
                                        document=file)

            except StopIteration:
                break

    # BUTTON_6
    elif message.text == message_text.text_for_buttons['button_6']:
        await message.answer(text=message_text.callback_for_b1_b1)
        path_ = os.path.join(os.getcwd(), './sources', 'sources_2_1')
        file_generator = functions.get_list_with_files_from_directory(path_)

        while True:
            try:
                file = next(file_generator)
                await bot.send_document(chat_id=message.from_user.id,
                                        document=file)

            except StopIteration:
                break
    # BUTTON_7
    elif message.text == message_text.text_for_buttons['button_7']:
        await message.answer(text=message_text.callback_support)

    # BUTTON_8
    elif message.text == message_text.text_for_buttons['button_8']:
        await message.answer(text=message_text.callback_help)


# SECOND_MENU_HANDLER
@dp.message_handler(Text(equals=(message_text.text_for_button_1.values())))
async def send_menu(message: Message):
    # BUTTON_1
    if message.text == message_text.text_for_button_1['button_1']:

        await message.answer(text=message_text.callback_for_b2_b1,
                             reply_markup=keyboards.menu)

        path_ = os.path.join(os.getcwd(), './sources', 'sources_2_1')
        file_generator = functions.get_list_with_files_from_directory(path_)

        while True:
            try:
                file = next(file_generator)
                await bot.send_document(chat_id=message.from_user.id,
                                        document=file)

            except StopIteration:
                break

    # BUTTON_2
    elif message.text == message_text.text_for_button_1['button_2']:
        await message.answer(text=message_text.callback_for_b2_b2)

    # BUTTON_3
    elif message.text == message_text.text_for_button_1['button_3']:
        await message.answer(text=message_text.callback_for_b2_b3)

    # BUTTON_4
    elif message.text == message_text.text_for_button_1['button_4']:
        await message.answer(text=message_text.callback_for_b2_b4)

    # BUTTON_5
    elif message.text == message_text.text_for_button_1['button_5']:
        await message.answer(text=message_text.callback_for_b2_b5)
        await testing.start_test(message)

    # BUTTON_6
    elif message.text == message_text.text_for_button_1['button_6']:
        await message.answer(text=message_text.callback_for_b2_b6,
                             reply_markup=keyboards.menu)


async def send_info_for_no_name(message: Message):
    await message.answer(text=message_text.get_reg_text(chat_id=message.from_user.id,
                                                        username=message.from_user.username))


def select_questions():
    conn = sqlite3.connect('sources/rosatomdb.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctest")
    results = cursor.fetchall()
    print(results)
    conn.close()
