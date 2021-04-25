from filters import middle_wars


async def on_shutdown(dp):
    await bot.close()


def main():
    pass


if __name__ == '__main__':
    print('start')
    print("Бот запущен")

    from aiogram.utils import executor
    from handlers import dp
    from handlers.handler import bot

    dp.middleware.setup(middle_wars.ThrottlingMiddleware())

    executor.start_polling(dp, on_shutdown=on_shutdown)
