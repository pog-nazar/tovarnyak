from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from keyboards import keyboard

from data.parser.content_parsing import get_info
from tools import db_control_tool
from tools import connector
from tools import is_url

from datetime import datetime, date

import logging


# data
media = None


logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

bot = Bot("YOUR BOT TOKEN")
dp = Dispatcher(bot,
                storage=storage)


class ClientStatesGroup(StatesGroup):
    create_post = State()
    send_post = State()
    set_time = State()


@dp.message_handler(commands=["start"])
async def start_action(message: types.Message):
    await message.answer("Привіт!!!", reply_markup=keyboard.main_menu)


@dp.message_handler(state=None)
async def create_post(message: types.Message):
    if message.text == "СТВОРИТИ ПОСТ📄":
        await ClientStatesGroup.create_post.set()
        await message.answer("Відправ мені посилання.", reply_markup=keyboard.wait_for_link)


@dp.message_handler(commands=["cancel"])
async def cancel_action(message: types.Message):
    await message.answer("Ви и так знаходитеся в головному меню.")


@dp.message_handler(state=ClientStatesGroup.create_post)
async def create_post(message: types.Message, state: FSMContext):
    if message.text == "ВІДМІНИТИ❌":
        await message.answer("Дія була відмінена. Ви зараз в головному меню.", reply_markup=keyboard.main_menu)
        await state.finish()

    elif is_url.is_url(message.text):
        global media

        photo_urls, short_description, description, specifications, price = get_info(message.text)

        description = connector.connect(short_description, description, specifications, price)

        media = list()

        for url in photo_urls:
            if not media:
                media.append(types.InputMediaPhoto(url, caption=description, parse_mode="html"))
            else:
                media.append(types.InputMediaPhoto(url))

        await bot.send_media_group(message.chat.id, media=media)
        await message.answer("Вам подобається?", reply_markup=keyboard.post_confirmation)
        await ClientStatesGroup.next()

    else:
        await message.answer("Відправте мені посилання.")


@dp.message_handler(state=ClientStatesGroup.send_post)
async def send_post(message: types.Message, state: FSMContext):
    if message.text == "ВІДМІНИТИ❌":
        await message.answer("Дія була відмінена. Ви зараз в головному меню.", reply_markup=keyboard.main_menu)
        await state.finish()

    elif message.text == "ВІДПАВИТИ✅":
        await bot.send_media_group("-1002167796888", media=media)
        await message.answer("Пост був успішно відправлений.", reply_markup=keyboard.main_menu)
        await state.finish()

    elif message.text == "/set_time":
        await message.answer(f"Сьогоднішня дата {date.today().strftime('%d.%m.%Y')}")
        await message.answer("Відправте мені дату в одному з цих форматів: дд.мм гг:хх/дд гг:мм/гг:мм")

        await ClientStatesGroup.next()


@dp.message_handler(state=ClientStatesGroup.set_time)
async def set_time(message: types.Message, state: FSMContext):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
