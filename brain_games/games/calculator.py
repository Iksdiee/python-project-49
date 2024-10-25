import random
from ..brain_engine import start_game

def game_calculator():
    first_number = random.randint(0, 10)
    second_number = random.randint(0, 10)
    math_symbol = random.choice(['+', '-', '*'])
    question = f"{first_number} {math_symbol} {second_number}"
    answer = eval(question)
    return question, str(answer)

def start_game_calculator():
    start_game(game_calculator, 'game-calculator')
