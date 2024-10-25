import random
from ..brain_engine import start_game


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def game_prime():

    question = random.randint(0, 20)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


def start_game_prime():
    start_game(game_prime, 'game-prime')
