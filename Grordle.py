#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 19:54:28 2022

@author: gregorysuematsu
"""

import pandas as pd
import numpy as np

print("Hello. Welcome to Grordle.")
num_letters = input("What letter length of words do you want? ")

print(num_letters)


word_bank = pd.read_excel('Word Bank.xlsx', 
                          sheet_name = num_letters + '-letter') 
print (word_bank)

# possible_solns = word_bank.loc(word_bank['Solution'] == 'Y') 
word_bank['Solution']
# print(possible_solns())
