from aiogram import Router
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

router = Router()

def key_get_start():
    button = KeyboardButton(text="О сельсовете")
    button_1 = KeyboardButton(text="Галерея")
    button_2 = KeyboardButton(text="Социальные объекты")

    button_7 = KeyboardButton(text="Населенные пункты")
    buttons_row = [button, button_1]
    buttons_row_two = [button_2, button_7]


    key_get_start = ReplyKeyboardMarkup(keyboard=[buttons_row, buttons_row_two], resize_keyboard=True, input_field_placeholder='Воспользуйтесь клавиатурой')
    return key_get_start



def admin_functions():
    button = KeyboardButton(text="Список пользователей")
    button_1 = KeyboardButton(text="Изменение расписаний")
    button_2 = KeyboardButton(text="Рассылка")
    buttons_row_two = [button, button_1]
    button_row_three = [button_2]


    admin_functions = ReplyKeyboardMarkup(keyboard=[buttons_row_two, button_row_three], resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой")
    return admin_functions


def admin_key_get_start():
    button = KeyboardButton(text="О сельсовете")
    button_1 = KeyboardButton(text="Галерея")
    button_2 = KeyboardButton(text="Социальные объекты")

    button_7 = KeyboardButton(text="Населенные пункты")
    button_8 = KeyboardButton(text='AdminPanel')
    buttons_row = [button, button_1]
    buttons_row_two = [button_2, button_7]
    button_row_three = [button_8]


    admin_key_get_start = ReplyKeyboardMarkup(keyboard=[buttons_row, buttons_row_two, button_row_three], resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой")
    return admin_key_get_start




def key_selsovet():
    button = KeyboardButton(text="Руководство")
    button_1 = KeyboardButton(text="Режим работы")
    button_2 = KeyboardButton(text="Контактная информация")
    button_3 = KeyboardButton(text="Одно окно")
    button_7 = KeyboardButton(text="Райисполком")

    button_4 = KeyboardButton(text="Назад")
    buttons_row = [button, button_1]
    buttons_row_two = [button_2, button_3]
    buttons_row_three = [button_7, button_4]

    key_selsovet = ReplyKeyboardMarkup(keyboard=[buttons_row, buttons_row_two, buttons_row_three],
                                       resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
                                       )
    return key_selsovet


def key_raiispolk():
    button = KeyboardButton(text="География и население")

    button_1 = KeyboardButton(text="Службы")
    button_3 = KeyboardButton(text="Суд")

    button_7 = KeyboardButton(text="Назад")

    buttons_row = [button, button_1]

    buttons_row_five = [button_3, button_7]

    key_raiispolk = ReplyKeyboardMarkup(keyboard=[buttons_row, buttons_row_five],
                                        resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
                                        )
    return key_raiispolk


def key_social_objects():
    button = KeyboardButton(text="Амбулатория")
    button_1 = KeyboardButton(text="Детский сад")

    button_4 = KeyboardButton(text="БелПочта")
    button_5 = KeyboardButton(text="Магазины")
    button_9 = KeyboardButton(text="Клуб")
    button_10 = KeyboardButton(text="Библиотека")
    button_7 = KeyboardButton(text="Назад")

    buttons_row = [button, button_1]
    buttons_row_two = [button_10, button_4]
    buttons_row_four = [button_5, button_9]
    buttons_row_five = [button_7]

    key_social_objects = ReplyKeyboardMarkup(
        keyboard=[buttons_row, buttons_row_two, buttons_row_four, buttons_row_five],
        resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
    )
    return key_social_objects


def key_cerkov():
    button = KeyboardButton(text="Великие праздники")
    button_2 = KeyboardButton(text="Галерея")

    button_7 = KeyboardButton(text="Назад")

    buttons_row = [button, button_2]
    buttons_row_four = [button_7]

    key_cerkov = ReplyKeyboardMarkup(keyboard=[buttons_row, buttons_row_four],
                                     resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
                                     )
    return key_cerkov

def key_tourists():
    button = KeyboardButton(text="Активный отдых")
    button_2 = KeyboardButton(text="Галерея")

    button_3 = KeyboardButton(text="Назад")

    buttons_row = [button, button_2]
    buttons_row_two = [button_3]
    key_tourists = ReplyKeyboardMarkup(keyboard=[buttons_row, buttons_row_two],
                                   resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
                                   )
    return key_tourists




def key_lake():
    button = KeyboardButton(text="Как добраться?")
    button_1 = KeyboardButton(text="Маршрут")

    button_4 = KeyboardButton(text="Меню")

    buttons_row = [button, button_1]

    buttons_row_three = [button_4]
    key_lake = ReplyKeyboardMarkup(keyboard=[buttons_row, buttons_row_three],
                               resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
                               )
    return key_lake

def key_get_raspisaniee():
    button = KeyboardButton(text="Автобусы")
    button_1 = KeyboardButton(text="Электропоезда")

    button_2 = KeyboardButton(text="Меню")

    buttons_row = [button, button_1]
    buttons_row_two = [button_2]
    key_raspisaniee = ReplyKeyboardMarkup(keyboard=[buttons_row, buttons_row_two],
                                      resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
                                      )
    return key_raspisaniee



def key_get_raspisanie():
    button = KeyboardButton(text="Ближайшие электропоезда")
    button_1 = KeyboardButton(text="Расписание на день")
    button_3 = KeyboardButton(text="Стоимость проезда")
    button_4 = KeyboardButton(text="Меню")
    buttons_row = [button, button_1]
    buttons_row_two = [button_3, button_4]
    key_get_raspisanie = ReplyKeyboardMarkup(keyboard=[buttons_row, buttons_row_two],
                                     resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
                                        )
    return key_get_raspisanie

def key_eventt():
    button = KeyboardButton(text="На Борисов, Минск")
    button_1 = KeyboardButton(text="На Оршу")
    button_3 = KeyboardButton(text="Расписание")

    buttons_row = [button, button_1]
    buttons_row_two = [button_3]
    key_eventt = ReplyKeyboardMarkup(keyboard=[buttons_row, buttons_row_two],
                                 resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
                                 )
    return key_eventt

def key_ysha():
    button = KeyboardButton(text="На Борисов, Минск🌃")
    button_1 = KeyboardButton(text="На Оршу🌁️")
    button_2 = KeyboardButton(text="Расписание")

    buttons_row = [button, button_1]
    buttons_row_two = [button_2]
    key_ysha = ReplyKeyboardMarkup(keyboard=[buttons_row, buttons_row_two],
                               resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
                               )
    return key_ysha

def key_ysh():
    button = KeyboardButton(text="На Борисов, Минск🌆")
    button_1 = KeyboardButton(text="На Оршу🏙️")
    button_2 = KeyboardButton(text="Расписание")

    buttons_row = [button, button_1]
    buttons_row_two = [button_2]
    key_ysh = ReplyKeyboardMarkup(keyboard=[buttons_row, buttons_row_two],
                              resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
                              )
    return key_ysh

def vlast():
    button = KeyboardButton(text="Исполком")
    button_1 = KeyboardButton(text="Сельсоветы")
    button_2 = KeyboardButton(text="Райсовет")
    button_4 = KeyboardButton(text="Законодательная власть")
    button_6 = KeyboardButton(text="Суд")
    button_7 = KeyboardButton(text="Назад")
    buttons_row = [button, button_1]
    buttons_row_two = [button_2, button_4]
    buttons_row_tree = [button_6, button_7]

    vlast = ReplyKeyboardMarkup(keyboard=[buttons_row, buttons_row_two, buttons_row_tree], resize_keyboard=True,
                                input_field_placeholder="Воспользуйтесь клавиатурой")
    return vlast

def key_slb():
    button = KeyboardButton(text="Отдел ЗАГС")
    button_1 = KeyboardButton(text="Прокуратура")
    button_2 = KeyboardButton(text="РОВД")
    button_3 = KeyboardButton(text="РОСК")
    button_5 = KeyboardButton(text="РОЧС")
    button_6 = KeyboardButton(text="Нотариальная контора")
    button_7 = KeyboardButton(text="ОПИ")
    button_9 = KeyboardButton(text="Отдел землеустройства")
    button_4 = KeyboardButton(text="Назад")
    buttons_row = [button, button_1]
    buttons_row_two = [button_2, button_3]
    buttons_row_three = [button_5, button_6]
    buttons_row_four = [button_7, button_9]

    buttons_row_six = [button_4]

    key_slb = ReplyKeyboardMarkup(
        keyboard=[buttons_row, buttons_row_two, buttons_row_three, buttons_row_four, buttons_row_six],
        resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
        )
    return key_slb

def key_soc():
    button = KeyboardButton(text="Образование")
    button_1 = KeyboardButton(text="Здравоохранение")
    button_2 = KeyboardButton(text="Труд, занятость и соцзащита")
    button_3 = KeyboardButton(text="Культура")
    button_4 = KeyboardButton(text="Религия")

    button_7 = KeyboardButton(text="Назад")

    buttons_row = [button, button_1]
    buttons_row_1 = [button_2, button_3]
    buttons_row_two = [button_4, button_7]

    key_soc = ReplyKeyboardMarkup(keyboard=[buttons_row, buttons_row_1, buttons_row_two],
                              resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
                              )
    return key_soc

def key_ek():
    button = KeyboardButton(text="Сельское хозяйстыво")
    button_1 = KeyboardButton(text="Промышленность")
    button_2 = KeyboardButton(text="ЖКХ")
    button_3 = KeyboardButton(text="Банки")
    button_4 = KeyboardButton(text="Строительство")
    button_5 = KeyboardButton(text="Транспорт")
    button_9 = KeyboardButton(text="Связь")
    button_10 = KeyboardButton(text="Лесное хозяйство")
    button_7 = KeyboardButton(text="Назад")

    buttons_row = [button, button_1]
    buttons_row_1 = [button_2, button_3]
    buttons_row_two = [button_4, button_5]
    buttons_row_four = [button_9, button_10]
    buttons_row_five = [button_7]

    key_ek = ReplyKeyboardMarkup(keyboard=[buttons_row, buttons_row_1, buttons_row_two, buttons_row_four, buttons_row_five],
                             resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
                             )
    return key_ek

def key_histt():
    button = KeyboardButton(text="Геральдика")
    button_4 = KeyboardButton(text="Назад")

    buttons_row_six = [button, button_4]

    key_histt = ReplyKeyboardMarkup(keyboard=[buttons_row_six],
                                resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
                                    )
    return key_histt


def weather():
    button = KeyboardButton(text="🔍")
    button_4 = KeyboardButton(text="Назад")

    buttons_row_six = [button, button_4]

    key_histt = ReplyKeyboardMarkup(keyboard=[buttons_row_six],
                                resize_keyboard=True, input_field_placeholder="Воспользуйтесь клавиатурой"
                                    )
    return key_histt