#!/usr/bin/ python3
# -*- coding: utf-8 -*-
import os
import json
from config import regstrFile, dictionary


def forLastStrokes():
    """ Get file data """
    read_last = open(regstrFile)
    last = read_last.readlines()
    read_last.close()
    return last


def find_lang_param():
    """ Find and return language """
    if "RU" in forLastStrokes()[0]:
        TRIG_LNG = 'RU'
        return TRIG_LNG
    elif "EN" in forLastStrokes()[0]:
        TRIG_LNG = 'EN'
        return TRIG_LNG


def get_phrase(win, phrase):
    """ Phrase selector
    :param win: Console
    :param phrase: index of phrase
    :return:
    """
    window = win
    text = phrase
    with open(dictionary, 'r', encoding='utf-8') as f:
        lang_list = json.load(f)
        a = lang_list[0][window][text][find_lang_param()]
    return a



def cls():
    """ Clean console :return: """
    os.system('cls' if os.name == 'nt' else 'clear')


def MyInstructions():  # Instruction
    cls()
    print(get_phrase('main', 'p100'))
