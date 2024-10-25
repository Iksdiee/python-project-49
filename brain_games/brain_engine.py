from .cli import welcome_user
from .brain_constants import GAME_DESCRIPTIONS


def start_game(game, game_description):
    counter = 0
    user_name = welcome_user()

    print(GAME_DESCRIPTIONS[game_description])

    while counter < 3:
        question, correct_answer = game()
        print(f'Question: {question}')
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f'''"{user_answer}" is wrong answer ;(.
            Correct answer was "{correct_answer}"\n
            Let's try again, {user_name}!''')
            break

    if counter == 3:
        print(f"Congratulations, {user_name}!")
