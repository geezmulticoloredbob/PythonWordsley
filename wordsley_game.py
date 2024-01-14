from wordsley_manager import *

user_total_score = 0
MAX_TOTAL_SCORE = 10
MAX_NUMBER_OF_GUESS = 6
user_number_of_guesses = 0
guess_word = ''

print("Welcome to the game, please ensure that you have read the instructions in the ReadMe file before you start!")
word_of_the_day = find_target_word()
#print(word_of_the_day)
for user_number_of_guesses in range(MAX_NUMBER_OF_GUESS):
    guess_word = get_user_guess(guess_word)
    if guess_word:
        user_total_score = user_word_scoring(guess_word, word_of_the_day)
        user_number_of_guesses = user_number_of_guesses + 1
        if user_number_of_guesses == MAX_NUMBER_OF_GUESS:
            word = ""
            print(f"Sorry, you have lost, the word was {word.join(word_of_the_day)}.")
            exit()
        else:
            print(f"You have {MAX_NUMBER_OF_GUESS-user_number_of_guesses} guesses remaining.")
        if user_total_score == MAX_TOTAL_SCORE:
            print("Congrats, you won!!")
            exit()