from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler
from datetime import datetime
import time
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


button_book = "Дневник"
button_upkmsk = "Расписание"
button_weather = 'Погода'
button_bus = "Автобус 10"
button_bus_east = 'Восточка'
button_bus_finite = 'Изоплит'
button_refresh = 'Обновить357'

all=["Дневник", "Расписание", 'Погода', "Автобус 10", 'Восточка', 'Изоплит', 'Обновить357', 'killl', 'на неделю', 'на сегодня', 'на завтра', 'hi','Hi','Hello','hello','Привет','привет','погода','klll']


names={
    'Shavkat': '574227924',
    'Lil': '837754073',
}


def rasp1(update: Update, context: CallbackContext, week_time):
    weeks = {
        1: ['2| Ин.яз    | 10:15-11:50','3| Ин.яз    | 12:45-14:20','4| ОП       | 14:30-16:05'],
        2: ['?| ПРАКТИКА | ???'],
        3: ['1| ФК       | 8:30-10:05', '2| АРХ/ПСОИ | 10:15-11:50', '3| АРХ      | 12:45-14:20','4| ОП       | 14:30-16:05'],
        4: ['2| ЭВМ      | 10:15-11:50', '3| ПСОИ     | 12:45-14:20', '4| ОП       | 14:30-16:05'],
        5: ['2| ЭМЛ/ОС   | 10:15-11:50', '3| ЭВМ      | 12:45-14:20', '4| ОС       | 14:30-16:05','5| ЭМЛ      | 16:25-18:00'],
        6: ['1| ИТ/С++   | 8:30-10:05', '2| С++      | 10:15-11:50'],
        }
    for key in weeks:
        if int(key) == week_time:
            lis = list(weeks[key])
            for i in lis:
                update.message.reply_text(
                    text=i,
                )

def rasp2(update: Update, context: CallbackContext):
    weeks = {
        1: ['2| Ин.яз    | 10:15-11:50', '3| Ин.яз    | 12:45-14:20','4| ОП       | 14:30-16:05'],
        2: ['С 9/11| !! П Р А К Т И К А !! | ???'],
        3: ['1| ФК       | 8:30-10:05', '2| АРХ/ПСОИ | 10:15-11:50', '3| АРХ      | 12:45-14:20','4| ОП       | 14:30-16:05'],
        4: ['2| ЭВМ      | 10:15-11:50', '3| ПСОИ     | 12:45-14:20', '4| ОП       | 14:30-16:05'],
        5: ['2| ЭМЛ/ОС   | 10:15-11:50', '3| ЭВМ      | 12:45-14:20', '4| ОС       | 14:30-16:05','5| ЭМЛ      | 16:25-18:00'],
        6: ['1| ИТ/С++   | 8:30-10:05', '2| С++      | 10:15-11:50'],
        }
    for key in weeks:
        lis = list(weeks[key])
        if key == 1:
            word='Понедельник'
        if key == 2:
            word='Вторник'
        if key == 3:
            word='Среда'
        if key == 4:
            word='Четверг'
        if key == 5:
            word='Пятница'
        if key == 6:
            word='Суббота'
        update.message.reply_text(text=word,)
        for i in lis:
            update.message.reply_text(
                text=i,
            )




def upkmsk(update: Update, context: CallbackContext):
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    hourminute = str(hour + ':' + minute)
    time1 = (str(str(datetime.now()).split())).split('-')
    year = str(time1[0][4:])
    month = str(time1[1])
    day = str(time1[2][:2])
    all_date = str(day + '/' + month + '/' + year + ' ' + hourminute)
    dt = datetime.strptime(all_date, "%d/%m/%y %H:%M")
    tt = dt.timetuple()
    yday0 = int(tt.tm_yday)
    # Файл, полученный в Google Developer Console
    CREDENTIALS_FILE = 'ros.json'
    # ID Google Sheets документа (можно взять из его URL)
    spreadsheet_id = '1ZBJrG8jyDRjknaT9_xiHavdVCA9KhUhj8-i3KumCakY'
    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = build('sheets', 'v4', http=httpAuth)
    # Пример чтения файла
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='замены!A2:D72',
        majorDimension='ROWS',
    ).execute()
    values2 = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='замены!F2:I72',
        majorDimension='ROWS',
    ).execute()

    lis1 = values['values']
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    hourminute = str(hour + ':' + minute)
    data_r = ((str(lis1[0]).split())[4]).split('.')
    year = str(data_r[2][2:])
    month = str(data_r[1])
    day = str(data_r[0])
    all_date = str(day + '/' + month + '/' + year + ' ' + hourminute)
    dt = datetime.strptime(all_date, "%d/%m/%y %H:%M")
    tt = dt.timetuple()
    yday1 = int(tt.tm_yday)
    lis1 = values2['values']
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    hourminute = str(hour + ':' + minute)
    data_r = ((str(lis1[0]).split())[4]).split('.')
    year = str(data_r[2][2:])
    month = str(data_r[1])
    day = str(data_r[0])
    all_date = str(day + '/' + month + '/' + year + ' ' + hourminute)
    dt = datetime.strptime(all_date, "%d/%m/%y %H:%M")
    tt = dt.timetuple()
    yday2 = int(tt.tm_yday)
    print('vsaaaaa')
    if yday0 +1 == yday1:
        lis1 = values['values']
    if yday0 +1 == yday2:
        lis1 = values2['values']
    kk = ''
    pp = '0'
    for i in range(1, len(lis1)):
        l = lis1[i]
        if l[1] == 'П-283':
            pp='1'
            for j in range(len(l)):
                kk = kk+l[j] + ' '
            update.message.reply_text(text=(kk))

    if pp == '0':
        update.message.reply_text(text='На завтра замен по группе П-283 нет!!')




def weather(update: Update, context: CallbackContext):
    import pyowm
    owm = pyowm.OWM('499af2ef60db617604eed7263763a802', language='ru')
    city = "Екатеринбург"
    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    print(w)
    compas = w.get_wind()['deg']

    def cardinal_points(compas):
        if compas >= 337.5 and compas <= 22.5:
            parties = 'северный'
        elif compas > 22.5 and compas < 67.5:
            parties = 'северо-восточный'
        elif compas >= 67.5 and compas <= 112.5:
            parties = 'восточный'
        elif compas > 112.5 and compas < 157.5:
            parties = 'юго-восточный'
        elif compas >= 157.5 and compas <= 202.5:
            parties = 'южный'
        elif compas > 202.5 and compas < 247.5:
            parties = 'юго-западный'
        elif compas >= 247.5 and compas <= 292.5:
            parties = 'западный'
        elif compas > 292.5 and compas < 337.5:
            parties = 'северо-западный'
        return parties


    temperature = str(int(w.get_temperature('celsius')['temp']))
    status = w.get_detailed_status()
    cardinal = cardinal_points(compas)
    speed = str(w.get_wind()['speed'])
    humidity = str(w.get_humidity())
    u=str(update.message.date)
    print(u)
    update.message.reply_text(
        text='Температура:  ' + temperature + '° ' + status + "\nВлажность:  " + humidity + " %" + '\nВетерт:   ' + speed + ' м/с, ' + cardinal + " ",
    )


def time_table(direction, update: Update, context: CallbackContext):
    import time
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    hourminute = float(hour + '.' + minute)+5
    week = time.strftime('%A')
    east_weekdays = '5:55 6:25 7:00 7:20 7:45 8:10 8:35 9:05 9:30 10:05 10:40 11:30 11:45 12:10 12:46 13:05 13:25 13:50 14:20 14:40 15:13 15:35 15:55 16:30 16:46 17:05 17:20 17:55 18:25 18:48 19:25 20:00 20:22 20:42 21:22 21:46 22:24'
    finite_weekdays = '6:25 7:00 7:35 7:57 8:20 8:45 9:10 9:40 10:05 10:40 11:20 12:05 12:25 12:45 13:23 13:40 14:00 14:31 15:00 15:17 15:57 16:16 16:33 17:06 17:22 17:45 18:01 18:36 19:02 19:26 20:02 20:33 20:53 21:14 21:55 22:19 22:55'
    east_Saturday = '6:22 7:00 7:30 7:55 8:20 8:45 9:05 10:10 10:30 11:30 12:05 12:25 12:45 13:10 13:30 14:30 15:35 15:55 16:55 17:20 18:25 19:00 20:00 21:00 22:00'
    finite_Saturday = '6:50 7:30 8:00 8:25 8:50 9:15 9:35 10:40 10:59 12:10 12:35 12:55 13:20 13:40 14:00 15:00 16:04 16:24 17:25 17:50 18:55 19:30 20:30 21:30 22:30'
    east_Sunday = '6:25 6:55 7:35 8:15 9:00 10:35 11:50 12:40 13:15 14:00 15:15 16:00 17:25 18:10 19:25 19:45 20:55 22:00'
    finite_Sunday = '6:58 7:35 8:20 8:55 9:40 11:15 12:35 13:20 14:00 14:40 15:55 16:40 18:05 18:50 20:05 20:20 21:28 22:32'

    if week == 'Saturday':
        if direction == button_bus_east:
            timetable = east_Saturday
        if direction == button_bus_finite:
            timetable = finite_Saturday

    if week == 'Sunday':
        if direction == button_bus_east:
            timetable = east_Sunday
        if direction == button_bus_finite:
            timetable = finite_Sunday

    else:
        if direction == button_bus_east:
            timetable = east_weekdays
        if direction == button_bus_finite:
            timetable = finite_weekdays

    timetable = list(timetable.replace(':', '.').split())
    weekdays = {}
    for i in range(len(timetable)):
        weekdays[i] = float(timetable[i])
    keys = len(weekdays)
    for key in weekdays:
        if weekdays[key] >= hourminute:
            keys = key
            break

    if hourminute < 7:
        keys1 = 0
        keys2 = 4

    elif keys >= len(weekdays)-3:
        keys1 = len(weekdays) - 4
        keys2 = len(weekdays)

    else:
        for key in weekdays:
            if weekdays[key] >= hourminute:
                keys = key
                break
        keys1 = keys - 1
        keys2 = keys + 3

    for i in range(keys1, keys2, 1):
        if weekdays[i] <= hourminute:
            k = 'Предыдущий рейс: '
        else:
            k = 'Следующий  рейс: '
        hourminutes = (str(weekdays[i]).replace('.', ' ')).split()
        if len(hourminutes[1]) == 1:
            hourminutes[1] = str(hourminutes[1]) + '0'
        if len(hourminutes[0]) == 1:
            hourminutes[0] = '0' + str(hourminutes[0])
        hourminutes = str(hourminutes[0]) + ':' + str(hourminutes[1])
        update.message.reply_text(
            text=(k + hourminutes)
        )


# def button_book_handler(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         text='Категория "дневник" пока не доступна!',
#         reply_markup=ReplyKeyboardRemove(),
#     )


def button_bus_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_bus_east),
                KeyboardButton(text=button_bus_finite),
            ],
        ],
        resize_keyboard=True
    )

    update.message.reply_text(
        text='Выбери остановку:',
        reply_markup=reply_markup,
    )


def button_ras(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='на неделю'),
                KeyboardButton(text='на сегодня'),
                KeyboardButton(text='на завтра'),
            ],
        ],
        resize_keyboard=True
    )
    update.message.reply_text(
        text='Выбери расписание:',
        reply_markup=reply_markup,
    )


r=1
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    name=update.message.chat.first_name
    id=update.message.chat.id
    # print(name,id)
    if name not in names:
        names[name]=id

    if text == 'на завтра':
        week_time = int(time.strftime('%w'))
        if week_time == 6:
            update.message.reply_text(
                reply_markup=ReplyKeyboardRemove(),
                text='Ты дурак? завтра не учимся! \n Вот расписание на понедельник!',
            )
        if (week_time ==6) or (week_time ==0):
            week_time=1
            update.message.reply_text(
                text='Расписание на завтра:',
                reply_markup=ReplyKeyboardRemove(),
            )
            rasp1(update=update, context=context, week_time=week_time)
            return
        week_time = week_time + 1
        update.message.reply_text(
            text='Расписание на завтра:',
            reply_markup=ReplyKeyboardRemove(),
        )
        rasp1(update=update, context=context, week_time=week_time)


    if text == 'на сегодня':
        week_time = int(time.strftime('%w'))
        print(week_time)
        if week_time==0:
            update.message.reply_text(
                reply_markup=ReplyKeyboardRemove(),
                text='Ты дурак? сегодня не учимся!',
            )
            return
        update.message.reply_text(
            text='Расписание на сегодня:',
            reply_markup=ReplyKeyboardRemove(),
        )
        rasp1(update=update, context=context, week_time=week_time)
    if text == 'на неделю':
        update.message.reply_text(
            text='Расписание на неделю:',
            reply_markup=ReplyKeyboardRemove(),
        )
        rasp2(update=update, context=context)


    if text == 'klll':
        print(122)
        upkmsk(update=update, context=context)


    if text=='killl':
        for key in names:
            context.bot.send_message(chat_id=574227924, text=key+'  '+str(names[key]))
            # print(key, '--', names[key])

    if text == button_refresh:
        for key in names:
            context.bot.send_message(chat_id=names[key], text=" !!!Это не проста так! зайди зацени!!! \n Чтобы узнать расписание напиши боту 'Расписание'! \n Результат может отправиться не сразу!\n Автоматизация расписание будет не скоро!")

    if text == 'hi' or text == 'Hi' or text == 'Hello' or text == 'hello' or text == 'Привет' or text == 'привет':
        name = update.message.chat.first_name
        update.message.reply_text(
            text='Привет ' + name + '!',
        )

    if text == button_upkmsk:
        return (button_ras(update=update, context=context))


    # if text == button_book:
    #     text1 = text
    #     return button_book_handler(update=update, context=context), text1

    if text == button_bus:
        text1 = text
        return (button_bus_handler(update=update, context=context)), text1
    if (text == button_bus_east) or (text == button_bus_finite) :
        direction = button_bus_east
        update.message.reply_text(
            text='Рейсы "Автобуса 10" остановки "Восточная"',
            reply_markup=ReplyKeyboardRemove(),
        )
        time_table(direction, update=update, context=context)

    if text == button_weather or text == 'погода':
        update.message.reply_text(
            text='Погода в Екатеринбурге:',
            reply_markup=ReplyKeyboardRemove(),
        )
        weather(update=update, context=context)

    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                # KeyboardButton(text=button_book),
                KeyboardButton(text=button_bus),
                KeyboardButton(text=button_weather),
                KeyboardButton(text=button_upkmsk),
            ],
        ],
        resize_keyboard=True
    )

    if text not in all:
        update.message.reply_text(
            text='Выбери категорию!',
            reply_markup=reply_markup,
        )

def main():
    print('Start')

    updater = Updater(
        token='1063534225:AAGF_uztOPJ0Wo7nRKd2olIPI5AnwdgJ-kc',
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

