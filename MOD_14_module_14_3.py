from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup


from keyboards import *
from texts import *

api = '___'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.reply('Привет! Я бот помогающий твоему здоровью.'
                        '\nВыберите, что Вы хотите сделать:'
                        '\n',reply_markup=start_kb)


@dp.message_handler(text='Рассчитать', state='*')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=menu_kb)


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()



@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    age = int(data.get('age'))
    growth = int(data.get('growth'))
    weight = int(data.get('weight'))
    calories = (10 * weight) + (6.25 * growth) - (5 * age) - 161
    await message.answer(f'Ваша норма калорий: {calories}')
    await state.finish()




@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина-Сан Жеора для расчёта нормы калорий:\n'
                               'Калории = (10 * вес) + (6.25 * рост) - (5 * возраст) - 161')
    await call.answer()




@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open('files/sapod.jpg', 'rb') as img:
        await message.answer_photo(img, f'Название: {sapodila_prod} | Описание: {des_sap} | Цена: {price_sap}')
    with open('files/chompu.jpg', 'rb') as img:
        await message.answer_photo(img, f'Название: {chompu_prod} | Описание: {des_chomp} | Цена: {price_chomp}')
    with open('files/aki.jpg', 'rb') as img:
        await message.answer_photo(img, f'Название: {aki_prod} | Описание: {des_aki} | Цена: {price_aki}')
    with open('files/amba.jpg', 'rb') as img:
        await message.answer_photo(img, f'Название: {ambarela_prod} | Описание: {des_amba} | Цена: {price_amba}')

    await message.answer(text='Выберите продукт для покупки:', reply_markup=product_kb)



@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(text='Вы успешно приобрели продукт!')
    await call.answer()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
