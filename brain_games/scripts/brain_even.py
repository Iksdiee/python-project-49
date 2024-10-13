import random

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def initiate_even():
    num = random.randint(0, 100)
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = "no"
    return num, correct_answer

