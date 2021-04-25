START_TEXT = ' Добро пожаловать в бота! '


def get_reg_text(chat_id, username):
    result = f'Сообщите менеджеру @Mutter0815  ваш chat_id: {chat_id} \nи ваш username: {username}'
    return result


text_for_buttons = {'button_1': 'Мои задачи💼',
                    'button_2': "Визитка🧑🏻‍💻",
                    'button_3': 'Тестирование📚',
                    'button_4': 'Трудовой распорядок📝',
                    'button_5': "Техно. инструкции🗃",
                    'button_6': "Корп. документы📚",
                    'button_7': "Чат📨",
                    'button_8': "Помощь🤓"}

text_for_button_1 = {'button_1': "Ознакомиться с Корп. документами",
                     'button_2': "Посмотреть визитку",
                     'button_3': "Ознакомиться с Тех. инструкциями",
                     'button_4': "Трудовой распорядок",
                     'button_5': "Пройти тестирование❗️",
                     'button_6': "↪️Назад↩️"}

callback_for_b1_b1 = 'Первым шагом для успешной адаптации сотрудника является ознакомление с корпоративными ' \
                     'документами. Вот файлы, с которыми тебе необходимо ознакомиться, чтобы продолжить'

callback_for_b1_b2 = 'Теперь нам необходимо ввести тебя в курс дела. Посмотри нашу видео-визитку:\n youtube.com/watch?v=qgYstix7740'

callback_for_b1_b5 = 'Отлично! Теперь самое время ознакомиться с технологически ми инструкциями'

callback_for_b1_b3 = 'Проверим что ты смог узнать?Желаю удачи я верю,у тебя получится!😎'

callback_support = 'Трудовой коллектив - важная часть жизни сотрудника👩🏻‍🏫👨🏼‍🏫.' \
                   'Он устанавливает внутригрупповые нормы, ценности, устанавливает определённую культуру.\n' \
                   'Здесь ты можешь вступить в чат и познакомиться со своими коллегами.' \
                   'Расскажи им о себе, так ты сможешь быстрее влиться в наш коллектив. Удачи!\nt.me/joinchat/UC5bWZLdIDFlMDEy'

callback_help = "Если у тебя есть какие-либо вопросы,то ты можешь обращаться сюда:\n " \
                'Telegram:@mutter0815\n' \
                'Email: mutter8525@yandex.ru'
callback_for_b2_b6 = 'Вы вернулись к исходному меню'
callback_for_b1_b4 = 'Далее тебе понадобиться твоё рабочее расписание. Его ты сможешь найти здесь:'

callback_for_b2_b1 = callback_for_b1_b1
callback_for_b2_b2 = callback_for_b1_b2
callback_for_b2_b3 = callback_for_b1_b5
callback_for_b2_b4 = callback_for_b1_b4
callback_for_b2_b5 = callback_for_b1_b3

win_test = 'Поздравляем! Вы полностью прошли процесс адаптации,удачи в дальнейшей работе!'
lose_test = 'К сожалению тест не пройден,попробуй ознакомиться с документацией еще раз и возвращайся 😊'
