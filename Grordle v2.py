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

print("Loading word bank... (~1 min)")
word_bank = pd.read_excel('Word Bank long.xlsx')
# word_bank = pd.read_excel('Word Bank.xlsx', 
#                           sheet_name = '5-letter') 

num_letters = int(input("What letter length of words do you want? "))

word_bank = word_bank.loc[((word_bank['Word']).str.len()== num_letters)]

possible_solns = word_bank.loc[(word_bank['Solution'] == 'Y').array, ['Word']]

# Choosing random solution
random.seed()
soln_ndx = random.randint(0, len(possible_solns) - 1)
soln = (possible_solns.iloc[soln_ndx]).values[0]

# print(soln)

# Begin guessing
n_guess = 0
guesses = []
results = []
is_correct = False

while n_guess < num_attempts:
    print("Previous guesses: ")
    for i in range(len(guesses)):
        print(guesses[i] + " " + results[i])
        
    guess = input("Guess #" + str(n_guess + 1) + ": ").lower()
    
    # Checks if word is valid
    if len(guess) != num_letters:
        print("Invalid guess. Word must be " + str(num_letters) + " letters long.")
        
    elif guess not in word_bank.values[:, 0]:
        print("Invalid guess. Word not in word bank.")
        
    elif guess in guesses:
        print("Invalid guess. Word already guessed.")
    else:
        guesses.append(guess)
        result = ''
          
        # Checks valid guess with solution
        for i, l in enumerate(guess):
            if l == soln[i]:
                result = result + "* "
            elif l in soln:
                result = result + ". "
            else:
                result = result + "_ "
        
        results.append(result)
        
        if result == ''.join(["* " for i in range(num_letters)]):
            n_guess = num_attempts
            is_correct = True
            
        n_guess = n_guess + 1
        

if is_correct:
    print("You guessed correctly!")
    for i in range(len(guesses)):
        print(guesses[i] + " " + results[i])
else:
    print("You failed to guess the solution: " + soln)
    