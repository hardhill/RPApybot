import os
import json
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
        files = filter(lambda x: x.endswith(".json"), files)
        self.data = []
        for onefile in files:
            with open(DIROUTDATA + "\\" + onefile, 'r') as file:
                data = json.load(file)
                self.data.append(data)
            try:
                pass
                #os.remove(DIROUTDATA + "\\" + onefile)
            except:
                pass

    def ListData(self):
        return self.data
