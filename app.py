import telebot
from log import Logf
from outdata import OutData
class Application(object):
    def __init__(self):
        print("============= RPA bot ver 1.0 ====================")
        self.bot = telebot.TeleBot("1333442954:AAEA2Zn5jkvRc3ag6Cv8qdJyX2Bo8G3Fb68")
        self.log = Logf()
        # вернуть список файлов готовых для отправки
        self._datas = OutData().ListData()


    def Start(self):
        self.me = self.bot.get_me()
        if(self.me):
            print(f"Идентификатор: {self.me.id}")
            print(f"Название бота: {self.me.first_name}")
            return True
        else:
            print("Бот не инициализировался. Завершаю программу")
            return False
    def SendMessage(self):
        err = 0
        message_count = 0
        if len(self._datas) < 1:
            return False
        for data in self._datas:
            print("Посылаю сообщение...")
            if data["type"] == "boto289":
                msg = 'Данные от: <b>'+data["time"]+'</b>\n'+data["title"]+'<b>'+data["value"]+'</b>'

            try:
                m = self.bot.send_message("-443484708", msg, parse_mode="html")
                message_count += 1
                print("Отправил сообщение: ",message_count)
            except Exception as er:
                print(er)
                err += 1
        if err > 0:
            return False

        return True


if __name__ == '__main__':
    app = Application()
    if not app.Start():
        exit(1)
    if app.SendMessage():
        print("Все сообщения посланы")
    else:
        print("Посылать пока нечего")
