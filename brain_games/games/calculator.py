import random

def game_calculator():
    first_number = random.randint(0, 10)
    second_number = random.randint(0, 10)
    math_symbol = random.choice(['+', '-', '*'])
    question = f"{first_number} {math_symbol} {second_number}"
    answer = eval(question)
    return question, str(answer)
