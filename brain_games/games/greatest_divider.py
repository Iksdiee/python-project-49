import random
import math
from ..brain_engine import start_game


def game_gcd():
    number1, number2 = random.randint(1, 10), random.randint(1, 10)
    question = f'{number1} {number2}'
    answer = math.gcd(number1, number2)
    return question, str(answer)


def start_game_gcd():
    start_game(game_gcd, 'game-gcd')
