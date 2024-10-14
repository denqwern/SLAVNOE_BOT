import sqlite3
import time
import json
import requests
from aiogram import Router, F, types
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from routers.Keyboard import key_selsovet, key_get_start, key_raiispolk, key_social_objects, \
    key_get_raspisaniee, key_get_raspisanie, key_eventt, key_ysha, key_ysh, vlast, key_histt, key_ek, \
    key_soc, key_slb, admin_functions, admin_key_get_start

router = Router()

transport = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Толочин", callback_data="Toloch")],
                                                  [InlineKeyboardButton(text=f"Славное", callback_data="Slavn")],
                                                  [InlineKeyboardButton(text='Залазье', callback_data="Zalaz")]])

transport_toloch = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=f"Славное", callback_data="Slavn")],
                                                         [InlineKeyboardButton(text='Залазье', callback_data="Zalaz")]])

transport_slav = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Толочин", callback_data="Toloch")],
                                                       [InlineKeyboardButton(text='Залазье', callback_data="Zalaz")]])

transport_zalaz = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Толочин", callback_data="Toloch")],
                                                        [InlineKeyboardButton(text=f"Славное", callback_data="Slavn")]])


@router.message(F.text == "AdminPanel")
async def send_naselennyi_punkt(message: types.Message):
    if message.from_user.id == int(2039046861):
        await message.answer(text="Выполнен вход в панель администатора коммуникационной платформы: ",
                             reply_markup=admin_functions())
    else:
        await message.answer(text='Неккоректный ввод данных!')


@router.message(F.text == "Автобусы")
async def punt(message: types.Message):
    await message.answer(text="Выберите остановочный пункт: ", reply_markup=transport)


@router.callback_query(F.data == 'Toloch')
async def toloch(callback: CallbackQuery):
    named_tuple = time.localtime()  # получить struct_time
    time_string_time = time.strftime("%H.%Mч.", named_tuple)
    time_string_date = time.strftime("%d.%m.%Y", named_tuple)

    await callback.message.answer(text=f"\n🕓{time_string_time}\n"
                                       f"📅 {time_string_date}"
                                       f"\n\n"
                                       f"РАСПИСАНИЕ ДВИЖЕНИЯ АВТОБУСОВ ПО МАРШРУТАМ (ОСТАНОВОЧНЫЙ ПУНКТ - ТОЛОЧИН):"
                                       "\n\nТОЛОЧИН-ЗАЛАЗЬЕ:"
                                       "\n07.50ч., 14.45ч. - пятница, воскресенье"
                                       "\n\nТОЛОЧИН-СЛАВНОЕ:"
                                       "\n07.50ч., 14.00ч. - среда", reply_markup=transport_toloch)


@router.callback_query(F.data == 'Slavn')
async def slavn(callback: CallbackQuery):
    named_tuple = time.localtime()  # получить struct_time
    time_string_time = time.strftime("%H.%Mч.", named_tuple)
    time_string_date = time.strftime("%d.%m.%Y", named_tuple)

    await callback.message.answer(text=f"\n🕓 {time_string_time}\n"
                                       f"📅 {time_string_date}"
                                       f"\n\n"
                                       "РАСПИСАНИЕ ДВИЖЕНИЯ АВТОБУСОВ ПО МАРШРУТАМ (ОСТАНОВОЧНЫЙ ПУНКТ - СЛАВНОЕ):"
                                       "\n\n● СЛАВНОЕ-ТОЛОЧИН:"
                                       "\n08.49ч., 16.00ч. - среда"
                                       "\n\n● СЛАВНОЕ-ЗАЛАЗЬЕ:"
                                       "\n08.49ч., 16.10ч. - пятница, воскресенье", reply_markup=transport_slav)


@router.callback_query(F.data == 'Zalaz')
async def Zalaz(callback: CallbackQuery):
    named_tuple = time.localtime()  # получить struct_time
    time_string_time = time.strftime("%H.%Mч.", named_tuple)
    time_string_date = time.strftime("%d.%m.%Y", named_tuple)

    await callback.message.answer(text=f"\n🕓 {time_string_time}\n"
                                       f"📅 {time_string_date}"
                                       f"\n\n"
                                       "РАСПИСАНИЕ ДВИЖЕНИЯ АВТОБУСОВ ПО МАРШРУТУ (ОСТАНОВОЧНЫЙ ПУНКТ - ЗАЛАЗЬЕ):"
                                       "\n\n● ЗАЛАЗЬЕ - СЛАВНОЕ - ТОЛОЧИН:"
                                       "\n09.00ч., 16.20ч. - пятница, воскресенье", reply_markup=transport_zalaz)


home = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="︎✔︎ Авхуты", url='https://telegra.ph/Avhuty-Slapovskij-selskij-sovet-06-30')],
    [InlineKeyboardButton(text='︎︎✔︎ Гута', url='https://telegra.ph/Guta-Slavnovskij-selskij-sovet-06-30')],
    [InlineKeyboardButton(text='︎︎︎✔︎ Загорье', url='https://telegra.ph/Zagore-Slavnovskij-selskij-sovet-06-30')],
    [InlineKeyboardButton(text='✔︎ Залазье', url='https://telegra.ph/Zalaze-Slavnovskij-selskij-sovet-06-30')]])


@router.message(F.text == "Населенные пункты")
async def punt(message: types.Message):
    await message.answer(text="Выберите населенный пункт: ", reply_markup=home)


@router.message(F.text == "Как добраться?")
async def send_kak_dobratsja(message: types.Message):
    await message.answer(text="Автомобиль поезд")


@router.message(F.text == "Маршрут")
async def send_marshryt(message: types.Message):
    await message.answer(text="Маршрут")


@router.message(F.text == "О сельсовете")
async def send_selsovet(message: types.Message):
    photo = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/О сельсовете/slanoe.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo))
    text = '*Славновский сельсовет*'
    text2 = '[*Местный орган власти*](https://telegra.ph/Funkcii-i-zadachi-selsoveta-08-16)'

    await message.answer(text=f"{text} \\- административная единица на территории Толочинского района"
                              " Витебской области Республики Беларусь образованная 20 августа 1924 года\\. Административным центром сельсовета является агрогородок Славное\\."
                              "\n\nТерритория сельсовета расположена в юго\\-западной части Толочинского района и включает"
                              " 24 населенных пункта с численностью более 1600 человек\\."
                              f"\n\n{text2} \\- Славновский сельский исполнительный комитет\\. Юридический адрес \\- агрогородок Славное, ул\\.Советская, д\\. 25\\.",
                         reply_markup=key_selsovet(), parse_mode=ParseMode.MARKDOWN_V2)


@router.message(F.text == "Руководство")
async def send_rukovodstvo(message: types.Message):
    await message.answer(text="*ПРЕДСЕДАТЕЛЬ* \\- Андрей Владимирович\\, кабинет №11 "
                              "\nДни приема\\: 1\\-я среда месяца \\- с 15\\.00ч\\. до 20\\.00ч\\.;"
                              "2\\,3\\,4\\,5 среда месяца с 8\\.00ч\\. до 13\\.00ч\\. "
                              "\n\n*УПРАВЛЯЮЩИЙ ДЕЛАМИ* \\- Ирина Михайловна\\, кабинет №12"
                              "\nДни приема\\: еженедельно с 8\\.00ч\\. до 12\\.00ч\\.;"
                              "по пятницам с 13\\.00ч\\. по 17\\.00ч\\.", parse_mode=ParseMode.MARKDOWN_V2)


@router.message(F.text == "Контактная информация")
async def send_contact_info(message: types.Message):
    await message.answer(text="\n\n*ПРЕДСЕДАТЕЛЬ* \\- 8\\(02136\\)29845"
                              "\n*УПРАВЛЯЮЩИЙ ДЕЛАМИ* \\- 8\\(02136\\)29849"
                              "\n\n📩 Электронный адрес\\: slavnoe@tolochin\\.vitebsk\\-region\\.gov\\.by"
                              "\n\n☎️ Номер горячей линии \\- 8\\(02136\\)29849"
                              "\n📞 Телефон приемной \\- 8\\(02136\\)51533"
                              "\n\n❗Прямая телефонная линия с гражданами и представителями юридических лиц осуществляется председателем Славновского сельского исполнительного комитета каждую 2\\-ю субботу месяца с 09\\.00ч\\. по 12\\.00ч\\. по телефону \\+375297100990",
                         parse_mode=ParseMode.MARKDOWN_V2)


raiisp_one = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Приемная", url='https://telegra.ph/Priemnaya-rajispolkoma-08-18')],
                     [InlineKeyboardButton(text="Структура", callback_data="struct")],
                     [InlineKeyboardButton(text="Одно окно",
                                           url='https://telegra.ph/Obshchaya-informaciya-o-sluzhbe-odno-okno-08-18')],
                     [InlineKeyboardButton(text="Горячая линия", url='https://telegra.ph/Goryachaya-liniya-08-18-2')]])


@router.callback_query(F.data == 'struct')
async def Slavn(callback: CallbackQuery):
    path_one = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/Функции и задачи райисполкома.doc'
    pathe_two = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/Структура райисполкома.doc'
    await callback.message.answer_document(document=types.FSInputFile(path=path_one))
    await callback.message.answer_document(document=types.FSInputFile(path=pathe_two))


@router.message(F.text == "Райисполком")
async def send_raiispolcom(message: types.Message):
    photo1 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/IMG_0774.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo1))
    await message.answer(text="Толочинский районный исполнительный комитет:"
                              "\n\nАдрес: 211092, г. Толочин, ул. Ленина, 1"
                              "\nЕ-mail: odok@tolochin.vitebsk-region.gov.by", reply_markup=key_raiispolk())
    await message.answer(text="Телефон: (802136) 5-15-33", reply_markup=raiisp_one)


sud = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="По уголовным/административным делам", callback_data='ygol')],
                     [InlineKeyboardButton(text="По экономическим делам", callback_data="econom")],
                     [InlineKeyboardButton(text="По делам интеллектуальной собственности", callback_data='int')]])


@router.message(F.text == "Суд")
async def send_raiispolcom(message: types.Message):
    photo1 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/SudTolochin.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo1))
    await message.answer(text="Адрес: 211092 Витебская область, г. Толочин, ул. Энгельса, д.16А"
                              "\nтел./факс 8(02136) 2-14-37"
                              "\ne-mail: tolochin@court.by"
                              "\nтелефон доверия 8 (02136) 2-14-37 (с 29.07.2024 по 22.08.2024)"
                              "\nканцелярия 8 (02136) 2-14-37", reply_markup=key_raiispolk())
    await message.answer(text="\n\n\nПримерные образцы документов для обращения в суд:", reply_markup=sud)


@router.callback_query(F.data == 'ygol')
async def Slavn(callback: CallbackQuery):
    path_one = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/Взыскание алиментов в порядке искового производства(2).doc'
    pathe_two = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/Взыскание алиментов в порядке приказного производства(4).doc'
    pathe_three = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/Взыскание заработной платы.doc'
    pathe_four = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/Жалоба на действия судебного исполнителя(1).docx'
    pathe_five = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/Заявление о возбуждении уголовного дела частного обвинения.docx'
    pathe_six = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/О взыскании долга.doc'
    pathe_seven = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/О восстановлении на работе и оплате за время вынужденного прогула(1).docx'
    pathe_nine = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/О выдаче дубликата исполнительного листа.doc'
    pathe_ten = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/О предоставлении свидания с обвиняемым.docx'
    pathe_nine_1 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/О признании гражданина недееспособным(3).docx'
    pathe_nine_2 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/О признании утратившим право пользования жилым помещением(4).docx'
    pathe_nine_3 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/Об индексации взысканной суммы.doc'
    pathe_nine_4 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/Об установлении факта получения заработной платы за конкретный период в определенном размере(2).docx'
    pathe_nine_5 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/Расторжение брака(2).docx'

    await callback.message.answer_document(document=types.FSInputFile(path=path_one))
    await callback.message.answer_document(document=types.FSInputFile(path=pathe_two))
    await callback.message.answer_document(document=types.FSInputFile(path=pathe_three))
    await callback.message.answer_document(document=types.FSInputFile(path=pathe_four))
    await callback.message.answer_document(document=types.FSInputFile(path=pathe_five))
    await callback.message.answer_document(document=types.FSInputFile(path=pathe_six))
    await callback.message.answer_document(document=types.FSInputFile(path=pathe_seven))
    await callback.message.answer_document(document=types.FSInputFile(path=pathe_nine))
    await callback.message.answer_document(document=types.FSInputFile(path=pathe_ten))
    await callback.message.answer_document(document=types.FSInputFile(path=pathe_nine_1))
    await callback.message.answer_document(document=types.FSInputFile(path=pathe_nine_2))
    await callback.message.answer_document(document=types.FSInputFile(path=pathe_nine_3))
    await callback.message.answer_document(document=types.FSInputFile(path=pathe_nine_4))
    await callback.message.answer_document(document=types.FSInputFile(path=pathe_nine_5))


@router.callback_query(F.data == 'econom')
async def Slavn(callback: CallbackQuery):
    path_1 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Заявление.docx'
    path_2 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Заявление кредитора  о признании должника банкротом (образец).doc'
    path_3 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Заявление на возврат госпошлины (2).doc'
    path_4 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Заявление на составление мотивировочной части.docx'
    path_5 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Заявление о возбуждении приказного производства (3).doc'
    path_6 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Заявление о выдаче дубликата судебного приказа.docx'
    path_7 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Заявление о завершении примирительной процедуры.docx'
    path_8 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Заявление о замене стороны ее правопреемником.docx'
    path_9 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Заявление о предоставлении рассрочки исполнения судебного постановления (1).doc'
    path_10 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Заявление о признании должника банкротом (образец).doc'
    path_11 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Заявление о признании должника несостоятельным  (образец).doc'
    path_12 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Заявление об отказе от заявленных требований (приказное производство).docx'
    path_13 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/заявление об отказе от иска.docx'
    path_14 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Исковое заявление о взыскании долга по договору поставки.docx'
    path_15 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Отзыв на заявление о возбуждении приказного производства.docx'
    path_16 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Претензия  о взыскании задолженности за поставленную продукцию (1).doc'
    path_17 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Расторжение брака(2).docx'
    path_18 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Соглашение о примирении.doc'
    path_19 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Ходатайство о восстановлении пропущенного срока на подачу апкл_жалобы.docx'
    path_20 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Ходатайство о назначении примирителя (1).doc'
    path_21 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/econom/Ходатайство о привлечении третьего лица.docx'

    await callback.message.answer_document(document=types.FSInputFile(path=path_1))
    await callback.message.answer_document(document=types.FSInputFile(path=path_2))
    await callback.message.answer_document(document=types.FSInputFile(path=path_3))
    await callback.message.answer_document(document=types.FSInputFile(path=path_4))
    await callback.message.answer_document(document=types.FSInputFile(path=path_5))
    await callback.message.answer_document(document=types.FSInputFile(path=path_6))
    await callback.message.answer_document(document=types.FSInputFile(path=path_7))
    await callback.message.answer_document(document=types.FSInputFile(path=path_8))
    await callback.message.answer_document(document=types.FSInputFile(path=path_9))
    await callback.message.answer_document(document=types.FSInputFile(path=path_10))
    await callback.message.answer_document(document=types.FSInputFile(path=path_11))
    await callback.message.answer_document(document=types.FSInputFile(path=path_12))
    await callback.message.answer_document(document=types.FSInputFile(path=path_13))
    await callback.message.answer_document(document=types.FSInputFile(path=path_14))
    await callback.message.answer_document(document=types.FSInputFile(path=path_15))
    await callback.message.answer_document(document=types.FSInputFile(path=path_16))
    await callback.message.answer_document(document=types.FSInputFile(path=path_17))
    await callback.message.answer_document(document=types.FSInputFile(path=path_18))
    await callback.message.answer_document(document=types.FSInputFile(path=path_19))
    await callback.message.answer_document(document=types.FSInputFile(path=path_20))
    await callback.message.answer_document(document=types.FSInputFile(path=path_21))


@router.callback_query(F.data == 'int')
async def Slavn(callback: CallbackQuery):
    path = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/intellect/Исковое заявление - 2.docx'
    path_1 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/intellect/Исковое заявление - 3.docx'
    path_2 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/intellect/Исковое заявление  - 1(3).docx'
    path_3 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/intellect/О взыскании вознаграждения, пени и процентов за пользование чужими денежными средствами(2).docx'
    await callback.message.answer_document(document=types.FSInputFile(path=path))
    await callback.message.answer_document(document=types.FSInputFile(path=path_1))
    await callback.message.answer_document(document=types.FSInputFile(path=path_2))
    await callback.message.answer_document(document=types.FSInputFile(path=path_3))


@router.message(F.text == "Режим работы")
async def send_rezhim_raboty(message: types.Message):
    await message.answer(text="\n\n💼 Ежедневно с 8.00ч. до 17.00ч."
                              "\n🔴 Обед с 13.00ч. до 14.00ч."
                              "\n🔴 Выходные дни: суббота, воскресенье")


@router.message(F.text == "Одно окно")
async def send_odno_okno(message: types.Message):
    await message.answer(text='*РЕЖИМ РАБОТЫ "ОДНО ОКНО":*'
                              '\nпонедельник\\, вторник\\, четверг\\, пятница c 8\\.00ч\\. до 18\\.00ч\\.'
                              '\nсреда\\: с 8\\.00ч\\. до 20\\.00ч\\.\\, без перерыва на обед'
                              '\nвыходные дни\\: суббота\\, воскресенье'
                              '\n\n*КОНСУЛЬТИРОВАНИЕ:*'
                              '\nпредварительное консультирование заинтересованных лиц '
                              'по осуществлению административных процедур по заявительному принципу'
                              ' «ОДНО ОКНО» проводит управляющий делами сельского исполнительного '
                              '\\(кабинет №12\\, тел\\. 8\\(02136\\)29849\\)'
                              '\n\nВ период временного отсутствия управляющего делами предварительное консультирование осуществляет Председатель \\(кабинет №11\\, тел\\. 8\\(02136\\)29845\\)\\.',
                         parse_mode=ParseMode.MARKDOWN_V2)


@router.message(F.text == "Назад")
async def send_nazad(message: types.Message):
    if message.from_user.id == int(2039046861):
        await message.answer(f'Главное меню:', reply_markup=admin_key_get_start())
    else:
        await message.answer(text="Главное меню:", reply_markup=key_get_start())


@router.message(F.text == "Социальные объекты")
async def send_social_objects(message: types.Message):
    await message.answer(text="Социальные объекты:", reply_markup=key_social_objects())


@router.message(F.text == "Расписание")
async def send_raspisanie(message: types.Message):
    await message.answer(text="Выберите вид транспорта:", reply_markup=key_get_raspisaniee())


@router.message(F.text == "Электропоезда")
async def send_electropoezda(message: types.Message):
    await message.answer(text="Расписание электропоездов:", reply_markup=key_get_raspisanie())


@router.message(F.text == "Меню")
async def send_menu(message: types.Message):
    await message.answer(text="Главное меню:", reply_markup=key_get_start())


@router.message(F.text == "Ближайшие электропоезда")
async def send_blizhaishie_elekteopoezda(message: types.Message):
    await message.answer(text=f"Выберете направление:", reply_markup=key_eventt())


@router.message(F.text == "Ушедшие электропоезда")
async def event(message: types.Message):
    await message.answer(text="Выберите направление:", reply_markup=key_ysh())


@router.message(F.text == "Расписание на день")
async def send_raspisanie_na_den(message: types.Message):
    await message.answer(text=f"Выберете направление:", reply_markup=key_ysha())


@router.message(F.text == 'Стоимость проезда')
async def send_stoim_proezda(message: types.Message):
    path = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/database/slavnoe_1.db'
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    cur.execute(f'SELECT station, stoim FROM stoimost_minsk_1')
    dff = cur.fetchall()
    a = ""
    for sum in dff:
        a += (f"{sum[0]} \\- {sum[1]}\n")

    await message.answer(text=f'```{a}```', parse_mode=ParseMode.MARKDOWN_V2)
    cur.close()
    connection.close()


def hour_one(finish_one):
    if finish_one == 7 or finish_one == 6 or finish_one == 5:
        hoursee = "часов"
        return hoursee
    if finish_one == 4 or finish_one == 3 or finish_one == 2:
        hoursee = "часа"
        return hoursee

    if finish_one == 1:
        hoursee = "час"
        return hoursee


def word_one(finish_one):
    if finish_one == 7 or finish_one == 6 or finish_one == 5:
        words = "осталось"
        return words

    if finish_one == 4 or finish_one == 3 or finish_one == 2:
        words = "осталось"
        return words

    if finish_one == 1:
        words = "остался"
        return words
    else:
        words = "осталось"
        return words


def minute_one(finish_two):
    if finish_two == 1 or finish_two == 21 or finish_two == 31 or finish_two == 41 or finish_two == 51:
        minuteee = "минута"
        return minuteee

    if finish_two == 2 or finish_two == 3 or finish_two == 4 or finish_two == 22 or finish_two == 23 or finish_two == 24 \
            or finish_two == 32 or finish_two == 33 or finish_two == 34 or finish_two == 42 or finish_two == 43 \
            or finish_two == 44 or finish_two == 53 or finish_two == 52:
        minuteee = "минуты"
        return minuteee

    if finish_two == 0 or finish_two == 5 or finish_two == 6 or finish_two == 7 or finish_two == 8 or finish_two == 9 or finish_two == 11 \
            or finish_two == 12 or finish_two == 13 or finish_two == 14 or finish_two == 15 or finish_two == 16 \
            or finish_two == 17 or finish_two == 18 or finish_two == 19 or finish_two == 20 or finish_two == 25 \
            or finish_two == 26 or finish_two == 27 or finish_two == 28 or finish_two == 29 or finish_two == 30 \
            or finish_two == 35 or finish_two == 36 or finish_two == 37 or finish_two == 38 or finish_two == 39 \
            or finish_two == 40 or finish_two == 45 or finish_two == 46 or finish_two == 47 or finish_two == 48 \
            or finish_two == 49 or finish_two == 50 or finish_two == 54 \
            or finish_two == 55 or finish_two == 56 or finish_two == 57 or finish_two == 58 or finish_two == 59:
        minuteee = "минут"
        return minuteee


@router.message(F.text == "На Борисов, Минск")
async def send_na_borisov_minsk(message: types.Message):
    named_tuple = time.localtime()  # получить struct_time
    time_string = time.strftime("%H:%M часов", named_tuple)
    time_string_2 = time.strftime("%d.%m.%Y", named_tuple)
    time_string_3 = time.strftime("%H%M", named_tuple)
    path = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/database/slavnoe_1.db'
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    n = str()
    for num in time_string_3:
        n += num
    q = n[0] + n[1]
    w = n[2] + n[3]
    result = int(''.join(map(str, q)))
    result_1 = int(''.join(map(str, w)))
    itog_number = result * 60 + result_1
    itog_number = int(itog_number)  # посчитали значение текущего времени в минутах

    cur.execute(f'SELECT time_min FROM raspisanie_minsk_1 WHERE time_min > {itog_number} LIMIT 1')
    vremj = cur.fetchall()
    countt = []

    for num in vremj:
        countt += num
    count_onee = ""
    for num in countt:
        count_onee += str(num)

    if count_onee == "":
        cur.execute(f'SELECT time_graf FROM raspisanie_minsk_1 WHERE id = 1')
        same = cur.fetchall()
        count = []
        for num in same:
            count += num
        do = ""
        for num in count:
            do += str(num)
        b = (f'{time_string}\n'
             f'{time_string_2}\n\n'
             f"На сегодня все поезда ушли. Ближайший поезд отправится от станции Славное завтра в {str(do)} часов.")

    if count_onee != "":
        cur.execute(f'SELECT time_graf, napravl, graf  FROM raspisanie_minsk_1 WHERE time_min > {itog_number} LIMIT 2')
        dff = cur.fetchall()
        a = ""
        count = 0
        for sum in dff:
            count += 1
            a += (f"\n№{count}. Время прибытия: {sum[0]} \n"
                  f"Следование: {sum[1]}\n"
                  f"График: {sum[2]}\n"
                  )

        finish = int(count_onee) - int(itog_number)
        finish_one = finish // 60
        finish_two = finish - (finish_one * 60)

        word = word_one(finish_one)
        minute = minute_one(finish_two)
        hours = hour_one(finish_one)

        b = (f'{time_string}\n'
             f'{time_string_2}\n\n'
             f"До отправления ближайшего электропоезда {word} {finish_one} {hours} {finish_two} {minute}!"
             f"\n\nБЛИЖАЙШИЕ ЭЛЕКТРОПОЕЗДА:"
             f"\n{a}")
        if int(finish_one) < 1:
            b = (f'{time_string}\n'
                 f'{time_string_2}\n\n'
                 f"До отправления ближайшего электропоезда {word} {finish_two} {minute}!"
                 f"\n{a}")

    await message.answer(text=f'{b}')

    cur.close()
    connection.close()


@router.message(F.text == "На Оршу")
async def send_na_orshy(message: types.Message):
    named_tuple = time.localtime()  # получить struct_time
    time_string = time.strftime("%H:%M часов", named_tuple)
    time_string_2 = time.strftime("%d.%m.%Y", named_tuple)
    time_string_3 = time.strftime("%H%M", named_tuple)
    path = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/database/slavnoe_1.db'
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    n = str()
    for num in time_string_3:
        n += num
    q = n[0] + n[1]
    w = n[2] + n[3]
    result = int(''.join(map(str, q)))
    result_1 = int(''.join(map(str, w)))
    itog_number = result * 60 + result_1
    itog_number = int(itog_number)

    cur.execute(f'SELECT time_min FROM raspisanie_orsha_1 WHERE time_min > {itog_number} LIMIT 1')
    vremj = cur.fetchall()
    countt = []

    for num in vremj:
        countt += num
    count_onee = ""
    for num in countt:
        count_onee += str(num)

    if count_onee == "":
        cur.execute(f'SELECT time_graf FROM raspisanie_orsha_1 WHERE id = 1')
        same = cur.fetchall()
        count = []
        for num in same:
            count += num
        do = ""
        for num in count:
            do += str(num)
        b = (f'{time_string}\n'
             f'{time_string_2}\n\n'
             f"На сегодня все поезда ушли. Ближайший поезд отправится от станции Славное завтра в {str(do)} часов.")

    if count_onee != "":
        cur.execute(f'SELECT time_graf, napravl, graf  FROM raspisanie_orsha_1 WHERE time_min > {itog_number} LIMIT 2')
        dff = cur.fetchall()
        a = ""
        count = 0
        for sum in dff:
            count += 1
            a += (f"\n\n№{count}. Время прибытия: {sum[0]} \n"
                  f"Следование: {sum[1]}\n"
                  f"График: {sum[2]}\n"
                  )

        finish = int(count_onee) - int(itog_number)
        finish_one = finish // 60
        finish_two = finish - (finish_one * 60)

        word = word_one(finish_one)
        minute = minute_one(finish_two)
        hours = hour_one(finish_one)

        b = (f'{time_string}\n'
             f'{time_string_2}\n\n'
             f"До отправления ближайшего электропоезда {word} {finish_one} {hours} {finish_two} {minute}!"
             f"\n\nБЛИЖАЙШИЕ ЭЛЕКТРОПОЕЗДА:"
             f"{a}")
        if int(finish_one) < 1:
            b = (f'{time_string}\n'
                 f'{time_string_2}\n\n'
                 f"До отправления ближайшего электропоезда {word} {finish_two} {minute}!"
                 f"\n\nБЛИЖАЙШИЕ ЭЛЕКТРОПОЕЗДА:"
                 f"{a}")

    await message.answer(text=f'{b}')

    cur.close()
    connection.close()


@router.message(F.text == "На Борисов, Минск🌃")
async def send_na_borisov_minsk_pic(message: types.Message):
    named_tuple = time.localtime()  # получить struct_time
    time_string = time.strftime("%H:%M часов", named_tuple)
    time_string_2 = time.strftime("%d.%m.%Y", named_tuple)
    time_string_3 = time.strftime("%H%M", named_tuple)
    path = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/database/slavnoe_1.db'
    connection = sqlite3.connect(path)
    n = str()

    for num in time_string_3:
        n += num

    q = n[0] + n[1]
    w = n[2] + n[3]
    result = int(''.join(map(str, q)))
    result_1 = int(''.join(map(str, w)))

    cur = connection.cursor()
    cur.execute(f'SELECT time_graf, napravl, graf  FROM raspisanie_minsk_1')
    dff = cur.fetchall()
    a = ""
    count = 0
    for sum in dff:
        count += 1
        a += (f"№{count}. Время прибытия: {sum[0]} \n"
              f"Следование: {sum[1]}\n"
              f"График: {sum[2]}\n"
              f"\n")

    await message.answer(text=f'{time_string}'
                              f'\n{time_string_2}'
                              f'\n\nРАСПИСАНИЕ НА ДЕНЬ:'
                              f'\n\n{a}')
    cur.close()
    connection.close()


@router.message(F.text == "На Оршу🌁️")
async def send_na_orshy_pic(message: types.Message):
    named_tuple = time.localtime()  # получить struct_time
    time_string = time.strftime("%H:%M часов", named_tuple)
    time_string_2 = time.strftime("%d.%m.%Y", named_tuple)
    time_string_3 = time.strftime("%H%M", named_tuple)
    path = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/database/slavnoe_1.db'
    connection = sqlite3.connect(path)
    n = str()

    for num in time_string_3:
        n += num

    cur = connection.cursor()
    cur.execute(f'SELECT time_graf, napravl, graf  FROM raspisanie_orsha_1')
    dff = cur.fetchall()
    a = ""
    count = 0
    for sum in dff:
        count += 1
        a += (f"№{count}. Время прибытия: {sum[0]} \n"
              f"Следование: {sum[1]}\n"
              f"График: {sum[2]}\n"
              f"\n")

    await message.answer(text=f'{time_string}'
                              f'\n{time_string_2}'
                              f'\n\nРАСПИСАНИЕ НА ДЕНЬ:'
                              f'\n\n{a}')
    cur.close()
    connection.close()


@router.message(F.text == "Амбулатория")
async def send_ambulatoria(message: types.Message):
    photo_2 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/Амбулатория/ambulatoria.jpeg'
    await message.answer_photo(photo=types.FSInputFile(path=photo_2))
    await message.answer(text="*СЛАВНОВСКАЯ СЕЛЬСКАЯ ВРАЧЕБНАЯ АМБУЛАТОРИЯ:*"
                              "\n\n*Адрес:* агрогородок Славное\\, улица Толочинская\\, 47"
                              "\n*Режим работы:* с 08\\.00ч\\. до 15\\.00ч\\. \\- прием; c 12\\.00ч\\. до 12\\.30ч\\.\\- обед\\; c 15\\.00ч\\. до 17\\.00ч\\.\\- работа на участке"
                              "\n*Телефон:* 8\\(02136\\)35443", parse_mode=ParseMode.MARKDOWN_V2)


@router.message(F.text == "Магазины")
async def send_magazine(message: types.Message):
    photo = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/Магазины/mag_zhd.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo))

    await message.answer(text="❶ *МАГАЗИН ДОРОРС \\(железнодорожный\\):*"
                              "\n\n*АДРЕС:* агрогородок Славное\\, улица Железнодорожная\\, 13А"
                              "\n*ТЕЛЕФОН:* 8\\(02136\\)29881"
                              "\n\n*РЕЖИМ РАБОТЫ:* с 10\\.00ч\\. до 18\\.30ч\\. \\- ежедневно",
                         parse_mode=ParseMode.MARKDOWN_V2)
    photo_2 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/Магазины/mag_belkoop.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo_2))
    await message.answer(text="❷ *МАГАЗИН БЕЛКОПСОЮЗ:*"
                              "\n\n*АДРЕС:* агрогородок Славное\\, улица Железнодорожная"
                              "\n*ТЕЛЕФОН:* 8\\(02136\\)29881"
                              "\n\n*РЕЖИМ РАБОТЫ:* с 09\\.00ч\\. до 19\\.00ч\\. \\- ежедневно",
                         parse_mode=ParseMode.MARKDOWN_V2)

    photo_3 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/Магазины/mag_tabakerka.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo_3))
    await message.answer(text="❸ *ТАБАКЕРКА:*"
                              "\n\n*АДРЕС:* агрогородок Славное\\, улица Железнодорожная",
                         parse_mode=ParseMode.MARKDOWN_V2)

    photo_4 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/Магазины/mag_pavilion.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo_4))
    await message.answer(text="❹ *ТОРГОВЫЙ ПАВИЛЬОН СЛАВНОЕ:*"
                              "\n\n*АДРЕС:* агрогородок Славное\\, улица Железнодорожная"
                              "\n*РЕЖИМ РАБОТЫ*\\: вторник \\- пятница с 09\\.00ч\\. по 19\\.00ч\\.\\; суббота с 09\\.00ч\\. по 15\\.00ч\\.\\; выходные дни\\: воскресенье\\, понедельник",
                         parse_mode=ParseMode.MARKDOWN_V2)


@router.message(F.text == "Детский сад")
async def send_denskiy_sad(message: types.Message):
    photo1 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/Детский сад/detski_sad.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo1))
    await message.answer(text="*ГУО СЛАВНОВСКИЙ ДЕТСКИЙ САД:*"
                              "\n\n*АДРЕС:* агрогородок Славное\\, улица Молодежная\\, 3"
                              "\n*ЗАВЕДУЮЩИЙ:* Татьяна Геннадьевна"
                              "\n*ТЕЛЕФОН:* 8\\(02136\\)29825", parse_mode=ParseMode.MARKDOWN_V2)


@router.message(F.text == "БелПочта")
async def send_belpost(message: types.Message):
    photo = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/Белпочта/belpochta.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo))

    await message.answer(text=f"*ОТДЕЛЕНИЕ ПОЧТОВОЙ СВЯЗИ СЛАВНОЕ:*"
                              "\n*ИНДЕКС:* 211090"
                              "\n*АДРЕС:* агрогородок Славное\\, улица Советская\\, 2"
                              "\n*ТЕЛЕФОН:* 8\\(02136\\)57938"
                              f"\n\n*РЕЖИМ РАБОТЫ:*"
                              "\nПонедельник: выходной"
                              "\nВторник: 09\\.00\\-14\\.45\\, Обед: 13\\.30 \\- 14\\.00"
                              "\nСреда: 10\\.00\\-15\\.45\\, Обед: 13\\.30 \\- 14\\.00"
                              "\nЧетверг\\-суббота: 09\\.00\\-14\\.45\\, Обед: 13\\.30 \\- 14\\.00"
                              "\nВоскресенье: выходной"
                              "\nПраздничные дни: выходной", parse_mode=ParseMode.MARKDOWN_V2)

    photo1 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/Белпочта/belpochta_fasad.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo1))
    text = " УСЛУГИ:"
    entity_bold = types.MessageEntity(type="bold",
                                      offset=len(" "),
                                      length=9, )
    entities = [entity_bold]
    await message.answer(text=f"{text}"
                              "\n● доставка;"
                              "\n● выдача БПК ОАО АСБ Беларусбанк;"
                              "\n● выдача наличных денег по БПК ОАО АСБ Беларусбанк;"
                              "\n● отправление По пути;"
                              "\n● пополнение БПК ОАО АСБ Беларусбанк;"
                              "\n● вклады, кредиты БПК ОАО АСБ Беларусбанк;"
                              "\n● письменная корреспонденция;"
                              "\n● прием телеграмм;"
                              "\n● почтовые денежные переводы;"
                              "\n● выплата пенсий и пособий;"
                              "\n● прием платежей;"
                              "\n● страхование;"
                              "\n● подписка на печатные СМИ;"
                              "\n● отправление ускоренной почты;"
                              "\n● посылки весом до 10кг.", entities=entities)


@router.message(F.text == "Клуб")
async def send_klub(message: types.Message):
    photo_2 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/Клуб/klub_slavnoe.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo_2))
    await message.answer(
        text="*Филиал Славновский сельский Дом культуры ГУК Толочинский районный центр культуры и народного творчества: *"
             "\n\n*АДРЕС:* агрогородок Славное\\, улица Советская\\, 25А"
             "\n\n*РЕЖИМ РАБОТЫ:* "
             "\nВТОРНИК \\- c 15\\.00ч\\. по 20\\.00ч\\.;"
             "\nСРЕДА \\- ПЯТНИЦА, ВОСКРЕСЕНЬЕ \\- c 12\\.00ч\\. по 20\\.00ч\\.; "
             "\nСУББОТА \\- c 15\\.00ч\\. по 23\\.00ч\\.; "
             "\nВЫХОДНОЙ \\- ПОНЕДЕЛЬНИК", parse_mode=ParseMode.MARKDOWN_V2)


@router.message(F.text == "Библиотека")
async def send_biblioteka(message: types.Message):
    photo_2 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/Библиотека/biblioteka.jpeg'
    await message.answer_photo(photo=types.FSInputFile(path=photo_2))
    await message.answer(text="*Славновская сельская библиотека Филиал №22: *"
                              "\n\n*Адрес:* агрогородок Славное\\, улица Советская\\, 25А"
                              "\n*Режим работы:* "
                              "\nвторник \\- суббота\\: 11\\.00\\-18\\.00\\; воскресенье\\: 11\\.00\\-17\\.00\\, обед с 14\\.00\\-15\\.00"

                              "\n\nТелефон\\: 8\\(02136\\)29880"
                              "\nemail\\: slavnoe\\.bibl22\\@yandex\\.by", parse_mode=ParseMode.MARKDOWN_V2)


@router.message(F.text == "Население")
async def send_naselenie(message: types.Message):
    photo = '/Users/user/Downloads/Новая папка (2)/nas.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo))
    await message.answer(
        text="*Толочинский район был образован 17 июля 1924 года*\\. Граничит на востоке с Оршанским\\, на севере с Чашникским и Сенненским районами Витебской\\, на юге со Шкловским и Круглянским районами Могилевской области\\, на западе – с Крупским районом Минской области\\. По территории района проходят автотрасса Брест\\-Минск\\-граница Российской Федерации\\, железная дорога того же направления\\. В составе района 7 сельских Советов\\. Населенных пунктов 262\\. Население Толочинского района составляет 22 745 человека \\(на 1 января 2022 года\\)\\. В сельской местности проживает 9 158 человек\\. Городское население г\\.Толочин \\- 9 823 человека\\, г\\.п\\.Коханово \\- 3 764 человека\\.",
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=key_raiispolk())


@router.message(F.text == "Власть")
async def village(message: types.Message):
    await message.answer(text="Районная власть: ", reply_markup=vlast())


@router.message(F.text == "Службы")
async def send_sluzhby(message: types.Message):
    await message.answer(text="Службы и структурные подразделения:", reply_markup=key_slb())


@router.message(F.text == "Социальная сфера")
async def send_social_objects(message: types.Message):
    await message.answer(text="Объекты социальной сферы:", reply_markup=key_soc())


@router.message(F.text == "Экономика")
async def send_economika(message: types.Message):
    await message.answer(text="Районный исполнительный комитет:", reply_markup=key_ek())


@router.message(F.text == "История")
async def send_hist(message: types.Message):
    await message.answer(
        text="Толочинщину с полным основанием можно назвать тихим краем лесов и рек, но это впечатление обманчиво. Бурные события истории никогда не проходили мимо нашего района. "
             "\n\nТерритория Толочинского района была заселена в эпоху мезолита (среднего каменного века) примерно в 9-ом тыс. до н. э. На ее территории проживали племена верхнеднепровской, нарвенской, северобелорусской, днепродвинской, банцеровской  культуры. Поселения этих культур были найдены около дд. Уголевщина, Заречье, Шашеловка, Багриново и др. "
             "\n\nТак, что история земель, входящих сегодня в состав района уходит корнями в глубокую древность. Первые летописные упоминания о населенных пунктах нашего района относятся к 11-12 векам. В древних летописях называется 10 городов западных земель Руси, в т.ч. город Друцк, тысячелетие, которого отмечалось в 2001 году. Друцк являлся в 10-13 веках южной границей Полоцкого княжества. "
             "\n\nГород Друцк был важным пунктом на торговом пути из «варяг в греки», который проходил через  территорию нашего района. "
             "\n\nВ 1001 году в Друцке была построена одна из первых православных церквей на территории современной Беларуси –  Пресвятой Богородицы. "
             "\n\nКнязья Друцкие занимали важное положение в Полоцком княжестве, а затем в Великом княжестве Литовском. Родом из князей Друцких была Софья Друцкая (Гольшанская), жена Великого князя Литовского и короля Польского Ягайлы (Владислава). "
             "\n\nЦентр района – город Толочин, упоминается в летописи в 1433 году как местечко в составе Великого княжества Литовского. Город принадлежал Друцким князьям и их наследникам, с начала 17-го века – канцлеру ВКЛ Льву Сапеге. Он в 1604 году основал здесь деревянный костел, который был перестроен и в 1804 году преобразован в православную Свято-Покровскую церковь. Сейчас это Свято-Покровский женский монастырь. "
             "\n\nВ результате 1-го раздела Речи Посполитой (1772) восточная часть Толочина вошла в состав Российской империи (с 1782 имел статус города, с 1783 – местечка) и стал называться Старый или Русский Толочин (пограничный таможенный пункт). А западная, что находилась на реке Друть - Заречный или Новый Толочин, до 1793г. входила в состав Речи Посполитой. "
             "\n\nВ ноябре 1812 года во время Отечественной войны в Толочине останавливался император Франции  - Наполеон. Здание, где он находился, сохранилось и по сей день. "
             "\n\nСтарый Толочин – центр Старотолочинской волости Копыльского , с 1861г. – Оршанского уездов. Новый Толочин – центр Заречнотолочинской волости Сенненского уезда Могилевской губернии.")
    await message.answer(
        text="В 1897 г. в местечке Толочин проживало 2614 жителей. В начале 20 века в Толочине работали 2 кожевенных, кирпичный, пивоваренный заводы, мельница, школа, 2 народных училища."
             "\n\nПосле Октябрьской революции в ноябре 1917 года в Толочине был создан местечковый Совет. В него входило 1008 солдат и 600 рабочих. "
             "\n\n18 февраля 1918 года кайзеровская Германия, нарушив условия перемирья, начали наступление на всем фронте против молодого Советского государства. "
             "\n\nОккупированными оказались Толочин, Старотолочинская, Кохановская волости и другие территории современной Толочинщины. Оккупация продлилась около 8 месяцев. 25 октября г. Толочин был освобожден частями Красной Армии. Была восстановлена советская власть. "
             "\n\nПервые социалистические преобразования в сельском хозяйстве начались в 1919 -20 гг. На Толочинщине  были созданы совхоз «Райцы», коммуны в поместьях Багриново, Озерцы и др. "
             "\n\nС 1920 г. Толочин находится в составе Витебской губернии РСФСР. С 17 июля 1924 г.Толочин – центр района в составе Оршанского округа, с 1938 г. – в Витебской области. С 22 июня 1955 года присвоен статус города. "
             "\n\nМирная жизнь района закончилась 22 июня 1941 года. Уже через две недели начались ожесточенные бои за Толочин. Гитлеровцам противостояла 1-я Московская дивизия. Бои продолжались три дня. Понеся большие потери, фашисты захватили город. Но толочинцы не сдались на милость захватчикам. "
             "\n\nВо время Великой Отечественной войны более 10 тысяч толочинцев защищали честь и независимость Родины на фронте. На территории района в разное время действовали 12 партизанских бригад,  других формирований. Наиболее крупными среди них были бригады М.П. Гудкова, «Гроза». Временно дислоцировались здесь 1-я бригада имени К.С. Заслонова, 8-я Круглянская бригада, 2-я Белорусская бригада имени П.Н. Пономаренко. Два из девяти партизанских генералов И.М.Кордович и И.П.Кожар – уроженцы Толочинщины. "
             "\n\nОсвобожден Толочин был 26 июня 1944 года силами 5-й гвардейской танковой армии под командованием маршала бронетанковых войск П.А. Ротмистрова. "
             "\n\nЗа годы войны район понес большие потери. Во время оккупации в Толочине и  районе погибло 9 521 человек, 2,5 тысячи были угнаны в фашистское рабство. На фронтах Великой Отечественной войны погибло более 4,3 тысячи толочинцев, в партизанских отрядах и подполье – около 580 человек. "
             "\n\nТолочинцы продолжают созидательную эстафету своих предков, и мы просто обязаны собственным умом, трудом и энтузиазмом вписать новую страницу в историю родного края, не забывая при этом своих корней и традиций.",
        reply_markup=key_histt())


@router.message(F.text == "Геральдика")
async def village(message: types.Message):
    await message.answer(
        text="Толочин впервые упоминается в 1433 г\\. как город Великого княжества Литовского\\, который принадлежал князьям Друцким\\. Родоначальник князей Толочинских являтся князь Михаил Толочинский\\, сын князя Ивана Семеновича Друцкого\\-Путяты \\(1380\\-1440\\)\\. Все князья Друцкие использовали единый герб «Друцк»\\."
             "\n\nПосле продолжительной борьбы православная аристократия в 1433 году получила право пользоваться родовыми гербами\\, и именно тогда князья Друцкие приобрели свой собственный герб под названиям «Друцк»\\. Он представлял собой «испанский» щит\\, на котором изображен серебряный меч рукояткой вверх на красном поле\\. По сторонам от лезвия меча – четыре золотых полумесяца\\."
             "\n\n4 октября 1634 г\\. Толочин вместе с городами Бешенковичи\\, Белыничи получил Магдебургское право\\, а значит и герб\\, но его изображение неизвестно\\. Возможно\\, герб Толочина\\, как в ряде других городов\\, представлял собой полностью или частью герб владельцев города\\, а значит князей Друцких\\."
             "\n\n*Герб* города Толочина и Толочинского района создан на основе частновладельческого герба князей Толочинских\\-Друцких\\, учрежден Геральдическим советом при Президенте Республики Беларусь в 2002 году\\, является символом исторической преемственности поколений людей\\, населяющих земли Толочинского района более 1000 лет\\.",
        parse_mode=ParseMode.MARKDOWN_V2)
    photo1 = '/Users/user/Downloads/Новая папка (2)/gb1.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo1))
    await message.answer(
        text="*Флаг* представляет собой прямоугольное полотнище красного цвета с соотношением сторон 1\\:2\\, в центре лицевой стороны которого размещено изображение герба города Толочина и Толочинского района\\. Утвержден Указом Президента Республики Беларусь от 28 февраля 2011 года № 86\\.",
        parse_mode=ParseMode.MARKDOWN_V2)


API = '239cee0024050686ff009bb45541c0fa'


@router.message(F.text == "Погода")
async def handle_weather(message: types.Message):
    trn = requests.get(f'api.openweathermap.org/data/2.5/forecast?lat=54.4329&lon=29.2779&appid={API}')
    data = json.loads(trn.text)

    await message.answer(text=f"\n{data[1]}")


raiisp = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="︎История", url='https://telegra.ph/Istoriya-rajona-08-16')],
                     [InlineKeyboardButton(text="Геральдика", url='https://telegra.ph/Geraldika-rajona-08-16')],
                     [InlineKeyboardButton(text="Наследие",
                                           url='https://telegra.ph/Istoriko-kulturnoe-nasledie-08-17')]])


@router.message(F.text == "География и население")
async def send_raiispolcom(message: types.Message):
    photo1 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/tolochin-s-vysoty_5.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo1))
    await message.answer(
        text="Толочинский район был образован 17 июля 1924 года.\n\nГраничит на востоке с Оршанским, на севере с Чашникским и Сенненским районами Витебской, на юге со Шкловским и Круглянским районами Могилевской области, на западе – с Крупским районом Минской области.\n\nПо территории района проходят автотрасса Брест-Минск-граница Российской Федерации, железная дорога того же направления.\n\nВ составе района 7 сельских Советов. Населенных пунктов 260.\n\nНаселение Толочинского района составляет 21 800 человека (на 1 января 2024 года). В сельской местности проживает 8 407 человек. Городское население г.Толочин - 9 666 человека, г.п.Коханово - 3 727 человека.",
        reply_markup=raiisp)


zags = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="График работы", url='https://telegra.ph/Rezhim-raboty-ZAGS-08-18')],
                     [InlineKeyboardButton(text="Грифик приема",
                                           url='https://telegra.ph/Grafik-priyoma-zainteresovannyh-lic-po-osushchestvleniyu-administrativnyh-procedur-08-18')],
                     [InlineKeyboardButton(text="Формы заявлений", callback_data='avtr')]])


@router.message(F.text == "Отдел ЗАГС")
async def send_raiispolcom(message: types.Message):
    photo1 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/загс/iаа.jpeg'
    await message.answer_photo(photo=types.FSInputFile(path=photo1))
    await message.answer(text="Отдел ЗАГС Толочинского районного исполнительного комитета:"
                              "\n\nАдрес: 211092, г. Толочин, ул. Ленина, д.1"
                              "\nтелефон: 8(02136)5-12-74, ", reply_markup=key_slb())
    await message.answer(text="телефон «горячей линии» 8(02136)5-12-74", reply_markup=zags)

    @router.callback_query(F.data == 'avtr')
    async def Slavn(callback: CallbackQuery):
        path_one = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/загс/Dopolnitelnye-platnye-uslugi,-okazyvaemye-otdelom-zags-.doc'
        pathe_two = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/загс/itogi-raboti-za-2022-1.docx'
        pathe_three = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/загс/Oplata-2024.doc'
        pathe_four = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/загс/Porjadok-obzhalovanija-administrativnyx-reshenij-1.doc'

        await callback.message.answer_document(document=types.FSInputFile(path=path_one))
        await callback.message.answer_document(document=types.FSInputFile(path=pathe_two))
        await callback.message.answer_document(document=types.FSInputFile(path=pathe_three))
        await callback.message.answer_document(document=types.FSInputFile(path=pathe_four))


@router.message(F.text == "РОВД")
async def send_raiispolcom(message: types.Message):
    photo1 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/ровд/XXXL.jpeg'
    await message.answer_photo(photo=types.FSInputFile(path=photo1))
    await message.answer(text="Адрес: 211092 ул. Ленина, 35, г.Толочин, Витебская область"
                              "\n\nЭлектронный адрес:rovd_tolochin@mvd.gov.by"
                              "\nтелефон: 8(02136)5-12-74"
                              "\n\nРежим работы РОВД: с 09:00 до 18:00 (обед с 13:00 до 14:00), суббота и воскресенье – выходной. Оперативно-дежурная служба – круглосуточно (тел. 102, 2-11-06, +375293140002, +375295970213).",
                         reply_markup=key_slb())


@router.message(F.text == "РОЧС")
async def send_raiispolcom(message: types.Message):
    photo1 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/ровд/kak-za-kamennoy-stenoy.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo1))
    await message.answer(text="Толочинский районный отдел по чрезвычайным ситуациям"
                              "\n\nул. Ленина, 89, 211092, г. Толочин, Витебская область"
                              "\nтелефон: 8-02136-5-81-01 факс: 8-02136-5-81-01"
                              "\n\nЛичный приём в Толочинском районном отделе по чрезвычайным ситуациям проводится по адресу: г.Толочин, ул.Ленина,89."
                              "\n\nПредварительная запись на личный приём к начальнику отдела и его заместителям производится в приёмной начальника отдела или по телефону (802136) 2-92-25 в рабочие дни с 8-00 до 13-00 и с 14-00 до 17-00."
                              "\n\nВ выходные и праздничные дни приём проводится ответственным лицом по отделу с 9-00 до 13-00.",
                         reply_markup=key_slb())


@router.message(F.text == "ОПИ")
async def send_raiispolcom(message: types.Message):
    photo1 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/ровд/1032532709_4-0-1915-1080_2072x0_60_0_0_bdad083478d0256f0968c33fca54ae64.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo1))
    await message.answer(
        text="Отдел принудительного исполнения Толочинского района управления принудительного исполнения главного управления юстиции Витебского областного исполнительного комитета"
             "\n\n211092, г. Толочин, ул. Гоголя, 69. "
             "\nНачальник отдела - тел. 8 (02136) 5-21-22"
             "\nКанцелярия: тел. 8 (02136) 5-15-43"
             "\n\nТелефон горячей линии: 8 (02136) 5 15 37, с 9.00 до 18.00."
             "\n\nРежим работы: понедельник, вторник, среда, четверг, пятница  с 9.00 до 18.00, обед с 13.00 до 14.00. Выходной: суббота,  воскресенье. "
             "\n\nБанковские реквизиты: р/с BY68AKBB36429030098962200000, код банка AKBBBY2X, Г.МИНСК, ОАО АСБ БЕЛАРУСБАНК, УНП 300002505",
        reply_markup=key_slb())


@router.message(F.text == "Отдел землеустройства")
async def send_raiispolcom(message: types.Message):
    await message.answer(text="Отдел землеустройства Толочинского районного исполнительного комитета"
                              "\n\nАдрес: 211092, Витебская обл., г. Толочин, ул. Ленина, 1, каб.№70"
                              "\nЭлектронная почта: zem@tolochin.vitebsk-region.gov.by"
                              "\n(факс): 8-02136-5-31-95"
                              "\n\nРежим работы: понедельник-пятница с 8.00 до 18.00"
                              "\nсуббота с 9.00 до 15.00 (дежурство)"
                              "\nВыходной день: воскресенье."
                              "\n\nПриемный день: Среда 8.00–14.00"
                              "\nАдрес: г. Толочин, ул. Ленина, каб. № 70"
                              "\nКонтактный телефон: 8-02136-5-31-95."
                              "\n\nГРАФИК ПРИЕМАФИЗИЧЕСКИХ И ЮРИДИЧЕСКИХ ЛИЦ ПО ВОПРОСАМ ОФОРМЛЕНИЯ ПРАВОУДОСТОВЕРЯЮЩИХ ДОКУМЕНТОВ НА ЗЕМЕЛЬНЫЕ УЧАСТКИ В НАСЕЛЕННЫХ ПУНКТАХ ТОЛОЧИНСКОГО РАЙОНАСПЕЦИАЛИСТАМИ ОТДЕЛА ЗЕМЛЕУСТРОЙСТВА ТОЛОЧИНСКОГО РАЙИСПОЛКОМА:"
                              "\n\nСлавновский сельсовет:"
                              "\nЛатушкина Ольга Владимировна"
                              "\n2-ая среда с 8-00 до 14-00"
                              "\nтелефон: 2-98-49", reply_markup=key_slb())


prokur = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Общая информация", url='https://telegra.ph/Obshchaya-informaciya-08-18-2')],
    [InlineKeyboardButton(text="Историческая справка", url='https://telegra.ph/Osnovy-i-korni-glubokoj-istorii-08-18')],
    [InlineKeyboardButton(text="График приема", url='https://telegra.ph/GRAFIK-PRIYOMA-GRAZHDAN-08-18')]])


@router.message(F.text == "Прокуратура")
async def send_raiispolcom(message: types.Message):
    photo1 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/ровд/3-plakat-3x6-100-let.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo1))
    await message.answer(
        text="Прокуратура Толочинского района входит в единую и централизованную систему органов прокуратуры Республики Беларусь."
             "\n\nАдминистративное здание прокуратуры расположено по адресу:"
             "\n ул. Энгельса, 9а, 211092, г. Толочин", reply_markup=key_slb())
    await message.answer(text="тел. (8-02136) 5-18-18, факс 5-10-92.", reply_markup=prokur)


@router.message(F.text == "РОСК")
async def send_raiispolcom(message: types.Message):
    photo1 = '/Users/dzianis/PycharmProjects/SLV_BOT/routers/pic/raiispolk/ровд/1013397345_0-0-2720-1530_2072x0_60_0_0_002c7d57178c0b27fb86dd97c5e8095d.jpg'
    await message.answer_photo(photo=types.FSInputFile(path=photo1))
    await message.answer(text="ТОЛОЧИНСКИЙ РАЙОННЫЙ ОТДЕЛ СЛЕДСТВЕННОГО КОМИТЕТА РЕСПУБЛИКИ БЕЛАРУСЬ"
                              "\n\nАдрес: 211092, Витебская область, г.Толочин, ул.Ленина, 35, тел/факс 8(02136) 2-21-38 "
                              "\ne-mail: tol_vt@sledcom.by (кроме обращений граждан и юридических лиц)"
                              "\n\nРежим работы:"
                              "\nПонедельник-пятница: с 9.00 до 18 часов"
                              "\nПерерыв на обед: ежедневно с 13.00 до 14.00 часов"
                              "\nВыходной: суббота, воскресенье", reply_markup=key_slb())


@router.message(F.text == "Нотариальная контора")
async def send_raiispolcom(message: types.Message):
    await message.answer(text="НОТАРИАЛЬНАЯ КОНТОРА ТОЛОЧИНСКОГО РАЙОНА"
                              "\n\nАдрес: 211092, г.Толочин, пер. Ленина, д. 3"
                              "\nТелефон для предварительной записи: 8 (02136)5-10-31; 5-17-11"
                              "\nE-mail: tolochin@vtb.belnotary.by"
                              "\n\nРежим работы:"
                              "\nвт.: с 8.00 до 17.00"
                              "\nср.: с 8.00 до 19.00"
                              "\nчт., пт.: с 8.00 до 17.00"
                              "\nперерыв с13.00 до 14.00"
                              "\nсб.: с 8.00 до 14.00, без перерыва"
                              "\nпн., вс.: выходной день"
                              "\n\nВо исполнение подпункта 1.2 пункта 1 постановления Совета Министров Республики Беларусь от 16 мая 2014 г. №107 «О некоторых вопросах выезда нотариуса в агрогородки, малые и средние городские поселения» и в соответствии с приказом председателя Витебской областной нотариальной палаты, для осуществления нотариального обслуживания сельского населения, юридических лиц и индивидуальных предпринимателей, осуществляющих деятельность в сельской местности, закреплены за нотариальной конторой Толочинского районаследующиеагрогородки, малые и средние городские поселения:"
                              "\n\nВоронцевичи, Горщевщина, Друцк, Жукнево, Заднево, Звенячи, г.п. Коханово, Низкий Городец, Обольцы, Озерцы, Райцы, Серковицы, Славени, Славное."
                              "\n\nНотариус выезжает в агрогородки и иные населенные пункты по графику выездов при поступлении не менее одной заявки на совершение нотариального действия и (или) оказание услуги правового и технического характера от заинтересованных лиц, поступившей в нотариальную контору."
                              "\n\nПодать заявку на выезд нотариуса в агрогородок для совершения нотариального действия и (или) оказания услуги правового и технического характера можно в устной или письменной форме. Направить заявку можно, в том числе электронным способом. Заявки принимаются не позднее рабочего дня (в соответствии с утверждённым режимом работы нотариальной конторы), предшествующего дате выезда согласно графика."
                              "\n\nНотариус выезжает в агрогородки и иные населённые пункты вне графика выездов в случае поступления на дату, не предусмотренную графиком выездов, заявки от ветерана Великой Отечественной войны или лица с нарушением функций опорно-двигательного аппарата."
                              "\n\nНа прием к нотариусу в агрогородках можно записаться в нотариальной конторе Толочинского района по телефонам: 5-10-31; 5-17-11; Viber: +375296848137. На сайте Белорусской нотариальной палаты имеется возможность подачи заявки на выезд нотариуса в агрогородки электронным способом.",
                         reply_markup=key_slb())
