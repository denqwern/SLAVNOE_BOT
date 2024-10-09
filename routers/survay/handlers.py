from aiogram.fsm.context import FSMContext
from .states import Survey
import json
import time
import subprocess
import requests
from aiogram import Router, types, F
from aiogram.enums import ChatAction
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import random


from ..Keyboard import key_get_start, admin_key_get_start,  key_get_raspisaniee



router = Router(name=__name__)

API = '239cee0024050686ff009bb45541c0fa'
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"














@router.callback_query(F.data == 'search')
async def search(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Survey.full_name)
    await callback.message.answer(text="Введите название населенного пункта:")


@router.message(Survey.full_name, F.text)
async def full_name(message: types.Message, state: FSMContext):
    city = message.text
    same = get_weather(city)
    await state.update_data(full_name=message.text)
    await message.answer(f"{same}", reply_markup=weather_keyboard_two)

    await state.set_state(Survey.full_name)
    await state.clear()




@router.message(Survey.full_name)
async def full_name(message: types.Message):
    await message.answer(f"SEARCH Некорректный тип введенных данных! Повторите попытку ввода данных: ")




@router.message(Command('weather'))
async def weather(message: types.Message, state: FSMContext):
    city = "славное"
    trn = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric&lang=ru')

    data = json.loads(trn.text)
    c = data['main']['pressure'] * 0.75
    m = f"{data["main"]["temp"]}"
    m = float(m)
    humidity = f"{data['main']['humidity']}"
    humidity = int(humidity)
    wind = f"{data['wind']['speed']}"
    weather = data['weather'][0]['description']
    wind = float(wind)



    await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
    text = f"{pic()}\nТекущая погода в Славновском сельсовете:"
    text_1 = '🌡 Температура воздуха:'
    text_2 = f'{pic_temp()} Чувствуется как:'
    text_3 = f'{pic_davlenie()} Атмосферное давление:'
    text_4 = '💦 Влажность:'
    text_5 = '💨 Ветер:'

    await message.answer(text=f"{text}"
                              f"\n\n{text_1} {data["main"]["temp"]}°"
                              f"\n{text_2} {data["main"]["feels_like"]}°"
                              f"\n{text_3} {c} мм рт.ст."
                              f"\n{text_4} {data['main']['humidity']} %"
                              f"\n{text_5} {data['wind']['speed']} м/c", reply_markup=key_get_start())

    await state.set_state(Survey.feedback)
    davlenie = f"{c}"
    davlenie = float(davlenie)

    if float(0.01) < wind <= float (0.20):
        a = "безветрянность"
    if float(0.21) < wind <= float (1.50):
        a = "незначительный ветер"
    if float(1.51) < wind <= float (3.30):
        a = "легкий ветер"
    if float(3.31) < wind <= float(5.40):
        a = "слабый ветер"
    if float(5.41) < wind <= float (7.90):
        a = "умеренный ветер"
    if float(7.91) < wind <= float (10.70):
        a = "свежий ветер"
    if float(10.71) < wind <= float (13.80):
        a = "сильный ветер"
    if float(13.81) < wind <= float (17.10):
        a = "крепкий ветер"
    if float(17.11) < wind <= float (20.70):
        a = "очень крепкий ветер"
    if float(20.71) < wind <= float (24.40):
        a = "штормовые условия"
    if float(24.41) < wind <= float (28.40):
        a = "сильно штормые условия"
    if float(28.41) < wind <= float (32.60):
        a = "жесткий шторм"
    if float(32.61) < wind:
        a = "ураган"

    if int(0) <= humidity <= int(40):
        b = "пониженная влажность"
    if int(41) <= humidity <= int(60):
        b = "комфортная влажность"
    if int(61) <= humidity <= int(100):
        b = "повышенная влажность"


    if float(750.00) <= davlenie <= float(770.01):
        c = "Атмосферное давление имеет комфортные для самочувствия показатели."
    if float(749.99) > davlenie:
        c = "Имеет место пониженное атмосферное давление, следите за своим самочувствием."
    if davlenie > float(770.02):
        c = "Атмосферное давление повышено, следите за своим самочувствием."


    if m <= float(-30.00):
        await message.answer(text=f"‼️ На улице крайне {weather}, холодно, преобладают {a} и {b}. Одевайтесь крайне тепло! {c}.\n\nНародная примета {mon()}:\n🗓️ {mounth()}\n\nДля получения актуальных сведений о состоянии текущей погоды в иных населенных пунктах нажмите 🔍. Далее в строке ввода наберите интересующее Вас название населенного пунта, нажмите - [отправить].", reply_markup=weather_keyboard)
    if m >= float(-30.00) and m <= float(-24.00):
        await message.answer(text=f"‼️ На улице {weather}, очень холодно, преобладают {a} и {b}. Одевайтесь очень тепло! {c}.\n\nНародная примета {mon()}:\n🗓️ {mounth()}\n\nДля получения актуальных сведений о состоянии текущей погоды в иных населенных пунктах нажмите 🔍. Далее в строке ввода наберите интересующее Вас название населенного пунта, нажмите - [отправить].", reply_markup=weather_keyboard)
    if m >= float(00.00) and m <= float(06.00):
        await message.answer(text=f"‼️ На улице {weather}, умеренно прохладно, преобладают {a} и {b}. Одевайтесь тепло! {c}.\n\nНародная примета {mon()}:\n🗓️ {mounth()}\n\nДля получения актуальных сведений о состоянии текущей погоды в иных населенных пунктах нажмите 🔍. Далее в строке ввода наберите интересующее Вас название населенного пунта, нажмите - [отправить].", reply_markup=weather_keyboard)
    if m >= float(06.00) and m <= float(12.00):
        await message.answer(text=f"‼️ На улице {weather}, прохладно, преобладают {a} и {b}. Одевайтесь теплее! {c}.\n\nНародная примета {mon()}:\n🗓️ {mounth()}\n\nДля получения актуальных сведений о состоянии текущей погоды в иных населенных пунктах нажмите 🔍. Далее в строке ввода наберите интересующее Вас название населенного пунта, нажмите - [отправить].", reply_markup=weather_keyboard)
    if m >= float(12.00) and m <= float(18.00):
        await message.answer(text=f"‼️ На улице {weather}, умеренно тепло, преобладают {a} и {b}. {c}\n\nНародная примета {mon()}:\n🗓️ {mounth()}\n\nДля получения актуальных сведений о состоянии текущей погоды в иных населенных пунктах нажмите 🔍. Далее в строке ввода наберите интересующее Вас название населенного пунта, нажмите - [отправить].", reply_markup=weather_keyboard)
    if m >= float(18.00) and m <= float(24.00):
        await message.answer(text=f"‼️ На улице {weather}, тепло, преобладают {a} и {b}. {c}\n\nНародная примета {mon()}:\n🗓️ {mounth()}\n\nДля получения актуальных сведений о состоянии текущей погоды в иных населенных пунктах нажмите 🔍. Далее в строке ввода наберите интересующее Вас название населенного пунта, нажмите - [отправить].", reply_markup=weather_keyboard)
    if m >= float(24.00) and m <= float(30.00):
        await message.answer(text=f"‼️ На улице {weather}, жарко, преобладают {a} и {b}. {c}\n\nНародная примета {mon()}:\n🗓️ {mounth()}\n\nДля получения актуальных сведений о состоянии текущей погоды в иных населенных пунктах нажмите 🔍. Далее в строке ввода наберите интересующее Вас название населенного пунта, нажмите - [отправить].", reply_markup=weather_keyboard)
    if m >= float(30.00) and m <= float(35.00):
        await message.answer(text=f"‼️ На улице {weather}, очень жарко, преобладают {a} и {b}. {c}\n\nНародная примета {mon()}:\n🗓️ {mounth()}\n\nДля получения актуальных сведений о состоянии текущей погоды в иных населенных пунктах нажмите 🔍. Далее в строке ввода наберите интересующее Вас название населенного пунта, нажмите - [отправить].", reply_markup=weather_keyboard)
    if m >= float(35.00):
        await message.answer(text=f"‼️На улице {weather}, крайне жарко, преобладают {a} и {b}. {c}\n\nНародная примета {mon()}:\n🗓️ {mounth()}\n\nДля получения актуальных сведений о состоянии текущей погоды в иных населенных пунктах нажмите 🔍. Далее в строке ввода наберите интересующее Вас название населенного пунта, нажмите - [отправить].", reply_markup=weather_keyboard)



@router.message(Command('raspisanie'))
async def start(message: types.Message, state: FSMContext):
    await message.answer(text="Выберите вид транспорта:",reply_markup=key_get_raspisaniee())
    await state.set_state(Survey.feedback)




@router.message(Command('project'))
async def start(message: types.Message, state: FSMContext):
    text = '[slavnoemyplace](https://www.instagram.com/slavnoemyplace/)'
    text_telegram = '[Славное, Толочинский район🌿](https://t.me/myplaceslavnoe)'

    await message.answer(text=f"Проект реализован командой сообществ {text}\nв социальной сети Instagram\\.",
                         parse_mode='MarkdownV2', reply_markup=key_get_start())
    await state.set_state(Survey.feedback)





gallery_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="︎Бросаю кость 🎲", callback_data="kubic")]])


@router.message(F.text == "Галерея")
async def send_naselennyi_punkt(message: types.Message):
    photo = '/Users/user/Desktop/СЛАВНОЕ/СЛАВНОЕ БОТ/routers/pic/random/1.jpg'
    photo_1 = '/Users/user/Desktop/СЛАВНОЕ/СЛАВНОЕ БОТ/routers/pic/random/2.jpg'
    photo_2 = '/Users/user/Desktop/СЛАВНОЕ/СЛАВНОЕ БОТ/routers/pic/random/3.jpg'
    photo_3 = '/Users/user/Desktop/СЛАВНОЕ/СЛАВНОЕ БОТ/routers/pic/random/5.jpg'
    h = [photo_1, photo_2, photo, photo_3]
    same = random.choice(h)
    await message.answer(f'{message.from_user.full_name}, представленная в текущем разделе галерея фотоснимков насчитывает триста шестьдесят тематических фотографий демонстрирующих красоту Славного сельского совета. Для удобного просмотра материалов реализован алгоритм случайного выбора.')

    await message.answer_photo(photo=types.FSInputFile(path=same))

    await message.answer(text=f"Для повторного получения случайного изображения из галереи воспользуйтесь игральной костью 🎲", reply_markup=gallery_menu)


@router.callback_query(F.data == 'kubic')
async def search(callback: CallbackQuery):
    photo = '/Users/user/Desktop/СЛАВНОЕ/СЛАВНОЕ БОТ/routers/pic/random/1.jpg'
    photo_1 = '/Users/user/Desktop/СЛАВНОЕ/СЛАВНОЕ БОТ/routers/pic/random/2.jpg'
    photo_2 = '/Users/user/Desktop/СЛАВНОЕ/СЛАВНОЕ БОТ/routers/pic/random/3.jpg'
    photo_3 = '/Users/user/Desktop/СЛАВНОЕ/СЛАВНОЕ БОТ/routers/pic/random/5.jpg'
    h = [photo_1, photo_2, photo, photo_3]
    same = random.choice(h)
    await callback.message.answer_photo(photo=types.FSInputFile(path=same))
    await callback.message.answer(text='Для продолжения воспользуйтесь игральной костью 🎲', reply_markup=gallery_menu)

















@router.message(Survey.photo, F.text)
async def full_name(message: types.Message, state: FSMContext):
    photo = '/Users/user/Desktop/СЛАВНОЕ/СЛАВНОЕ БОТ/routers/pic/random/DJI_0043.JPG'
    photo_1 = '/Users/user/Desktop/СЛАВНОЕ/СЛАВНОЕ БОТ/routers/pic/random/DJI_0047.JPG'
    photo_2 = '/Users/user/Desktop/СЛАВНОЕ/СЛАВНОЕ БОТ/routers/pic/random/DJI_0063.JPG'
    h = [photo_1, photo_2, photo]
    same = random.choice(h)

    await message.answer_photo(photo=types.FSInputFile(path=same))

    await state.set_state(Survey.photo)
    await state.clear()


def get_weather(city):
        params = {
            'q': city,
            'appid': API,
            'units': 'metric',
            'lang': 'ru'
        }

        response = requests.get(WEATHER_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            weatheerr = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'temperaturee': data['main']['feels_like'],
                'country' : data['sys']['country'],
                'descriptions': data['weather'][0]['description'],
                'himidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'speed' : data['wind']['speed']}

            text = f"{data['name']}, {country(city)}. Текущая погода:"
            text_1 = '🌡 Температура воздуха:'
            text_2 = f'🔥 Чувствуется как:'
            text_3 = f'🤕 Атмосферное давление:'
            text_4 = '💦 Влажность:'
            text_5 = '💨 Ветер:'

            man = (f"{text}\n\n{text_1} {data["main"]["temp"]}°"
                   f"\n{text_2} {data["main"]["feels_like"]}°"
                   f"\n{text_3} {data['main']['pressure'] * 0.75} мм рт.ст."
                   f"\n{text_4} {data['main']['humidity']} %"
                   f"\n{text_5} {data['wind']['speed']} м/c"
                   f"\n\n‼️ На улице {data['weather'][0]['description']}, {zharko(city)}, преобладают {veter(city)} и {vlazhnost(city)}. {davlenie(city)}"
                   f"\n\nДля получения актуальных сведений о состоянии текущей погоды в иных населенных пунктах нажмите 🔍. Далее в строке ввода наберите интересующее Вас название населенного пунта, нажмите - [отправить].")
            return man

        else:
            man = "Введенное Вами название населенного пункта, города не найдено."
            return man

        return None


def pic_davlenie(city):
    city = city
    trn = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(trn.text)
    c = data['main']['pressure'] * 0.75
    c = float(c)

    if float(750.00) <= c <= float(770.01):
        c = "😁"
        return c
    if float(749.99) > c:
        c = "🤕"
        return c
    if c > float(770.02):
        c = "🤕"
        return c

def pic_temp(city):
    city = city
    trn = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(trn.text)
    m = f"{data["main"]["temp"]}"
    m = float(m)
    if m > float(00.00):
        g = "🔥"
        return g
    if m <= float(00.00):
        g = "🥶"
        return g

def veter(city):
    city = city
    trn = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(trn.text)

    wind = f"{data['wind']['speed']}"

    wind = float(wind)


    if float(0.00) < wind <= float (0.20):
        a = "безветрянность"
        return a
    if float(0.30) < wind <= float (1.50):
        a = "незначительный ветер"
        return a
    if float(1.51) < wind <= float (3.30):
        a = "легкий ветер"
        return a
    if float(3.40) < wind <= float(5.40):
        a = "слабый ветер"
        return a
    if float(5.41) < wind <= float (7.90):
        a = "умеренный ветер"
        return a
    if float(8.00) < wind <= float (10.70):
        a = "свежий ветер"
        return a
    if float(10.80) < wind <= float (13.80):
        a = "сильный ветер"
        return a
    if float(13.90) < wind <= float (17.10):
        a = "крепкий ветер"
        return a
    if float(17.20) < wind <= float (20.70):
        a = "очень крепкий ветер"
        return a
    if float(20.80) < wind <= float (24.40):
        a = "штормовые условия"
        return a
    if float(24.50) < wind <= float (28.40):
        a = "сильно штормые условия"
        return a
    if float(28.50) < wind <= float (32.60):
        a = "жесткий шторм"
        return a
    if float(32.60) < wind:
        a = "ураган"
        return a


def vlazhnost(city):
    city=city
    city = city
    trn = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(trn.text)
    humidity = f"{data['main']['humidity']}"
    humidity = int(humidity)


    if int(0) <= humidity <= int(40):
        b = "пониженная влажность"
        return b
    if int(40) <= humidity <= int(60):
        b = "комфортная влажность"
        return b
    if int(60) <= humidity <= int(100):
        b = "повышенная влажность"
        return b


def davlenie(city):
    city=city
    trn = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(trn.text)
    c = data['main']['pressure'] * 0.75
    davlenie = f"{c}"
    davlenie = float(davlenie)

    if float(750.00) <= davlenie <= float(770.01):
        c = "Атмосферное давление имеет комфортные для самочувствия показатели."
        return c
    if float(749.99) > davlenie:
        c = "Имеет место пониженное атмосферное давление, следите за своим самочувствием."
        return c
    if davlenie > float(770.02):
        c = "Атмосферное давление повышено, следите за своим самочувствием."
        return c

def zharko(city):
    city = city
    trn = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(trn.text)
    m = f"{data["main"]["temp"]}"
    m = float(m)


    if m <= float(-30.00):
        a = 'крайне холодно'
        return a

    if m >= float(-30.01) and m <= float(-24.01):
        a = 'очень холодно'
        return a

    if m >= float(-24.00) and m <= float(-12.01):
        a = 'холодно'
        return a

    if m >= float(-12.00) and m <= float(-00.01):
        a = 'умеренно холодно'
        return a

    if m >= float(00.00) and m <= float(06.00):
        a = 'умеренно прохладно'
        return a

    if m >= float(06.01) and m <= float(12.00):
        a = 'прохладно'
        return a

    if m >= float(12.01) and m <= float(18.00):
        a = 'умеренно тепло'
        return a

    if m >= float(18.01) and m <= float(24.00):
        a = 'тепло'
        return a

    if m >= float(24.01) and m <= float(30.00):
        a = 'жарко'
        return a

    if m >= float(30.01) and m <= float(35.00):
        a = 'очень жарко'
        return a

    if m >= float(35.01):
        a = 'крайне жарко'
        return a




def country(city):
    city = city
    trn = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(trn.text)
    a = data['sys']['country']
    a = str(a)


    file = open('/Users/dzianis/PycharmProjects/SLV_BOT/routers/survay/country.txt', 'r')
    nuv = open('/Users/dzianis/PycharmProjects/SLV_BOT/routers/survay/num.txt', 'r')

    p = file.readline()
    l = nuv.readline()

    dictionary = ""
    dictionary = list(dictionary)

    dictionary_first = ""
    dictionary_first = list(dictionary_first)

    while p != "":
        p = p.rstrip("\n")
        dictionary.append(p)
        p = file.readline()

    file.close()

    while l != "":
        l = l.rstrip("\n")
        dictionary_first.append(l)
        l = nuv.readline()

    dictionary_one = {}
    for i in range(len(dictionary_first)):
        dictionary_one[dictionary_first[i]] = dictionary[i]

    file.close()
    nuv.close()
    math = dictionary_one[f'{str(a)}']
    return math



@router.message(Survey.feedback)
async def feedback(message: types.Message, state: FSMContext):
    username = message.from_user.id
    first_name = message.from_user.first_name
    second_name = message.from_user.last_name
    name_two = message.from_user.username

    same_one = 'Ваше сообщение принято! Благодарим за коммуникацию!'
    same_two = 'Сообщение успешно отправлено! Ожидает обработку!'
    same_three = 'Сообщение принято! Ожидает обработку!'
    h = [same_one, same_two, same_three]
    same = random.choice(h)



    await message.answer(f'{same}')

    await message.bot.forward_message(chat_id=2039046861, from_chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.send_message(chat_id=2039046861, text=f"ID: {username}\nFirstname: {first_name}\nSecondname: {second_name}\nNickname: {name_two}")
    await state.clear()

    await state.set_state(Survey.feedback)


@router.message(Survey.same_one)
async def feedback(message: types.Message, state: FSMContext):
    username = message.from_user.id
    first_name = message.from_user.first_name
    second_name = message.from_user.last_name
    name_two = message.from_user.username

    await message.answer(f'Отлично! Напиши суть претензии', reply_markup=replace)


    await message.bot.forward_message(chat_id=2039046861, from_chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.send_message(chat_id=2039046861, text=f"ID: {username}\nFirstname: {first_name}\nSecondname: {second_name}\nNickname: {name_two}")
    await state.clear()














def time_of_day():
    named_tuple = time.localtime()  # получить struct_time
    time_string = time.strftime("%H:%M:%S часов", named_tuple)
    time_string = str(time_string)

    if str("23:00.00") <= time_string <= str("23:59:59") or str("00:00:00") <= time_string <= str ("05:00:00"):
        k = str("Доброй ночи")
        return k

    if str("05:00:01") <= time_string <= str("11:00:00"):
        k = str("Доброе утро")
        return k

    if str("11:00:01") <= time_string <= str("16:00:00"):
        k = str("Добрый день")
        return k

    if str("16:00:01") <= time_string <= str("22:59:59"):
        k = str("Добрый вечер")
        return k

@router.message(CommandStart)
async def start(message: types.Message):
    text_telegram = '[«Мое место»](https://t.me/myplaceslavnoe)'
    await message.answer(text=f"{time_of_day()}\\, *{message.from_user.full_name}* 🖐\n\n"
             f"Мое имя Демид\\! Я бот\\-помощник\\, представляю Вам цифровую коммуникативную платформу\\, разработанную для жителей и гостей населенных пунктов\\,"
             f" входящих в состав Славновского сельского совета Толочинского района Витебской области 🌿\\. Наш телеграм\\-чат {text_telegram}\\, подписывайся\\!", parse_mode=ParseMode.MARKDOWN_V2, reply_markup=key_get_start())
    if message.from_user.id == int(2039046861):
        await message.answer(f'Вы авторизовались как администратор!', reply_markup=admin_key_get_start())


weather_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="︎Интересно знать", url='https://telegra.ph/Samaya-nizkaya-temperatura-za-istoriyu-meteonablyudenij-08-16')],
                                                         [InlineKeyboardButton(text='🔍', callback_data="search")]])

weather_keyboard_two = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="︎🔍", callback_data="search")]])


@router.callback_query(F.data == 'zavtra')
async def zavtra(callback: CallbackQuery):
    await callback.message.answer(text="💡 Самая низкая температура за всю историю метеонаблюдений в Беларуси - минус 42,2 градуса фиксировалась 17 января 1940 года в поселке Славное Толочинского района.")

def mon():
    named_tuple = time.localtime()  # получить struct_time
    main_data = time.strftime("%d.%m.%Y", named_tuple)
    main_data = str(main_data)

    if main_data[3] == str(0) and main_data[4] == str(1):
        t = "января"
        return t
    if main_data[3] == str(0) and main_data[4] == str(2):
        t = "февраля"
        return t
    if main_data[3] == str(0) and main_data[4] == str(3):
        t = "марта"
        return t
    if main_data[3] == str(0) and main_data[4] == str(4):
        t = "апреля"
        return t
    if main_data[3] == str(0) and main_data[4] == str(5):
        t = "мая"
        return t
    if main_data[3] == str(0) and main_data[4] == str(6):
        t = "июня"
        return t
    if main_data[3] == str(0) and main_data[4] == str(7):
        t = "июля"
        return t
    if main_data[3] == str(0) and main_data[4] == str(8):
        t = "августа"
        return t
    if main_data[3] == str(0) and main_data[4] == str(9):
        t = "сентября"
        return t
    if main_data[3] == str(1) and main_data[4] == str(0):
        t = "октября"
        return t
    if main_data[3] == str(1) and main_data[4] == str(1):
        t = "ноября"
        return t
    if main_data[3] == str(1) and main_data[4] == str(2):
        t = "декабря"
        return t

def pic():
    named_tuple = time.localtime()  # получить struct_time
    main_data = time.strftime("%d.%m.%Y", named_tuple)
    main_data = str(main_data)

    if main_data[3] == str(1) and main_data[4] == str(1) or main_data[3] == str(0) and main_data[4] == str(1) or main_data[3] == str(0) and main_data[4] == str(2):
        t = "На дворе зима ❄️"
        return t
    if main_data[3] == str(0) and main_data[4] == str(3) or main_data[3] == str(0) and main_data[4] == str(4) or main_data[3] == str(0) and main_data[4] == str(5):
        t = "На дворе весна 🦋️"
        return t
    if main_data[3] == str(0) and main_data[4] == str(6) or main_data[3] == str(0) and main_data[4] == str(7) or main_data[3] == str(0) and main_data[4] == str(8):
        t = "На дворе лето 🍃️"
        return t
    if main_data[3] == str(0) and main_data[4] == str(9) or main_data[3] == str(1) and main_data[4] == str(0) or main_data[3] == str(1) and main_data[4] == str(1):
        t = "На дворе лето 🍂"
        return t

def pic_temp():
    city = "славное"
    trn = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(trn.text)
    m = f"{data["main"]["temp"]}"
    m = float(m)
    if m > float(00.00):
        g = "🔥"
        return g
    if m <= float(00.00):
        g = "🥶"
        return g

def pic_davlenie():
    city = "славное"
    trn = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(trn.text)
    c = data['main']['pressure'] * 0.75
    c = float(c)

    if float(750.00) <= c <= float(770.01):
        c = "😁"
        return c
    if float(749.99) > c:
        c = "🤕"
        return c
    if c > float(770.02):
        c = "🤕"
        return c

def mounth():
    named_tuple = time.localtime()  # получить struct_time
    main_data = time.strftime("%d.%m.%Y", named_tuple)
    main_data = str(main_data)

    if main_data[3] == str(0) and main_data[4] == str(1):
        a1 = "1 января — Новый год. Если сильный мороз и мало снега — к хорошему урожаю хлеба."
        a2 = "5 января Федул. На этот день существует поговорка: Пришел Федул, ветер надул — к урожаю."
        a3 = "7 января — Рождество. Перед праздником смотрели в небо: если на нем много звезд — будет много грибов и ягод. Святочные дни (с Рождества до Крещения). Если они пасмурные и теплые, то хлеб уродится хороший, если ясные — к неурожаю."
        a4 = "Крестьяне говорили: Снега под Крещение надует — хлеба прибудет. Также считалось, что ясная и холодная погода — к засушливому лету, пасмурная и снежная — к обильному урожаю. Звездная ночь на Крещение — уродятся горох и ягоды."
        a5 = "21 января — Емельян. Надо следить за ветром: если подует с юга — посулит грозовое лето."
        a6 = "23 января — Григорий. Если на стогах образуется иней — лето будет сырое и холодное."
        a7 = "25 января — Татьяна. В народе отмечали: Снег на Татьяну — лето дождливое, проглянет солнышко — к раннему разливу. Закат пурпурного цвета — к большому снегопаду. Солнце заходит в красную переливающуюся зарю — завтра будут ветер и мороз. Солнечные лучи идут пучками вниз — к холоду, вверх — к вьюге. Луна светит ярко, а в безлунную ночь небо усыпано яркими звездами — завтрашний день будет ясным и морозным."
        a8 = "Лес шумит — к оттепели; треск усиливается — к сильным морозам."
        a9 = "Ворона кричит на полдень, в сторону юга - к теплу, на север - к холоду."
        a10 = "Снегири поют при смене погоды - перед снегопадом."
        a11 = "Воробьи сидят на деревьях втихомолку - пойдет снег без ветра."
        a12 = "Собака растягивается на полу и спит, раскинув лапы, - к теплой погоде."
        a13 = "В январе висит много частых и длинных сосулек - урожай будет хороший."
        a14 = "В январе растет день - растет и холод."
        a15 = "В январе снегу надует - хлеба прибудет."
        a16 = "Если январь сухой, морозный и вода в реках сильно убывает, то лето будет сухое и жаркое."
        a17 = "С января солнце на лето поворачивает."
        a18 = "Январь на порог, прибыло дня на воробьиный скок."
        a19 = "Январь подкладывает дров в печку."
        a20 = "Январь тулуп до пят надевает, хитрые узоры на окнах расписывает, глаз снегами тешит да ухо морозом рвет."
        a21 = "Январю-батюшке - морозы, февралю - метелицы."
        a22 = "Сух январь — крестьянин богат."
        a23 = "Если в январе очень холодно, то грибы появятся позднее."
        a24 = "Если в январе март — бойся в марте января."
        a25 = "Если январь холодный, июль будет сухой и жаркий."
        a26 = "Зимой снег глубокий - летом хлеб высокий."
        a27 = "Много снега - много хлеба."
        a28 = "Морозный январь - урожайный год."
        a29 = "Серый январь - хлебам беда."
        a30 = "Рано в январе начинает стучать дятел - к ранней весне."
        a31 = "Если в январе частые снегопады и метели, то в июле частые дожди."
        er = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23,
              a24, a25, a26, a27, a28, a29, a30, a31]
        return random.choice(er)

    if main_data[3] == str(0) and main_data[4] == str(2):
        a1 = "1 февраля — Макар. Если погода ясная — будет ранняя весна."
        a2 = "На Ефима (2 февраля) в полдень солнце — к ранней весне, если метель — вся Масленица метельная. (Масленица обычно приходится на последнюю неделю февраля)."
        a3 = "Какова Аксинья (погода на 6 февраля) — такова и весна."
        a4 = "Ветер понесся — к сырому году."
        a5 = "14 февраля — Трифон. Если небо звездное — к поздней весне."
        a6 = "Если на Сретение (15 февраля) установится оттепель, то весна будет ранней и теплой, если холода — холодной, выпавший в этот день снег — к затяжной и дождливой весне. На Сретение снежок — весной дождёк."
        a7 = "Злится февраль-коротышка, что ему мало дней дадено."
        a8 = "У февраля два друга: метель, да вьюга."
        a9 = "Что январь упустил — то февраль подберет."
        a10 = "Январю — морозы, февралю — метели."
        a11 = "Февраль — апрельский дедушка, зиму замыкает, дни прибавляет, солнце на лето поворачивает."
        a12 = "Хоть и злится февраль, а весну чует."
        a13 = "В феврале и снег весною пахнет."
        a14 = "Февраль бока греет, ноги студит."
        a15 = "Если февраль дождливый, то весна и лето тоже будут дождливыми. Сухой февраль – к засухе."
        a16 = "Тёплый февраль – к холодной весне."
        a17 = "Как февраль аукнется, так осень откликнется."
        a18 = "Много инея на деревьях – будет много мёда."
        a19 = "Снег к деревьям прилипает – к теплу."
        a20 = "У лошадей копыта потеют – к потеплению."
        a21 = "Ветряная погода без инея – к бурану."
        a22 = "Луна покраснела – к ветру, теплу и снегу."
        a23 = "Кошка на задние лапы встает и когтями стены скребет – будет тепло."
        a24 = "Февраль зиму провожает, а весну встречает."
        a25 = "В феврале зима с весною борются: кому дальше идти, кому вспять повернуть."
        a26 = "Хоть февраль злится, но весну чует."
        a27 = "Вьюги да метели на февраль налетели: бегут по снегу, а следу нету."
        er = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23,
              a24, a25, a26, a27]
        return random.choice(er)

    if main_data[3] == str(0) and main_data[4] == str(3):
        a1 = "Март сухой да мокрый май — будет каша да каравай."
        a2 = "Ранняя весна ничего не стоит."
        a3 = "Рано затает — долго не растает."
        a4 = "Поздняя весна сулит раннюю зиму."
        a5 = "Весна да осень — на дню погод восемь."
        a6 = "Весной сверху печет, а снизу — морозит."
        a7 = "Весной и осенью дождь со снегом чередит."
        a8 = "Зима весну пугает, да все равно тает."
        a9 = "Как зима не злится, а все весне покорится."
        a10 = "Весной грач прилетел — через месяц снег сойдет."
        a11 = "Грач на горе — весна на дворе."
        a12 = "Март-месяц любит куролесить: морозом гордится и на нос садится."
        a13 = "Пришел марток — надевай семеро порток."
        a14 = "Если в мартовские метели снег ложится на полях волнисто, то хорошо родятся овощи и яровые хлеба."
        a15 = "Лес почернел — к оттепели. На раннем льду появилась вода — к теплу."
        a16 = "Ранний прилет грачей и жаворонков — к ранней весне."
        a17 = "22 марта — сорок мучеников. Сорок мучеников — сорок утренников, предстоит еще сорок заморозков."
        a18 = "Если грачи прямо на гнезда летят — к дружной весне."
        a19 = "В марте пошел дождь — будет богатый урожай грибов."
        a20 = "Часто опускаются туманы — лето будет дождливым."
        a21 = "Грянул гром — жди похолодания."
        a22 = "Если первый весенний месяц холодный и сухой — будет много хлеба."
        a23 = "Редкие заморозки — к урожайному году."
        a24 = "Если в марте сосульки длинные, то ожидается затяжная весна."
        a25 = "Дождь в марте – к грибному лету."
        a26 = "Мартовский гром предвещает затяжные холода."
        a27 = "Если в марте снег не тает, то травы в апреле не будет."
        er = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23,
              a24, a25, a26, a27]
        return random.choice(er)

    if main_data[3] == str(0) and main_data[4] == str(4):
        a1 = "Первый гром при северном ветре — весна будет холодной, восточном — сухой и теплой, западном — мокрой, при южном — теплой."
        a2 = "Из березы течет много сока — к дождливому лету. Если береза распустится раньше ольхи и клена, лето будет сухим, а если наоборот — мокрым."
        a3 = "8 апреля — Гавриил, Василий. Какова погода 8 апреля — такова и 8 октября, и наоборот."
        a4 = "21 апреля — Родион-ледолом, ревучие воды. Ясный день — хорошее лето, ненастье — плохое лето."
        a5 = "29 апреля — Ирина — урви берега. В этот день обычно кукушка начинает куковать."
        a6 = "Если в апреле день жаркий, а ночь прохладная, погода пока меняться не будет."
        a7 = "Днем пасмурно, а к ночи прояснилось — ждите заморозка."
        a8 = "Ясные ночи, как правило, заморозками кончаются."
        a9 = "Грачи стаями над гнездами носятся, кричат и тут же взлетают — погода переменится."
        a10 = "Если береза много сока дает — лето дождливое будет."
        a11 = "Птицы вьют гнезда на солнечной стороне — прохладным будет лето."
        a12 = "Апрель красен почками — май листочками. Ранний вылет пчел — признак ранней и теплой весны. Сырую погоду было не принято ругать ни при каких обстоятельствах. Апрель с водою — май с травою."
        a13 = "Мокрый апрель — хорошая пашня."
        a14 = "В апреле — по колено зима, а по плечи лето."
        a15 = "1 апреля — Дарья Грязные пролубницы. На Дарью проруби мутятся. Если вешняя вода на Дарью идет с шумом — травы хорошие бывают, а когда тихо — быть им жухлыми и низкорослыми."
        a16 = "4 апреля — Василий Солнечник. Апрель-снегогон дороги рушит, а кругом ручьи да лужи. Воды столько, что она уже ночами начинает сниться."
        a17 = "6 апреля — Захарий день. Коли ночь теплая, то весна дружная."
        a18 = "7 апреля — на Благовещение — в третий и в последний раз встречаются Весна с Зимой. Сдала Зима свои позиции, но выговорила-выторговала-таки себе право еще 40 раз (40 утренников или заморозков) наведываться в сады по вечерам или утрам."
        a19 = "Если на Благовещение ночь теплая — весна будет дружная."
        a20 = "Если на Благовещение небо безоблачное — лету быть грозному, но зато пшеница уродится."
        a21 = "Дождь на Благовещение хороший урожай грибов предвещает, а морозец — огурцы сулит."
        a22 = "Гроза на Благовещение — к урожаю орехов, а иней и туман — к урожаю яровых."
        a23 = "Весна до Благовещения — много морозов впереди (40 холодных утренников)."
        a24 = "Коли на Благовещение снег на крышах лежит, так лежать ему до Егория (6 мая) и в поле."
        a25 = "Поверхность снега в начале апреля шероховатая - к урожаю."
        a26 = "В конце апреля идут теплые дожди - к урожаю."
        a27 = "Если ласточки еще не прилетели в апреле – вся весна будет холодной."
        er = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23,
              a24, a25, a26, a27]
        return random.choice(er)

    if main_data[3] == str(0) and main_data[4] == str(5):
        a1 = "Майские холода — к урожаю."
        a2 = "Май холодный — год хлебородный."
        a3 = "На Козьму (1 мая) в рубашке пахать — в шубе сеять."
        a4 = "Теплый вечер и звездная ночь на Якова (13 мая) — к ветреному и сухому лету, а теплый день с дождем предвещает обильные хлеба."
        a5 = "На Еремея (14 мая) погоже — уборка хороша, непогодь — всю зиму промаешься». Если накануне восход солнца был ясным, то и все лето будет ясным."
        a6 = "Арина-рассадница (18 мая). Срок высадки рассады."
        a7 = "Иов — горошник (19 мая). Часто его также называли огуречником. Большая роса в этот день — к урожаю огурцов."
        a8 = "От Николы (22 мая) осталось двенадцать морозов-утренников, коли не весной, то на Семенов день (14 сентября)."
        a9 = "На Мокия (24 мая) мокро — все лето мокро. Если в этот день солнечный восход багряный, то лето будет с грозами."
        a10 = "Если на Епифана (25 мая) утро красное, то лето будет жаркое и сухое."
        a11 = "На Сидора (28 мая) сиверко — все лето холодное, на Пахома тепло — все лето теплое."
        a12 = "Если дуб одевается листвой раньше ясеня, лето будет сухим."
        a13 = "Желтые цветки одуванчика перед дождем закрываются, если его семена — парашютики сжимаются, как зонтики, — быть дождю, если они долго парят в воздухе — к хорошей погоде."
        a14 = "Когда утром чувствуется сильный запах цветков желтой акации — днем будет гроза."
        a15 = "В мае все принарядится — там листком, тут цветком, а где и травинкой."
        a16 = "В мае даже ветер весело поет."
        a17 = "Май на порог весну приволок, леса наряжает, лето в гости ожидает."
        a18 = "Но как не верили крестьяне капризному апрелю, так и на ласковый май не возлагали они радужных надежд."
        a19 = "Ай, ай, месяц май — и тепел, да холоден."
        a20 = "Майская травка и голодного накормит."
        a21 = "Май — коню сена дай да на печь полезай."
        a22 = "Наш пономарь понадеялся на май, и без коровы стал."
        a23 = "Первая майская гроза, согласно поверью, достаток намывала. Поэтому, заслышав громовые раскаты, молодежь на улицу спешила, чтоб удачу поймать, а старики, за счастьем уже не гнавшиеся, лишь крестились, да приговаривали: «Пошли, Господи, тихую воду и теплую росу»."
        er = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23]
        return random.choice(er)

    if main_data[3] == str(0) and main_data[4] == str(6):
        a1 = "Если первые два дня месяца льет дождь — июнь будет сухим. Вороны садятся клювами в одну сторону — к сильному ветру."
        a2 = "Пришел Фалей (2 июня) — досевай огурцы скорей."
        a3 = "Если 3 июня дождь с градом, то 3 декабря будет снег с «крупой»."
        a4 = "Обильная роса 7 июня (Иванов день) — к хорошему урожаю. Должна зацвести рябина: если она хорошо цветет — к урожаю льна, позднее цветение — к долгой осени."
        a5 = "Коли на Евтихия (10 июня) тихо, без ветра — к урожаю."
        a6 = "Считается, если на Устина (14 июня) утро пасмурное — к урожаю яровых, дождливое — к урожаю льна."
        a7 = "На Лукьяна в канун Митрофана (17 июня) не ложись спать рано, а приглядывайся откуда ветер дует. Тянет с полудня (юга) — яровому хороший рост, дует с гнилого угла (северо-запада) — жди ненастья."
        a8 = "Если днем листочки кислицы располагаются параллельно поверхности почвы, а на ночь складываются вдвое, то погода будет ясной, если наоборот — пойдет дождь."
        a9 = "Исключительный предсказатель погоды и чертополох. Перед пасмурными днями его колючки плотно сжимаются и совсем не колются, а перед жаркими — отгибаются в стороны. Перед дождем поникают фиалки, полевой вьюнок, чистотел, маргаритки, клевер. Не раскрывают бутоны розы, шиповник, мальва. На черешках листьев клена появляются капельки нектара. Усиленно выделяют нектар и хорошо пахнут дрема, жимолость, табак, донник, левкой. Если на листьях конского каштана выступают капли воды — начнутся продолжительные дожди."
        a10 = "Если в теплый день сильно стучит дятел, скоро будет дождь. Грачи пасутся на траве — к дождю, играют — к хорошей погоде."
        a11 = "Утки перед дождем ныряют и плещутся, а индейки оправляют перья. Если в небе ни облачка, а бабочка крапивница залетает в дом или прячется в куче сухого мусора, значит через несколько часов начнется гроза."
        a12 = "Обильная роса — к солнцу, ее отсутствие — к дождю. Утром туман стелется по воде — к хорошей погоде. Солнце печет в жаркую погоду — к грозе или граду."
        a13 = "В радуге больше красного цвета — дождь скоро прекратится, больше синего — усилится. Вечерняя радуга — к хорошей погоде, утренняя — к дождливой. Если вечерняя заря светло-розовая, то, даже несмотря на небольшие тучи, завтра в первой половине дня будет хорошая погода. Если в пасмурный вечер хорошо просматривается горизонт и отчетливо слышны звуки — завтра будет дождь, а возможно, и гроза."
        a14 = "Вечерняя радуга в июне предвещает хорошую погоду."
        a15 = "Красные облака до восхода солнца – к ветру, тучи – к дождю."
        a16 = "Обильные росы в июне – к хорошему урожаю."
        a17 = "Частые туманы в июне обещают урожай грибов."
        a18 = "Если ночи в июне теплые, ждите изобилия плодов."
        a19 = "Поздний расцвет рябины – к долгой осени."
        a20 = "Если жаворонок вьет гнездо в ямке, то лето будет сухим, а если вьет на бугорке – то мокрым."
        a21 = "Если соловей поет всю ночь, не умолкая, то следующий день будет ветреным."
        a22 = "Журавли летают высоко – к ненастью."
        a23 = "Если вокруг муравейника много муравьев – к хорошей погоде."
        a24 = "Если в первом месяце лета часто моросит небольшой дождь – урожай вас порадует."
        a25 = "Много шишек на ели – ждите хороший урожай огурцов."
        a26 = "Частые грозы сулят хороший урожай."
        a27 = "Много комаров – к изобилию ягод."
        er = [a1, a2, a3, a4,a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21,a22, a23, a24, a25, a26, a27]
        return random.choice(er)

    if main_data[3] == str(0) and main_data[4] == str(7):
        a1 = "Если в день на Мефодия (3 июля) дождь, то он будет идти сорок дней."
        a2 = "Трава в соку, сбор лечебных трав. Крестьяне считали этот день лучшим для посева репы: «Репу сей на Аграфену (6 июля — Аграфена-купальница: начало купания) — хорошая репа будет»"
        a3 = "В Иванову (7 июля — Рождество Иоанна Крестителя, или, как называют этот день в народе, Иван Купала) ночь смотрели на небо: если звездно — будет много грибов. А под утро наблюдали за росой: если она обильная, то будет хороший урожай огурцов."
        a4 = "8 июля — Петр и Феофания. С этого дня можно ожидать еще сорок жарких дней."
        a5 = "10 июля — Самсон-сеногной. Считалось, что если на Самсона дождь, то он будет продолжаться до «бабьего лета» (14 сентября)."
        a6 = "12 июля — Петр и Павел. С этого времени начинают темнеть ночи. Петр и Павел день убавил. Петр и Павел жару прибавил."
        a7 = "Дождь на Святого Петра — урожай худой, два — хороший, три дождя — богатый."
        a8 = "Кувшинки на реке раскрываются и уходят под воду — к дождю. Клен «плачет» — скоро пойдет дождь. У каштана обильно выделяются капли клейкой жидкости — к длительному дождю через 1-2 суток."
        a9 = "Ласточки и стрижи летают близко к земле, воробьи прячутся под крышу — будет гроза. Лягушки держатся на поверхности воды, поднимают головы и квакают — к ненастью. Если дождевые червы выползают из земли — ясная погода сменится грозой. Кузнечики дружно прыгают и стрекочут — к сухой и ясной погоде. Если вечером в лесу теплее, чем в поле, а комары и другие насекомые клубятся — завтра будет теплый и ясный день."
        a10 = "Ночью нет росы, а в низинах не видно тумана — к ненастью. Звезды блестят — к жаре, мерцают — к грозе, падают — к ветру. Если на рог месяца можно мысленно навесить ведро — будет сухо, если ведро «падает» — пойдет дождь."
        a11 = "Небо заволокли белые облака с четкими контурами — дождя не будет, но возможен ветер."
        a12 = "Ясный закат — к ясной погоде, красный — к ветру, бледный — к дождю."
        a13 = "Глухой гром — ожидается тихий дождь, гулкий — будет беспрерывный ливень, град. Гром гремит долго и не резко — будет ненастье, отрывисто и непродолжительно — хорошая погода."
        a14 = "Если июль жаркий, то декабрь будет морозный."
        a15 = "Если июльским утром туман стелется по воде — будет хорошая погода."
        a16 = "Гром гремит долго — к ненастью, отрывисто — будет ясно."
        a17 = "Радуга с севера на юг с ярким красным цветом – к ненастью."
        a18 = "Утром нет росы – ночью будет дождь."
        a19 = "Если июльским утром прошел маленький дождь, то днем установится хорошая погода."
        a20 = "Если в июле много осота – ждите холодной зимы, много щавеля – к теплой зиме."
        a21 = "Лилия утром едва поднялась над водой – к дождю."
        a22 = "Паук вышел из гнезда и мастерит новую паутину – к хорошей погоде."
        a23 = "Ласточки задевают крыльями поверхность воды — к дождю."
        a24 = "Вороны взвиваются в небо — к ненастью."
        a25 = "Вечерняя заря золотисто–желтая с розовыми отблесками – к хорошей погоде. Зеленая окраска луны признак наступления сильной засухи."
        a26 = "Лес без ветра шумит – к дождю."
        a27 = "Протяжный гром – к долгому ненастью."

        er = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23,
              a24, a25, a26, a27]
        return random.choice(er)

    if main_data[3] == str(0) and main_data[4] == str(8):
        a1 = "Макрида (1 августа) мокра — и осень мокра, Макрида суха — и осень тоже."
        a2 = "Какая на Илью (2 августа) погода до обеда — такое будет лето, а какая погода после обеда — такая будет осень."
        a3 = "4 августа — Мария Магдалина. Громовой день."
        a4 = "7 августа — Анна Зимоуказательница (Анна-холодница и Макарий). По этому дню судили о зиме. Если утренник холодный — и зима холодная. Какая погода до обеда — такая зима до декабря, какая погода после обеда — такая зима после декабря (ясный и теплый день предвещает холодную зиму, дождливый — снежную)."
        a5 = "14 августа — первый Спас медовый."
        a6 = "19 августа — второй Спас. Преображение."
        a7 = "27 августа — Михей-Тиховей. Если в этот день дуют тихие ветры — к погожей осени, буря — к ненастной."
        a8 = "28 августа — Успение."
        a9 = "29 августа — третий Спас Нерукотворный, хлебный, ореховый."
        a10 = "Если в первую неделю августа стоит постоянная погода, то зима будет долгой и снежной."
        a11 = "Туман долго не рассеивается - к ясной погоде."
        a12 = "Август без дождя - к теплой и сухой осени."
        a13 = "Выпал иней в августе - знак ранней, студеной зимы."
        a14 = "Много гроз в августе - к длительной осени."
        a15 = "Если в августе на деревьях, особенно на березе, появляется много желтых листьев, то осень будет ранняя."
        a16 = "Теплый и сырой август - к урожаю грибов."
        a17 = "Если журавли в конце августа собираются стаями и летят на юг, то будет ранней и зима."
        a18 = "В августе дуб желудями богат - к урожаю."
        a19 = "Если кроты выходят из-под земли, то ожидается ухудшение погоды."
        a20 = "Если ласточки купаются и тревожно летают, то в гнездо, то из гнезда — быть дождю."
        a21 = "Если листья деревьев показывают свою изнанку — быть дождю."
        a22 = "В августе дуб богат желудями — к урожаю."
        a23 = "Если в августе листья на деревьях желтеют снизу, то ранний сев будет хорошим."
        a24 = "Если лягушки прыгают на берег и квакают днем, то будет дождь."


        er = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23,
              a24]
        return random.choice(er)

    if main_data[3] == str(0) and main_data[4] == str(9):
        a1 = "Сентябрьское солнце, будто устав за долгое лето, все ближе к земле льнет, темные ночи смелеют, а туманы норовят с холодными утренниками побрататься. Но если раскатисто и по-хозяйски громко гремит в занавешенном тучами небе сентябрьский гром — осень обещает быть теплой."
        a2 = "Вторичное цветение яблони — к долгой осени. На деревьях листья желтеют снизу кроны — осень будет долгой."
        a3 = "Если листья березы желтеют с верхушки — предстоит ранняя весна, снизу — поздняя, а если равномерно по всей кроне — то сроки наступления весны будут средне многолетними."
        a4 = "Журавли летят высоко, не спеша, курлыкают — к хорошей осени."
        a5 = "Птицы летят низко — ожидается холодная зима, высоко — теплая."
        a6 = "Большие муравьиные кучи — будет суровая зима."
        a7 = "Гром в сентябре — к продолжительной теплой осени."
        a8 = "Хоть и холоден батюшка сентябрь — да сыт."
        a9 = "Что июль с августом не сварят — сентябрь приберет, а кто запаслив — тот и счастлив. Что осенью руками соберешь, то зимой губами подберешь."
        a10 = "3 сентября — Фаддей и Василиса. Если день ясный и безоблачный, еще четыре недели должна продержаться хорошая погода."
        a11 = "5 сентября — Лупп Брусничник. Если в этот день журавли на юг потянули — зима ранняя. Если журавли летят низко, то зима теплая, высоко — холодная."
        a12 = "6 сентября — Арсений. В этот день наши редки ходили в лес и наблюдали за комарами: если их много, то зима предстоит мягкая."
        a13 = "11 сентября — Иван Постный, Полеток. Иван-постный пришел, лето красное увел."
        a14 = "13 сентября — Куприянов день. Если на Куприяна можно увидеть журавлей, то зима будет поздняя."
        a15 = "14 сентября — Семен Летопроводец, Осенины (начало «бабьего лета»). Если этот день дождливый, то и осень будет мокрой, а если теплый, то зиму надо ждать мягкую."
        a16 = "23 сентября — Петр и Павел Рябинники. В этот день смотрели на рябину: низко склонилась — к теплой и мокрой зиме, не склонилась — к холодной."
        a17 = "29 сентября — Шиповница. В этот день полагалось не только собирать шиповник, но и наблюдать за другими дарами леса: если грибов уже нет, а орехи все еще есть — зима будет снежной и суровой."
        a18 = "30 сентября — Вера, Надежда, Любовь и мать их Софья."
        a19 = "Много паутины в сентябре на бабье лето — к ясной осени, к холодной зиме."
        a20 = "Поздний листопад — к суровой и продолжительной зиме."
        a21 = "Листопад проходит скоро — зима будет холодная."
        a22 = "Если осенью листья берез начнут желтеть с верхушки — весна будет ранняя, снизу — поздняя."
        a23 = "Если в сентябре муравьи бегают по верхушкам травы, то снег будет глубокий и зима ранняя, а если по низу — то долгая."
        a24 = "Если журавли летят высоко, не спеша и курлычат — будет стоять хорошая осень."
        a25 = "Какая погода в первый день сентября, такой будет и вся осень."
        er = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23,
              a24, a25]
        return random.choice(er)

    if main_data[3] == str(1) and main_data[4] == str(0):
        a1 = "Если в начале октября лист березы или дуба не полностью опадает — к позднему снегу и холодной зиме, поздний листопад — к продолжительной суровой зиме."
        a2 = "Октябрьский гром — к бесснежной зиме."
        a3 = "Много рябины — много грязи."
        a4 = "Пока лист с вишен не опал, сколько бы снегу не выпало, оттепель его сгонит."
        a5 = "Первый снежок не лежок, выпал и тает."
        a6 = "Если в октябре звезды яркие — к хорошей погоде."
        a7 = "1 октября — Арина. На Арину — конец белых грибов. Если на Арину журавли полетели, то на Покров (14 октября) надо ждать первого мороза, а если их в этот день не видно, то раньше Артемия (2 ноября) не ударит ни один мороз."
        a8 = "3 октября — Астафий. Если на Астафия туманно и тепло, а по проулкам летает паутина — к благоприятной осени и не скорому снегу."
        a9 = "Примечали и ветер: северный — к стуже, южный — к теплу, западный — к дождю, восточный — к ведру. Кроме того, южный ветер в этот день — к хорошему урожаю озимого хлеба."
        a10 = "4 октября — Кондратий и Игнат. Погода этого дня должна продержаться без изменений четыре недели."
        a11 = "7 октября — Фекла. Фекла — дергай свеклу."
        a12 = "13 октября — Григорий. Если в этот день выпадает снег, зима не скоро настанет."
        a13 = "14 октября — Покров. На Покров северный ветер к холодной зиме, южный — к теплой, западный — к снежной, переменный — к непостоянной. Если на Покров день морозно и лежит снег, вся зима будет морозной и суровой. Первый сухой снег обещает хорошее лето. Ранний снег до Покрова дня упадет — зима не скоро наступит. Ранний снег — к ранней весне."
        a14 = "20 октября — Сергий. С Сергия зима начинается, дневной снег не лежит, а первый надежный выпадает ночью."
        a15 = "23 октября — Евлампий. Если на Евлампия рога месяца показывают на север, быть скорой зиме, и снег ляжет посуху, на юг — скорой зимы не жди, будет слякоть до Казанской (до 4 ноября). На Евлампия рога месяца показывают в ту сторону, откуда быть ветрам. Снег ляжет посуху — быть суровой зиме."
        a16 = "25 октября — Пров. Полагалось наблюдать за звездами: если они яркие — будет мороз, тусклые — оттепель, мерцают синим цветом — будет снег, много ярких звезд — к урожаю гороха."
        a17 = "27 октября — Прасковья, Параскева-грязниха. Наши предки верили, что если на Параскеву грязь велика, то выпавший снег сразу установит санный путь."
        a18 = "Если в октябре случается гроза, то зима ожидается малоснежной и короткой."
        a19 = "Зима наступит через тридцать дней после выпадения первого снега."
        a20 = "Если первый снег лег на сухую землю, то он скоро растает."
        a21 = "Если первый снег выпал днем, то он не будет долго лежать."
        a22 = "Быстрый листопад – к суровой зиме."
        a23 = "Если деревья долго не сбрасывают листья, то можно ожидать теплую и короткую зиму."
        a24 = "Перелетные птицы улетают в первых числах октября – к скорой и холодной зиме."
        a25 = "Если птицы улетают в конце октября – к затяжной осени и мягкой зиме."
        a26 = "Если в октябре дуб полностью сбросил листву, то можно ожидать теплую зиму."
        a27 = "Холодный октябрь – признак лютой зимы."
        er = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23,
              a24, a25, a26, a27]
        return random.choice(er)

    if main_data[3] == str(1) and main_data[4] == str(1):
        a1 = "Много снега в ноябре — будет урожай хлеба. Если снег лег на мокрую землю и не растаял, значит весной рано и дружно зацветут подснежники. По возможности следят за мышами: если мыши делают большие запасы — предстоит суровая и снежная зима."
        a2 = "Первая пороша — еще не санный путь."
        a3 = "Ноябрь с гвоздем, декабрь с мостом."
        a4 = "4 ноября — Казанская. В народе про этот день говорили: «Коли на Казанскую небо заплачет, то следом за дождем и зима придет. Первый снежок показался — настоящий через месяц будет»."
        a5 = "5 ноября — Яков. Крестьяне считали, что если на Якова крупица, то с Матрены (22 ноября) зима станет на ноги."
        a6 = "8 ноября — Дмитрий. Если в этот день холодно и снежно — весна будет поздней и холодной, если оттепель — зима и весна будут теплыми."
        a7 = "14 ноября — Кузьма и Демьян, или Кузьминки. «Кузьма и Демьян куют лед на земле и на водах», — утверждает пословица. Снежный день обещает большой весенний разлив. Если в этот день на деревьях еще есть листья — на следующий год ожидается мороз."
        a8 = "19 ноября — Павел и Варлаам. Много снега в этот день — к снежной зиме."
        a9 = "21 ноября — Михайлов день. Зима встает на ноги в Михайлов день."
        a10 = "23 ноября — Ераст. Наши предки говорили: «С Ераста жди ледяного наста». Но если в этот день на деревьях иней, а на следующий день после Федора-студита (25 ноября) землю запорошит снегом, то вплоть до Введения (4 декабря) будут оттепели и простоит осенняя распутица."
        a11 = "25 ноября — день Студита. Со Студита станет холодно и сердито. Но если в этот день на дворе дождь или снег, то оттепели быть долго."
        a12 = "28 ноября — Гурий. Выпавший в этот день снег не тает до весны."
        a13 = "29 ноября — Матвей. Считалось, что если на Матвея веют буйные ветры, то до Николы (19 декабря) быть вьюгам и метелям."
        a14 = "Гусь лапку поджимает — ожидается стужа, полощется в воде — тепло."
        a15 = "Длинные сумерки — к ненастью, короткие — к хорошей погоде."
        a16 = "Если деревья сбросили не все листья, то впереди ожидается лютая зима."
        a17 = "Затянувшийся листопад – примета долгой зимы."
        a18 = "Гроза в ноябре предсказывает малоснежную зиму."
        a19 = "Какая погода в ноябре, таким ожидается апрель."
        a20 = "Если в ноябре вновь появились комары, то можно рассчитывать на теплую зиму."
        a21 = "Снег лег на землю в первых числах ноября – весна придет рано."
        a22 = "Ясный день – признак скорого похолодания. Ненастье с дождем предвещает скорую зиму."
        a23 = "Если 5 ноября идет снежная крупа, то 22 ноября можно ожидать наступления настоящей зимы."
        a24 = "Считалось, что со дня Нестора (9 ноября) вода замерзает."
        a25 = "12 ноября прилетают на зиму синички и снегири. Если стайки синиц кружатся вокруг жилья, то можно ожидать скорых морозов."
        a26 = "Иней или снег 21 ноября предсказывает обильный снегопад. Ясный день – знак лютой зимы. Утренний туман показывает на оттепель. Мокрый снег – примета дождливой весны."
        a27 = "Дождь предвещает теплую зиму, кроме того 4 декабря будет стоять теплая погода"
        er = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23,
              a24, a25, a26, a27]
        return random.choice(er)

    if main_data[3] == str(1) and main_data[4] == str(2):
        a1 = "Cухой декабрь сулит сухую весну и лето."
        a2 = "1 декабря — Платон и Роман. Если день теплый — зима будет теплой, а если в течение дня погода переменится, то и зима будет переменчивой."
        a3 = "3 декабря — Прокл. Считалось, если 3 декабря идет снег, то и 3 июня пойдет дождь."
        a4 = "В народе говорили: «Коли до Введения (4 декабря) снег выпадет, то растает, после Введения — ляжет зима». Также считалось, что мороз во Введение — все праздники морозные, тепло — все праздники теплые."
        a5 = "«Пришел Прокоп (5 декабря) — разрыл сугроб, по снегу ступает — дорогу копает». С этого дня устанавливается хороший санный путь."
        a6 = "Если 6 декабря идет мокрый снег и ветер с севера, то 6 июня пойдет дождь и подует северный ветер."
        a7 = "9 декабря — Юрьев день (Георгий Победоносец), Егорий осенний, холодный. Багряная заря в этот день — к ветрам. Ходили слушать и воду в колодцах: если тихая, не волнуется — зима предстоит тихая и теплая, послышится звук — надо ждать сильных вьюг и морозов. Если на Егория осеннего много снега — на Егория весеннего вырастет трава. Юрьев день в берлогах медведь засыпает."
        a8 = "Крестьяне считали, что снег на Парамона (12 депкабря) — быть метелям до Николы (19 декабря). Если на Парамона снег — мороза до Николы не видать. В снегопад белка бегает по земле — он скоро прекратится."
        a9 = "13 декабря — Андрей Первозванный. В этот день ходили к рекам и озерам и вторично слушали воду: тихая — к хорошей зиме, шумная — к стужам и метелям."
        a10 = "15 декабря. Наши предки верили, что если в этот день идет дождь, то он будет продолжаться 47 дней."
        a11 = "17 декабря Варвара. В этот день приглядывались к дымовым трубам: дым тянется к небу — к морозу, к земле без ветра — к ненастью, виснет коромыслом — к оттепели. А вечером смотрели на небо: звездное — к холодам, тусклое — к теплу. На Варвару день ясный — жди мороза. С Варварина дня наступают сильные морозы. Снегирь прилетит — о зиме известит. Трещит Варюха — береги нос и ухо!"
        a12 = "19 декабря — Никольщина. Никольские морозцы не чета введенским. Считалось, что если до этого дня зима была строгой, то в дальнейшем будут долгие оттепели."
        a13 = "В народе говорили: «Коли на Анну (22 декабря) иней на деревьях — будет урожай»."
        a14 = "«На Спиридона (25 декабря) солнце — на лето, зима — на мороз», — гласит поговорка. Этот день считался началом самых сильных холодов и метелей. Крестьяне также утверждали, что если на Спиридона с утра солнечно, то не надо спешить с ранним севом."
        a15 = "26 декабря — Евгений и Евстрат. С этого дня наблюдали за погодой в течение 12 сут, считая, что каждый день покажет погоду определенного месяца следующего года: 26 декабря соответствует январю, 27 — февралю, 28 декабря — марту и т.д."
        a16 = "29 декабря — Агей. Если в этот день сильный мороз, то холода простоят до Крещения (19 января)."
        a17 = "Снегири запели, а сороки прячутся — к вьюге. Воробьи забираются в хворост, а синицы пищат с утра — мороз усилится."
        a18 = "Если появились снегири только в декабре, то можно ожидать лютую зиму."
        a19 = "Бесснежный декабрь – признак сухой весны."
        a20 = "Если декабрь малоснежный, то ожидается засушливое лето."
        a21 = "Сильные снегопады в первых числах декабря предвещают ливни в начале июня."
        a22 = "Гром в декабре – примета лютой зимы."
        a23 = "В декабре северный ветер предвещает приближение морозов."
        a24 = "Частые ветры в декабре – признак теплого марта."
        a25 = "Если декабрь выдался теплым, то зима будет затяжной, а весна будет холодной и поздно наступит."
        a26 = "Если в декабре нет оттепелей с дождями, то лето будет сухим."
        a27 = "Если до 2 декабря с севера прилетели птицы, то наступают ранние холода."
        er = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23,
              a24, a25, a26, a27]
        return random.choice(er)




