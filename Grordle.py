#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 19:54:28 2022

@author: gregorysuematsu
"""

import pandas as pd
import numpy as np
import random

num_attempts = 6

# print("Hello. Welcome to Grordle.")
print("_ is incorrect, . is correct letter & incorrect spot, * is correct letter & spot")
# num_letters = input("What letter length of words do you want? ")

num_letters = '5'

word_bank = pd.read_excel('Word Bank.xlsx', 
                          sheet_name = num_letters + '-letter') 
# print (word_bank)


possible_solns = word_bank.loc[(word_bank['Solution'] == 'Y').array, ['Word']]
# print(possible_solns)

random.seed()
soln_ndx = random.randint(0, len(possible_solns) - 1)
soln = (possible_solns.loc[soln_ndx]).values[0]

print(word_bank.values)

guess = "hello"

n_guess = 0

guesses = []
results = []

while n_guess < num_attempts:
    print("Previous guesses: ")
    for i in range(len(guesses)):
        print(guesses[i])
        print(results[i])
        
    guess = input("Guess #" + str(n_guess + 1) + ": ")
    
    if len(guess) != int(num_letters) or guess not in word_bank.values:
        print("Invalid guess.")
    
    else:
        guesses.append(guess)
        
        
        
        n_guess = n_guess + 1
    