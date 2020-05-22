#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
# from dictionary import DictionaryLang
import locale
import os
import sys
import time
from datetime import datetime

from calc_time import CounterTime


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n")


cls()

if sys.platform == 'win32':
    locale.setlocale(locale.LC_ALL, 'rus_rus')
else:
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

print(datetime.now().strftime("%B %Y"))

regstrFile = 'reglist.txt'
now = datetime.now()
dt_string = now.strftime("%Y.%m.%d %H:%M:%S")
try:
    file = open(regstrFile)
except IOError as e:
    with open(regstrFile, "w") as file_out:
        file_out.write("EN\n%s In\n" % dt_string)
else:
    pass

# globals
defvalue = ""
last = defvalue
EndTimeF = defvalue
startsTime = defvalue
CheckOut = defvalue


def forLastStrokes():
    global last
    read_last = open(regstrFile)
    last = read_last.readlines()


forLastStrokes()

def wt(win, phrase):    # Get phrase from dictionary json
    forLastStrokes()
    global TRIG_LNG, lLANG_TYPE
    with open('dict.json', 'r', encoding='utf-8') as f:
        lang_list = json.load(f)
    if "RU" in last[0]:
        TRIG_LNG = 'RU'
    elif "EN" in last[0]:
        TRIG_LNG = 'EN'
    text = phrase
    window = win
    a = lang_list[0][window][text][TRIG_LNG]
    return a


def MyInstructions():   # Instruction
    cls()
    print("\nThe program for count time period.\n", end="")
    print("All records in file <<reglist.txt>>.\n", end="")
    print("Usage\n", end="")
    print("\t C \tStart in. Press C(c), if you want write start time.\n", end="")
    print("\t G \tStop now. Press G(g), if you want write stop time.\n", end="")
    print("\t S \tCount summ time in hour. Press S(s) , if you want summ time between dates.\n", end="")
    print("\t Q \tQuit. Press Q(q) , if you want exit from program.\n", end="")
    print("\t RU,EN \tSet language in reglist.txt. RU - for russian, EN - for english language.\n", end="")


print(wt('main', 'p16'), dt_string.split()[0], end="")  # Сейчас
print(wt('main', 'p02'), end="")                        # Для справки введите 'I'


def getLastTime():  # Count Time between last and inserted time
    global EndTimeF, startsTime, CheckOut
    forLastStrokes()
    if "Out" in last[-1]:
        laststroke = last[-1]
        splitLastStroke = laststroke.split()
        EndTimeF = str(splitLastStroke[1])
        startsTime = EndTimeF
        CheckOut = 0
    elif "In" in last[-1]:
        laststroke = last[-1]
        splitLastStroke = laststroke.split()
        startsTime = str(splitLastStroke[1])
        EndTimeF = now.strftime("%H:%M:%S")
        CheckOut = 1
    return EndTimeF, startsTime, CheckOut


def countTime():
    global tdelta
    getLastTime()
    s1 = startsTime
    s2 = EndTimeF
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    print(wt('main', 'p09'), tdelta)
    return tdelta


while True:
    getLastTime()
    if CheckOut == 0:

        message = wt('main', 'p03')         # Для подтверждения начала записи, введите C.
        print(message)
        print("_"*len(message))
        answer = input(wt('main', 'p04'))   # Записать время начала? С:
    elif CheckOut == 1:

        answer = input(wt('main', 'p05'))   # Записать время ухода? G:
    else:

        answer = input(wt('main', 'p06'))   # Вы пришли или уходите? C или G:
    if answer in ("C", "c"):
        if CheckOut == 0:
            cls()
            now = datetime.now()
            dt_string = now.strftime("%Y.%m.%d %H:%M:%S")
            print(wt('main', 'p08'), dt_string)   # Начало:
            reglist = open(regstrFile, 'a')
            letItWrite = str(dt_string) + " In" + "\n"
            reglist.write(letItWrite)
            reglist.close()
        else:
            print("try G or g")
    elif answer in("G", "g"):
        if CheckOut == 1:
            cls()
            now = datetime.now()
            dt_stringg = now.strftime("%Y.%m.%d %H:%M:%S")
            print(wt('main', 'p01'), dt_stringg)
            reglist = open(regstrFile, 'a')
            countTime()
            letItWrite = str(dt_stringg) + " Out sum " + str(tdelta) + "\n"
            reglist.write(letItWrite)
            reglist.close()
            print(wt('main', 'p07'))   # Всего хорошего!
            time.sleep(2)
            break
        else:
            print("Try C or c")
    elif answer in ("I", "i"):
        MyInstructions()
    elif answer in("S", "s"):
        while True:
            scount = CounterTime(regstrFile, input(wt('calc', 'p10')), input(wt('calc', 'p11')),
                                 TRIG_LNG)      # "Введите начальную дату:" "Введите конечную дату:"
            CounterTime.CountSumm(scount)
            myQL = input(wt('calc', 'p03'))     # Show More?
            if myQL == "":
                continue
            else:
                break
    elif answer in("Q", "q"):
        print(wt('main', 'p07'))    # "Всего хорошего!"
        time.sleep(2)
        break
    else:
        print("Invalid response")
