import random
import os

os.system('cls')
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(logo)
word_list = ["watermelon", "banana", "cherry"]
chosen_word = random.choice(word_list)
lives = 6

display_word = list('_' * len(chosen_word))
print(stages[6])
print(display_word)
print(lives)

while '_' in display_word:
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter not in display_word:
        os.system('cls')
        for pos in range(len(chosen_word)):
            if guess_letter == chosen_word[pos]:
                display_word[pos] = guess_letter

        if guess_letter not in chosen_word:
            lives -= 1
        print(logo)
        print(stages[lives])
        print(display_word)
        print(lives)
    else:
        print('You already guessed')
    if lives == 0:
        print("Lose")
        break
else:
    print("Win")

