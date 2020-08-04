import telebot
from log import Logf
from outdata import OutData
class Application(object):
    def __init__(self):
        print("============= RPA bot ====================")
        self.bot = telebot.TeleBot("1333442954:AAEA2Zn5jkvRc3ag6Cv8qdJyX2Bo8G3Fb68")
        self.log = Logf()
        # вернуть список файлов готовых для отправки
        self._htmls = OutData().ListData()


    def Start(self):
        self.me = self.bot.get_me()
        if(self.me):
            print(f"Идентификатор: {self.me.id}")
            print(f"Название:{self.me.first_name}")
            return True
        else:
            print("Бот не инициализировался. Завершаю программу")
            return False
    def SendMessage(self):
        err = 0
        if len(self._htmls) < 1:
            return False
        for data in self._htmls:
            print("Посылаю сообщение...")
            try:
                m = self.bot.send_message("-443484708", data, parse_mode="html")
            except Exception as er:
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
