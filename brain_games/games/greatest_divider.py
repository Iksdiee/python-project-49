import math
import random


def game_gcd():
    number1, number2 = random.randint(1, 10), random.randint(1, 10)
    question = f'{number1} {number2}'
    answer = math.gcd(number1, number2)
    return question, str(answer)
