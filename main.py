import logging
from register_bot import bot, dp
from aiogram import executor

from handlers import situation_callbacks, common_handlers, consultation_callbacks, menu_callbacks, signup_fsm_block


logging.basicConfig(level=logging.INFO)


common_handlers.register_common_handlers(dp)
menu_callbacks.register_menu_callbacks(dp)
situation_callbacks.register_callbacks_situation(dp)
consultation_callbacks.register_consultation_callbacks(dp)
signup_fsm_block.register_signup_fsm_block(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
