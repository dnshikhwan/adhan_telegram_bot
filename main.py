# # al adhan app
import aladhan
from tabulate import tabulate
import telebot


def adhan_sender():
    location = aladhan.Coordinates(55.755825,37.617298)
    client = aladhan.Client(location)

    adhans = client.get_today_times()

    prayer_times = {}
    for adhan in adhans:
        print("{: <15} | {: <15}".format(adhan.get_en_name(), adhan.readable_timing(show_date=False)))
        prayer_times.update({adhan.get_en_name():adhan.readable_timing(show_date=False)})

    table = tabulate(prayer_times.items(), headers=["Prayer", "Time"], tablefmt="grid")
    print(table)

    bot = telebot.TeleBot("7008122091:AAF79WZkLwPd3GNzJ3MuwhuT_iPc__WCTFY")

    @bot.message_handler(commands=['prayertime',])
    def send_welcome(message):
        bot.reply_to(message, table)

    bot.infinity_polling()


if __name__ == "__main__":
    adhan_sender()
