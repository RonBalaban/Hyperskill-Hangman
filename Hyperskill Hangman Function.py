# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:19:18 2020

@author: Rbala
"""

# Shebang line for Windows is #!, followed by some info

#! python""3


import random
import string
print("H A N G M A N \n")
words = ['python', 'java', 'kotlin', 'javascript']
correct_word = random.choice(words)
remaining = list(correct_word)   # starts as ['p', 'y', 't', 'h', 'o', 'n'], but as we guess letters, becomes all dashes. 
guessed = list("-" * len(correct_word))  # Starts as ['-', '-', '-', '-', '-', '-'], but as we guess letters, gets closer to the word
lives = 8  # They have 8 lives
wrong_letters = [] # list of wrong letters
lets_play = ''


while lets_play not in ['play','exit']:
    lets_play = input('Type "play" to play the game, "exit" to quit: ').lower()

    if lets_play == 'play':
        while lives > 0:  # Get 8 lives for wrong guesses. right guess doesnt lose points. 
            print()
            print("".join(guessed))  # -------   # Join list into a string. Print ----- at start, but as the game goes, replace '-' with letters
            guess = input("Input a letter: ")
            if guess.islower() and len(guess) == 1 and guess not in string.punctuation:       
                if guess not in correct_word:
                    if guess not in wrong_letters:
                        print("No such letter in the word") 
                        lives -= 1 
                        wrong_letters.append(guess)
                        continue
                    if guess in wrong_letters:
                        print("You already typed this letter")                   
                if guess in guessed :  # They put a duplicate. Dashes started as ----, but became -a-a. If they guess a again, no change.
                    print("You already typed this letter")               
                else:
                    while guess in remaining: # the letter is in our listed correct word ['p', 'y', 't', 'h', 'o', 'n']. We loop in case duplicates
                        print()
                        guessed[remaining.index(guess)] = guess  # replace the '-' with correct letter (then gets printed above)
                        remaining[remaining.index(guess)] = "-"  # Replace guessed letter with '-', then cycle through loop again (if there's duplicates)
                        # Operations with list- Searching specific elements
                if lives == 0:
                    break
                if guessed == list(correct_word):  # At which point they guessed everything.
                    print(correct_word)
                    print("You guessed the word! \nYou survived!")
                    break
            else:
                if guess.isupper() or guess in string.punctuation or guess in string.digits:
                    print("It is not an ASCII lowercase letter")         
                if len(guess) != 1:
                    print("You should input a single letter")
        if guessed != list(correct_word):
                print("You are hanged!")
    if lets_play == 'quit':
        break


      
# So what happens?
# First, choose a random word to be correct (correct_word)
# Next, make a list of dashes, equal to length of correct_word : ------- (dashes)
# Then make a list containing the letters in correct_word (listed)  Why? So that when we guess a letter, we check if it's in this list.
# If it is, then change the correctly guessed letter to be a '-'.  Why? This allows us to loop through this list if there's mutliple of one letter.
# While loop part: 
# Guess the correct letter. 
# Next, turn ---------- (dashes) into -a-a------ [javascript] by using the index in listed
# Then, turn the correctly guessed letter into '-' .  i.e: j-v-script
               
# We're basically looking in a list of correct letters. Replacing dashes with the letter where they should be.
# The second part; listed[listed.index(guess)] = "-"  is just used for removing the already guessed letters
                
                
                
                
                
                
    
    
    