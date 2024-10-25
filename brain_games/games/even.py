import random
from ..brain_engine import start_game


def game_even():
    num = random.randint(0, 100)
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = "no"
    return num, correct_answer

def start_game_even():
    start_game(game_even, 'game-even')
