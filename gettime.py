#!/usr/bin/python3
# -*- coding: utf-8 -*-
import locale
import sys
import time
from datetime import datetime
from calc_time import CounterTime
from config import regstrFile
from utils import cls,  find_lang_param, get_phrase, MyInstructions, forLastStrokes


# globals
default_value = ""
last = default_value
EndTimeF = default_value
startsTime = default_value
CheckOut = default_value


# Clear
cls()
if sys.platform == 'win32':
    locale.setlocale(locale.LC_ALL, 'rus_rus')
else:
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
now = datetime.now()
dt_string = now.strftime("%Y.%m.%d %H:%M:%S")
try:
    file = open(regstrFile)
except IOError as e:
    with open(regstrFile, "w") as file_out:
        file_out.write("EN\n%s In\n" % dt_string)
        print("Data file created.\n")
else:
    pass


print(get_phrase('main', 'p16'), dt_string.split()[0], end="")  # Сейчас
print(get_phrase('main', 'p02'), end="")                        # Для справки введите 'I'

def getLastTime():  # Count Time between last and inserted time
    global EndTimeF, startsTime, CheckOut
    forLastStrokes()
    now = datetime.now()
    if "Out" in forLastStrokes()[-1]:
        the_last_stroke = forLastStrokes()[-1]
        splitLastStroke = the_last_stroke.split()
        EndTimeF = str(splitLastStroke[1])
        startsTime = EndTimeF
        CheckOut = 0
    elif "In" in forLastStrokes()[-1]:
        the_last_stroke = forLastStrokes()[-1]
        splitLastStroke = the_last_stroke.split()
        startsTime = str(splitLastStroke[1])
        EndTimeF = now.strftime("%H:%M:%S")
        CheckOut = 1
    return EndTimeF, startsTime, CheckOut


def countTime():
    getLastTime()
    s1 = startsTime
    s2 = EndTimeF
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    return tdelta

# Interface
while True:
    getLastTime()
    if CheckOut == 0:
        message = get_phrase('main', 'p03')         # Для подтверждения начала записи, введите C.
        print(message)
        print("_"*len(message))
        answer = input(get_phrase('main', 'p04'))   # Записать время начала? С:
    elif CheckOut == 1:
        answer = input(get_phrase('main', 'p05'))   # Записать время ухода? G:
    else:
        answer = input(get_phrase('main', 'p06'))   # Вы пришли или уходите? C или G:
    if answer in ("C", "c"):
        if CheckOut == 0:
            cls()
            now = datetime.now()
            dt_string = now.strftime("%Y.%m.%d %H:%M:%S")
            print(get_phrase('main', 'p08'), dt_string)   # Начало:
            reglist = open(regstrFile, 'a')
            letItWrite = str(dt_string) + " In" + "\n"
            reglist.write(letItWrite)
            reglist.close()
        else:
            print("try G or g")
    elif answer in ("G", "g"):
        if CheckOut == 1:
            cls()
            now = datetime.now()
            dt_stringg = now.strftime("%Y.%m.%d %H:%M:%S")
            print(get_phrase('main', 'p01'), dt_stringg)
            countTime()
            letItWrite = str(dt_stringg) + " Out sum " + str(countTime()) + "\n"
            print(get_phrase('main', 'p09'), str(countTime()))
            reglist = open(regstrFile, 'a')
            reglist.write(letItWrite)
            reglist.close()
            print(get_phrase('main', 'p07'))   # Всего хорошего!
            time.sleep(2)
            break
        else:
            print("Try C or c")
    elif answer in ("I", "i"):
        MyInstructions()
    elif answer in ("S", "s"):
        cls()
        while True:
            try:
                scount = CounterTime(regstrFile, input(get_phrase('calc', 'p10')), input(get_phrase('calc', 'p11')),
                                     find_lang_param())
                # "Введите начальную дату:" "Введите конечную дату:"
                CounterTime.CountSumm(scount)
                myQL = input(get_phrase('calc', 'p03'))  # Show More?
                if myQL == "":
                    continue
                else:
                    break
            except KeyboardInterrupt:
                print(get_phrase('calc', 'p12'))    # Пожалуйста, введите дату.
                print(get_phrase('calc', 'p13'))
    elif answer in ("Q", "q"):
        print(get_phrase('main', 'p07'))    # "Всего хорошего!"
        time.sleep(2)
        break
    else:
        print("Invalid response.")