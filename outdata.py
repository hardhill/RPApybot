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
