#!/usr/bin/ python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import re
import json


class CounterTime:
    def __init__(self, file, startdate, enddate, lang):
        MFT = '%Y.%m.%d'
        self.LANG = lang
        self.startdate = startdate
        self.enddate = enddate
        pattern_a = '[0-9][0-9][0-9][0-9]\.[0-1][0-2]\.[0-3][0-9]'
        pattern_b = '[0-9][0-9][0-9][0-9]\.0[0-9]\.[0-3][0-9]'
        if re.match(pattern_a, self.startdate) and re.match(pattern_a, self.enddate)\
                or re.match(pattern_b, self.startdate) and re.match(pattern_b, self.enddate):
            self.start_date = datetime.strptime(self.startdate, MFT)
            self.end_date = datetime.strptime(self.enddate, MFT)
        else:
            print(self.wt('calc', 'p05'), end="")     # No true data, repeat enter
            self.start_date = datetime.strptime('1900.01.01', MFT)
            self.end_date = datetime.strptime('2050.01.01', MFT)
        self.file = file




    def wt(self, win, phrase):
        with open('dict.json', 'r', encoding='utf-8') as f:
            lang_list = json.load(f)
        text = phrase
        window = win
        a = lang_list[0][window][text][self.LANG]
        return a

    def CountSumm(self):
        print(self.wt('calc', 'p04'), self.start_date.strftime('%Y.%m.%d') + "/"
              + self.end_date.strftime('%Y.%m.%d'), end="\n")
        regIstrFile = self.file
        read_file = open(regIstrFile)
        lines = read_file.readlines()
        valueTime = 0
        for line in lines:
            spl_line = line.split()[0]
            if spl_line not in('RU', 'EN'):
                MFT = '%Y.%m.%d'
                spl_line = datetime.strptime(line.split()[0], MFT)
                if self.start_date <= spl_line <= self.end_date:
                    if line.split()[2] == "Out":
                        ftr = [3600, 60, 1]
                        SSUMM = sum([a * b for a, b in zip(ftr, map(int, line.split()[4].split(':')))])
                        valueTime = valueTime + SSUMM
                    else:
                        pass
                else:
                    pass
            else:
                pass

        read_file.close()

        if len(str(timedelta(seconds=valueTime))) not in (7, 8):
            ithDay = str(timedelta(seconds=valueTime)).split(",")[1].split(":")[1:3]
            shareTime = str(timedelta(seconds=valueTime))
            print(self.wt('calc', 'p06'), shareTime + self.wt('calc', 'p07'), self.wt('calc', 'p09'),
                  str(valueTime // 3600) + ":" + ithDay[0] + ":" + ithDay[1], ")", end="\n")
            print(self.wt('calc', 'p08'), str(valueTime // 3600) + self.wt('calc', 'p07'), end="\n\n")
        else:
            print(self.wt('calc', 'p06'), str(timedelta(seconds=valueTime)) + self.wt('calc', 'p07'), end="\n")


# test = CounterTime('reglist.txt', "2020.05.21", "2020.05.22", 'EN')
# test.CountSumm()
