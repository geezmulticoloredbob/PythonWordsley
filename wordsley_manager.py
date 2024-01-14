"""
Wordsley is a guess the word application where the user
has six chances to guess a five letter word.
Author: Coen Walmsley
Company: NM Tafe
Copyright: 2022
"""

import random

LENGTH_OF_WORD = 5
characters_used = []
user_total_score = 0
user_letter_score = [0] * LENGTH_OF_WORD
NO_LETTER_NO_PLACE = '❌  '
YES_LETTER_NO_PLACE = '❓  '
YES_LETTER_YES_PLACE = '✔  '
user_number_of_guesses = 0
user_display_score = [NO_LETTER_NO_PLACE] * LENGTH_OF_WORD


def find_target_word():
    """
    Function used to select a random target word from the target words file.
    :param target_word: The target word (currently saved as an empty string variable)
    :return: The target word in a list of characters

    """

    with open("word-bank/target_words.txt", "r") as file:
        all_text = file.read()
        words = list(map(str, all_text.split()))
        # use random to save target word as variable
        target_word = random.choice(words)
    target_word = list(target_word)
    return target_word


def get_user_guess(user_word):
    """
    Takes the user's input, checks that it is a valid
    :param user_word: The user's input (currently an empty string)
    :return: The user's input validated and ready to be scored
    >>> get_user_guess('aback')
    ['a', 'b', 'a', 'c', 'k']
    >>> get_user_guess('back')
    "Invalid guess, please try again!"
    >>> get_user_guess('cracks')
    "Invalid guess, please try again!"
    >>> get_user_guess(123)
    "Invalid guess, please try again!"
    """
    while True:
        user_word = input("Please enter your guess: ")
        if len(user_word) != LENGTH_OF_WORD:
            print("Invalid guess, please try again!")
            continue
        elif not user_guess_check(user_word):
            continue
        return list(user_word)


def user_guess_check(word):
    """
    Checks through the all words allowed text file to ensure that user's guess can be used
    :param word: User's guess word after it has been validated by type and length
    :return: Message whether word can be used or not.
    >>> user_guess_check("sting")
    True
    >>> user_guess_check("app")
    False
    >>> user_guess_check("string")
    False
    >>> user_guess_check('zyamb')
    False
    """
    file = open("word-bank/all_words.txt", "r")
    readfile = file.read()
    if word in readfile:
        return True
    else:
        print("Invalid guess, try again!")


def user_word_scoring(user_word, target_word):
    """
    Compares the elements of the target word list and the user word list, and scores the user word in comparison
    to the target word.
    :param user_word: The list of the user's word
    :param target_word: The list of the target word
    :return: The user's score for that word compared to the target score
    >>> user_word_scoring('peach', 'apple')
    ['p', 'e', 'a', 'c', 'h']
    ['⌀', '⌀', '⌀', '~', '~']
    You have used the following characters: ['p', 'e', 'a', 'c', 'h']
    3
    >>> user_word_scoring('peach', 'sting')
    ['p', 'e', 'a', 'c', 'h']
    ['~', '~', '~', '~', '~']
    You have used the following characters: ['p', 'e', 'a', 'c', 'h']
    0
    >>> user_word_scoring('fling', 'sting')
    [0, 0, 2, 2, 2]
    ['f', 'l', 'i', 'n', 'g']
    ['~', '~', '✓', '✓', '✓']
    You have used the following characters: ['f', 'l', 'i', 'n', 'g']
    6
    """

    for i, letter in enumerate(user_word):
        if user_word[i] == target_word[i]:
            user_letter_score.pop(i)
            user_letter_score.insert(i, 2)
            user_display_score.pop(i)
            user_display_score.insert(i, YES_LETTER_YES_PLACE)

        elif letter in target_word:
            user_letter_score.pop(i)
            user_letter_score.insert(i, 1)
            user_display_score.pop(i)
            user_display_score.insert(i, YES_LETTER_NO_PLACE)
        else:
            user_display_score.pop(i)
            user_display_score.insert(i, NO_LETTER_NO_PLACE)
            characters_used.append(letter)
    word = "   "
    word1 = ""
    user_string = word.join(user_word)
    print(user_string.upper())
    print(word1.join(user_display_score))
    user_total_score = sum(user_letter_score)
    print(f"You have used the following characters: {characters_used}")
    return sum(user_letter_score)


def main(test=False):
    if test:
        import doctest
        return doctest.testmod()


if __name__ == "__main__":
    print(main(test=True))
