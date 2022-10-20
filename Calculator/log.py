from datetime import datetime as dt
from time import time


def div_logger(data):
    time = dt.now().strftime("%H:%M")
    with open("log.txt", "a") as file:
        file.write("{}, {}".format(time, data))
