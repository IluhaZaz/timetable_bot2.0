import asyncio

import pandas as pd

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config_data.config import Config, load_config


from handlers import user_handlers

from config_data.menu import set_main_menu


# Функция конфигурирования и запуска бота
async def main() -> None:

    # Загружаем конфиг в переменную config
    config: Config = load_config('C:\\Users\\Acer\\Documents\\new_timetable_bot\\.env')

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)

    storage = MemoryStorage()

    dp = Dispatcher(storage=storage)

    dp.include_router(user_handlers.router)

    #настройка меню
    await set_main_menu(bot)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())