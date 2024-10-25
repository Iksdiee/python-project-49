import random
from ..brain_engine import start_game

def generate_progression():
    start_number = random.randint(0, 10)
    length = random.randint(5, 10)
    increment = random.randint(1, 10)
    progression = []

    for i in range(length):
       progression.append(start_number + i * increment)

    return progression

def game_progression():
    basis = generate_progression()
    replace_index = random.randint(0, len(basis) - 1)
    answer = basis[replace_index]
    question = ''

    for i in range(len(basis)):
        if i == replace_index:
            question += '.. '
        else:
            question += f'{basis[i]} '

    return question.strip(), str(answer)

def start_game_progression():
    start_game(game_progression, 'game-progression')
