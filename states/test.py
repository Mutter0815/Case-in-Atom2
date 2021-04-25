from aiogram.dispatcher.filters.state import StatesGroup, State
from functions import get_main_questions


class Test(StatesGroup):
    question_1_1 = State()
    question_1_2 = State()
    question_1_3 = State()
    question_1_4 = State()

    dop_question_1_1 = State()
    dop_question_1_2 = State()

    question_2_1 = State()
    question_2_2 = State()
    question_2_3 = State()
    question_2_4 = State()

    dop_question_2_1 = State()
    dop_question_2_2 = State()

    question_3_1 = State()
    question_3_2 = State()
    question_3_3 = State()
    question_3_4 = State()
