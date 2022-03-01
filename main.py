#INSTRUCTIONS
# if letter is X: correct letter, correct place
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
    rounds = 0
    print("instructions: ")
    print("- capital letter means correct letter at correct place")
    print("- characters in single quotation marks mean correct letter at the wrong place")
    print("- lowercase letters mean wrong letters at the wrong place")      
    while rounds < 5:
        answer = str(answer)
        guess = input("please enter a five letter guess: ")
        #if the guess is not 5 letters long 
        while (len(guess) != 5):
            guess = input("incorrect number of letters. Please try again: ")  
        #if the guess is correct 
        if guess.lower() == answer.lower():
            print(guess.upper())
            print("YAY you win!")
            break
        #if the player is not able to get the correct word after 5 rounds
        if rounds == 4 and guess.lower() != answer.lower():
            print(list(guess))
            print("OH NO youre out of guesses :( ")
            break
        #correct letter, wrong place
        answer = list(answer)
        guess = list(guess)
        for letter in guess:
            for alphabet in answer:
                if letter == alphabet:
                    letter = letter + "+"

        """
        for letter in guess: 
            if letter in answer:
                letter = "+" + letter + "+"
        """
        
        #correct letter, correct place
        if guess[rounds] == answer[rounds]:
            guess[rounds] = guess[rounds].upper()
        
        print(guess)
        rounds+=1 
        
possibleWords = fiveLetterWords()
word = chooseWord(possibleWords)
game(word)
