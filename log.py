import os
class Logf:
    def __init__(self):
        if not os.path.exists("log"):
            try:
                os.makedirs("log")
            except:
                pass
