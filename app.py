import telebot
from log import Logf
from outdata import OutData
class Application(object):
    def __init__(self):
        print("============= RPA bot ====================")
        self.bot = telebot.TeleBot("1333442954:AAEA2Zn5jkvRc3ag6Cv8qdJyX2Bo8G3Fb68")
        self.log = Logf()
        self.htmls = OutData()

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
        print("Посылаю сообщение...")
        m = self.bot.send_message("-443484708","<b>Hello from python bot</b>",parse_mode="html")
        if len(m)>0:
            pass


if __name__ == '__main__':
    app = Application()
    if not app.Start():
        exit(1)
   # app.SendMessage()