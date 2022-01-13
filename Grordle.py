#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 19:54:28 2022

@author: gregorysuematsu
"""

import pandas as pd
import numpy as np
import random

# print("Hello. Welcome to Grordle.")
# num_letters = input("What letter length of words do you want? ")

num_letters = '5'

word_bank = pd.read_excel('Word Bank.xlsx', 
                          sheet_name = num_letters + '-letter') 
print (word_bank)


possible_solns = word_bank.loc[(word_bank['Solution'] == 'Y').array, ['Word']]
print(possible_solns)

random.seed()
soln_ndx = random.randint(1, len(possible_solns))

print(possible_solns.loc[soln_ndx])


