from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.handler import CancelHandler, current_handler
from handlers.handler import send_info_for_no_name

from functions import check_chat_id


class ThrottlingMiddleware(BaseMiddleware):

    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood_'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: Message, data: dict):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        chat_id = message.from_user.id

        if handler:
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")

        else:
            key = f"{self.prefix}_message"

        if check_chat_id(chat_id):
            await dispatcher.throttle(key)

        else:
            await send_info_for_no_name(message)
            raise CancelHandler()
