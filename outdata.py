import os
from params import *
class OutData:
    def __init__(self):
        #создать папку если нет ее
        if not os.path.exists(DIROUTDATA):
            try:
                os.makedirs(DIROUTDATA)
            except:
                pass
        #считать все файлы заданной директории
        files = os.listdir(DIROUTDATA)
        htmls = filter(lambda x: x.endswith(".html"), files)
        self.data = []
        for html in htmls:
            with open(DIROUTDATA + "\\" + html, 'r', encoding="utf8") as file:
                data = file.read()
                self.data.append(data)
            try:
                os.remove(DIROUTDATA + "\\" + html)
            except:
                pass

    def ListData(self):
        return self.data
