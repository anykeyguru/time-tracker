#!/usr/bin/ python3
# -*- coding: utf-8 -*-
import os
import json
from config import regstrFile

def forLastStrokes():
    read_last = open(regstrFile)
    last = read_last.readlines()
    read_last.close()
    return last

def find_lang_param():
    with open('dict.json', 'r', encoding='utf-8') as f:
        lang_list = json.load(f)
        if "RU" in forLastStrokes()[0]:
            TRIG_LNG = 'RU'
        elif "EN" in forLastStrokes()[0]:
            TRIG_LNG = 'EN'
    return TRIG_LNG

def wt(win, phrase):
    with open('dict.json', 'r', encoding='utf-8') as f:
        lang_list = json.load(f)
    text = phrase
    window = win
    a = lang_list[0][window][text][find_lang_param()]
    return a

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')