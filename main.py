#if letter is capital: correct letter, correct place

#if letter is lowercase: letter not found in word

import json
import random

data = json.load(open("dictionary.json"))

def fiveLetterWords():
    fiveLetters = []
    sum = 0
    for word in data.keys():
        word = word.lower()
        if len(word) == 5:
            fiveLetters.append(word)      
            sum +=1    
    print(sum) 
    return fiveLetters

def chooseWord(possibleWords):
    word = possibleWords[random.randint(0, 3552)]
    return word
    


#def game():
   # guess = input("please enter a five letter word")
    #for letter in guess: 
        


possibleWords = fiveLetterWords()
word = chooseWord(possibleWords)






