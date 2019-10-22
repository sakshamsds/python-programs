# -*- coding: utf-8 -*-

#https://www.geeksforgeeks.org/hangman-game-python

import random
from collections import Counter
#import re

text = open('word2.0.txt', 'r')
words = []
words = text.read().split('\n')

'''
# regex for lower caseletters only
regex = '[^a-z ]'

# make list of words
text = open('words.txt', 'r')
words = []
lines = text.readlines()
for line in lines:
    line = line.lower()
    line = re.sub(regex, '', line)
    words += line.split(' ')
'''

# remove small words and other characters
smallWords = []

for word in words:
    if len(word)<4:
        smallWords.append(word)
        
for word in smallWords:
    if word in words:
        words.remove(word)

word = random.choice(words)

# function for inputting a guess
def guess_input():
    try:
        guess = str(input('Enter a letter to guess: '))
    except:
        print('Enter only a letter')
    return guess.lower()

# function for validating a guess
def guess_validated(guess, letterGuessed):
    if len(guess)!=1:
        print('Enter only SINGLE letter ffs\n')
        return False
    elif not guess.isalpha():
        print('Enter only LETTER goddammit\n')
        return False
    elif guess in letterGuessed:
        print('You have already gussed this letter\n')
        return False
    return True

def game():
    print('Guess the word!')
    
    # for printing empty spaces for letters of the word
    for _ in word:
        print('_', end=' ')
    print()
    
    # some parameters
    letterGuessed = []      # list for storing gussed letters
    chances = len(word) + 3
    flag = 0            # 1 if letter is correctly guessed
    
    try:
        while flag==0 and chances!=0:
            print()
            print('Chances left: {}'.format(chances))
            print()
            chances -= 1
            
            # Input a guess
            guess = guess_input()
            
            # Validation
            while not guess_validated(guess, letterGuessed):
                guess = guess_input()
                                    
            # if letter is guessed correctly
            if guess in word:
                chances += 1                    # if correctly guessed then chances doesnt decrease
                k = word.count(guess)           # count number of occurences of guess in word
                for _ in range(k):
                    letterGuessed += guess      # the letter is added as many times            
            
            # print the word 
            for char in word:
                if char in letterGuessed and Counter(letterGuessed) != Counter(word):
                    print(char, end=' ')
                    # if the used has guessed all letters
                elif Counter(letterGuessed) == Counter(word):
                    print('The word is: ', end=' ')
                    print(word)
                    flag=1
                    print('Congratulation, You Won!.')
                    break   # break out of for loop
                    break   # break out of while loop
                else:
                    print('_', end=' ')
                
        # if user has used all his chances
        if chances<=0 and Counter(letterGuessed) != Counter(word):
            print()
            print('You lost! Try Again.')
            print('The word was {}'.format(word))
            
    except:
        print('Bye! Try Again.')
        exit()
        

if __name__ == '__main__':
    game()
