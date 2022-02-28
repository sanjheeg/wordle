#if letter is X: correct letter, correct place

#if letter is 'x': correct letter, wrong place 

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
    return fiveLetters

def chooseWord(possibleWords):
    word = possibleWords[random.randint(0, 6370)]
    return word
    

def game(answer):
    print(answer)
    sum = 0
    for i in range(0,5):
        print("instructions:\n -capital letter means correct letter at correct place \n -characters in single quotation marks mean correct letter at the wrong place \n -lowercase letters mean wrong letters at the wrong place")
        guess = input("please enter a five letter word: ")
        for i in range (0, 5):
            sum += 1
            if answer.lower() == guess.lower():
                print("YAY you got this")
                break
            if sum == 5: 
                if answer.lower() != guess.lower():
                    print("OH NO its okay!")
            guess = list(guess)
            answer = list(answer)
            #correct word, correct place
            if answer[i]== guess[i]:
                guess[i] = guess[i].upper()
            #correct word, wrong place
            elif guess[i] in answer:
                str(guess[i])
                guess[i] = "'" + guess[i] + "'"
            
        print(*guess, sep = " ")

    

possibleWords = fiveLetterWords()
word = chooseWord(possibleWords)
game(word)





