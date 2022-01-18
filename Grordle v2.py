#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 20:04:52 2022

@author: gregorysuematsu
"""


import pandas as pd
import random

num_attempts = 6


print("Hello. Welcome to Grordle.")
print("_ is incorrect, . is correct letter & incorrect spot, * is correct letter & spot")

print("Loading word bank...")
word_bank = pd.read_excel('Word Bank copy.xlsx')

print(word_bank)

num_letters = int(input("What letter length of words do you want? "))

word_bank_clean = word_bank.loc[(len(word_bank['Word']).array == num_letters), ['Word']]

print(word_bank_clean)

