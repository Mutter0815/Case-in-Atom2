from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from states.test import Test

from bot_dp import dp, bot
import functions
from keyboards import get_main_question_menu, menu
import message_text


async def start_test(message: Message):
    dict_question = functions.get_main_questions(index=1)[0]
    keyboard = get_main_question_menu(dict_question=dict_question)

    await message.answer(text=dict_question['question'],
                         reply_markup=keyboard)

    await Test.question_1_1.set()


@dp.message_handler(state=Test.question_1_1)
async def answer_q1_1(message: types.Message, state: FSMContext):
    answer = message.text

    dict_question_old = functions.get_main_questions(index=1, index_2=0)
    print(dict_question_old)
    if answer == dict_question_old['true']:
        await state.update_data(answer1_1=True)
    else:
        await state.update_data(answer1_1=False)

    dict_question = functions.get_main_questions(index=1, index_2=1)
    keyboard = get_main_question_menu(dict_question=dict_question)

    await message.answer(text=dict_question['question'], reply_markup=keyboard)

    await Test.question_1_2.set()


@dp.message_handler(state=Test.question_1_2)
async def answer_q1_2(message: types.Message, state: FSMContext):
    answer = message.text

    dict_question_old = functions.get_main_questions(index=1, index_2=1)
    if answer == dict_question_old['true']:
        await state.update_data(answer1_2=True)
    else:
        await state.update_data(answer1_2=False)

    dict_question = functions.get_main_questions(index=1, index_2=2)
    keyboard = get_main_question_menu(dict_question=dict_question)

    await message.answer(text=dict_question['question'], reply_markup=keyboard)

    await Test.question_1_3.set()


@dp.message_handler(state=Test.question_1_3)
async def answer_q1_3(message: types.Message, state: FSMContext):
    answer = message.text

    dict_question_old = functions.get_main_questions(index=1, index_2=2)
    if answer == dict_question_old['true']:
        await state.update_data(answer1_3=True)
    else:
        await state.update_data(answer1_3=False)

    dict_question = functions.get_main_questions(index=1, index_2=3)
    keyboard = get_main_question_menu(dict_question=dict_question)

    await message.answer(text=dict_question['question'], reply_markup=keyboard)

    await Test.question_1_4.set()


@dp.message_handler(state=Test.question_1_4)
async def answer_q1_4(message: types.Message, state: FSMContext):
    answer = message.text

    dict_question_old = functions.get_main_questions(index=1, index_2=3)
    if answer == dict_question_old['true']:
        await state.update_data(answer1_4=True)
    else:
        await state.update_data(answer1_4=False)

    data = await state.get_data()
    result = 0

    for pre_result in data.values():
        if pre_result:
            result += 1

    if result > 2:
        dict_question = functions.get_main_questions(index=2, index_2=0)
        keyboard = get_main_question_menu(dict_question=dict_question)

        await message.answer(text=dict_question['question'], reply_markup=keyboard)

        await Test.question_2_1.set()

    else:
        dict_question = functions.get_main_questions(index=1, index_2=0, doptest=True)
        keyboard = get_main_question_menu(dict_question=dict_question)

        await message.answer(text=dict_question['question'], reply_markup=keyboard)

        await Test.dop_question_1_1.set()


@dp.message_handler(state=Test.dop_question_1_1)
async def answer_q1_3(message: types.Message, state: FSMContext):

    dict_question = functions.get_main_questions(index=1, index_2=1, doptest=True)
    keyboard = get_main_question_menu(dict_question=dict_question)

    await message.answer(text=dict_question['question'], reply_markup=keyboard)

    await Test.dop_question_1_2.set()


@dp.message_handler(state=Test.dop_question_1_2)
async def answer_q1_3(message: types.Message, state: FSMContext):

    dict_question = functions.get_main_questions(index=2, index_2=0)
    keyboard = get_main_question_menu(dict_question=dict_question)

    await message.answer(text=dict_question['question'], reply_markup=keyboard)

    await Test.question_2_1.set()


@dp.message_handler(state=Test.question_2_1)
async def answer_q1_1(message: types.Message, state: FSMContext):
    answer = message.text

    dict_question_old = functions.get_main_questions(index=2, index_2=0)
    if answer == dict_question_old['true']:
        await state.update_data(answer2_1=True)
    else:
        await state.update_data(answer2_1=False)

    dict_question = functions.get_main_questions(index=2, index_2=1)
    keyboard = get_main_question_menu(dict_question=dict_question)

    await message.answer(text=dict_question['question'], reply_markup=keyboard)

    await Test.question_2_2.set()


@dp.message_handler(state=Test.question_2_2)
async def answer_q1_1(message: types.Message, state: FSMContext):
    answer = message.text

    dict_question_old = functions.get_main_questions(index=2, index_2=1)
    if answer == dict_question_old['true']:
        await state.update_data(answer2_2=True)
    else:
        await state.update_data(answer2_2=False)

    dict_question = functions.get_main_questions(index=2, index_2=2)
    keyboard = get_main_question_menu(dict_question=dict_question)

    await message.answer(text=dict_question['question'], reply_markup=keyboard)

    await Test.question_2_3.set()


@dp.message_handler(state=Test.question_2_3)
async def answer_q1_1(message: types.Message, state: FSMContext):
    answer = message.text

    dict_question_old = functions.get_main_questions(index=2, index_2=2)
    if answer == dict_question_old['true']:
        await state.update_data(answer2_3=True)
    else:
        await state.update_data(answer2_3=False)

    dict_question = functions.get_main_questions(index=2, index_2=3)
    keyboard = get_main_question_menu(dict_question=dict_question)

    await message.answer(text=dict_question['question'], reply_markup=keyboard)

    await Test.question_2_4.set()


@dp.message_handler(state=Test.question_2_4)
async def answer_q1_1(message: types.Message, state: FSMContext):
    answer = message.text

    dict_question_old = functions.get_main_questions(index=2, index_2=3)
    if answer == dict_question_old['true']:
        await state.update_data(answer2_4=True)
    else:
        await state.update_data(answer2_4=False)

    data = await state.get_data()
    result = 0

    for name in ['answer2_1', 'answer2_2', 'answer2_3', 'answer2_4']:
        if data[name]:
            result += 1

    if result > 2:
        dict_question = functions.get_main_questions(index=3, index_2=0)
        keyboard = get_main_question_menu(dict_question=dict_question)

        await message.answer(text=dict_question['question'], reply_markup=keyboard)

        await Test.question_3_1.set()

    else:
        dict_question = functions.get_main_questions(index=2, index_2=0, doptest=True)
        keyboard = get_main_question_menu(dict_question=dict_question)

        await message.answer(text=dict_question['question'], reply_markup=keyboard)

        await Test.dop_question_2_1.set()


@dp.message_handler(state=Test.dop_question_2_1)
async def answer_q1_3(message: types.Message, state: FSMContext):

    dict_question = functions.get_main_questions(index=2, index_2=1, doptest=True)
    keyboard = get_main_question_menu(dict_question=dict_question)

    await message.answer(text=dict_question['question'], reply_markup=keyboard)

    await Test.dop_question_2_2.set()


@dp.message_handler(state=Test.dop_question_2_2)
async def answer_q1_3(message: types.Message, state: FSMContext):

    dict_question = functions.get_main_questions(index=3, index_2=0)
    keyboard = get_main_question_menu(dict_question=dict_question)

    await message.answer(text=dict_question['question'], reply_markup=keyboard)

    await Test.question_3_1.set()


@dp.message_handler(state=Test.question_3_1)
async def answer_q1_1(message: types.Message, state: FSMContext):
    answer = message.text

    dict_question_old = functions.get_main_questions(index=3, index_2=0)
    if answer == dict_question_old['true']:
        await state.update_data(answer3_1=True)
    else:
        await state.update_data(answer3_1=False)

    dict_question = functions.get_main_questions(index=3, index_2=1)
    keyboard = get_main_question_menu(dict_question=dict_question)

    await message.answer(text=dict_question['question'], reply_markup=keyboard)

    await Test.question_3_2.set()


@dp.message_handler(state=Test.question_3_2)
async def answer_q1_1(message: types.Message, state: FSMContext):
    answer = message.text

    dict_question_old = functions.get_main_questions(index=3, index_2=1)
    if answer == dict_question_old['true']:
        await state.update_data(answer3_2=True)
    else:
        await state.update_data(answer3_2=False)

    dict_question = functions.get_main_questions(index=3, index_2=2)
    keyboard = get_main_question_menu(dict_question=dict_question)

    await message.answer(text=dict_question['question'], reply_markup=keyboard)

    await Test.question_3_3.set()


@dp.message_handler(state=Test.question_3_3)
async def answer_q1_1(message: types.Message, state: FSMContext):
    answer = message.text

    dict_question_old = functions.get_main_questions(index=3, index_2=2)
    if answer == dict_question_old['true']:
        await state.update_data(answer3_3=True)
    else:
        await state.update_data(answer3_3=False)

    dict_question = functions.get_main_questions(index=3, index_2=3)
    keyboard = get_main_question_menu(dict_question=dict_question)

    await message.answer(text=dict_question['question'], reply_markup=keyboard)

    await Test.question_3_4.set()


@dp.message_handler(state=Test.question_3_4)
async def answer_q1_1(message: types.Message, state: FSMContext):
    answer = message.text

    dict_question_old = functions.get_main_questions(index=3, index_2=3)
    if answer == dict_question_old['true']:
        await state.update_data(answer3_4=True)
    else:
        await state.update_data(answer3_4=False)

    data = await state.get_data()
    result = 0

    for pre_result in data.values():
        if pre_result:
            result += 1

    if result > 6:
        functions.save_result_in_db(chat_id=message.from_user.id,
                                    result=result)
        await message.answer(text=message_text.win_test, reply_markup=menu)
        await state.finish()
    else:
        functions.save_result_in_db(chat_id=message.from_user.id,
                                    result=result)
        await message.answer(text=message_text.lose_test, reply_markup=menu)
        await state.finish()









