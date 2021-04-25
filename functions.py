import os
import sqlite3


def get_list_with_files_from_directory(directory):
    new_path = os.getcwd()
    print(new_path)
    print(directory)
    names = os.listdir(directory)
    print(names)
    list_with_files = []

    for name in names:
        with open(os.path.join(directory, name), mode='rb') as file:
            yield file


def check_chat_id(chat_id):
    conn = sqlite3.connect(os.path.join('sources', 'rosatomdb.sqlite'))
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM workers WHERE telegram_id=:chatId", {"chatId": chat_id})
    results = cursor.fetchone()
    print(results)
    if results:
        conn.close()
        return results[3]
    else:
        conn.close()
        return False


def get_all_answers(index=None):
    conn = sqlite3.connect(os.path.join('sources', 'rosatomdb.sqlite'))
    cursor = conn.cursor()
    cursor.execute("SELECT var1, var2, var3, var4 FROM doctest")

    list_with_answers = []

    result = cursor.fetchall()
    for question in result:
        for i in range(3):
            list_with_answers.append(question[i])

    return list_with_answers


def get_main_questions(index: int, index_2=None, doptest=None):
    conn = sqlite3.connect(os.path.join('sources', 'rosatomdb.sqlite'))
    cursor = conn.cursor()

    list_with_dicts = []

    if not doptest:
        cursor.execute("SELECT questions, var1, var2, var3, var4, true FROM doctest WHERE quest_id=:id", {"id": index})
    else:
        cursor.execute("SELECT questions, var1, var2, var3, var4, true FROM doptest WHERE quest_id=:id", {"id": index})

    result = cursor.fetchall()

    for question in result:
        quest_dict = {
            'question': question[0],
            'var_1': question[1],
            'var_2': question[2],
            'var_3': question[3],
            'var_4': question[4],
            'true': question[5]
        }
        list_with_dicts.append(quest_dict)

    print(list_with_dicts)

    if index_2 is not None:
        return list_with_dicts[index_2]

    else:
        return list_with_dicts


def save_result_in_db(chat_id, result):
    conn = sqlite3.connect(os.path.join('sources', 'rosatomdb.sqlite'))
    cursor = conn.cursor()
    cursor.execute(f"UPDATE workers SET testresult = {result} WHERE telegram_id ={result}")
    conn.commit()


