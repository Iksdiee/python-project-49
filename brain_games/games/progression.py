import random


def generate_progression():
    start_number = random.randint(0, 10)
    length = random.randint(5, 10)
    increment = random.randint(1, 10)
    progression = [start_number]
    counter = 0

    while len(progression) != length:
        progression.append(progression[counter] + increment)
        counter += 1

    return progression

def game_progression():
    basis = generate_progression()
    replace_index = random.randint(0, len(basis)-1)
    answer = basis[replace_index]
    question = ''

    for i in basis:
        if i == answer:
            question += ' .. '
        else:
            question += f' {str(i)} '

    return question, str(answer)
