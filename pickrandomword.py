import random
from words import words
import string

# print(words)

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #keep track of what letters have been guessed

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        #letters used
        print('You have', lives, 'lives. You have used these letters: ', ' '.join(used_letters))

        #current W - R D progress
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('Letter not in word.')

        elif user_letter in used_letters:
            print('You have already guessed that character. Please try again.')
        else:
            print('You did not use a real character, try again.')

            #gets here when word letters == 0 or lives == 0
    if lives == 0:
        print('You have died. The word was ', word)
    else:
        print('You guessed the word ', word, '!!!')

hangman()