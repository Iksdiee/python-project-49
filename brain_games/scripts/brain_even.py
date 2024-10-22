import random
from ..cli import welcome_user
from . import brain_constants


def initiate_even():
	num = random.randint(0, 100)
	if num % 2 == 0:
        	correct_answer = 'yes'
	else:
		correct_answer = "no"
	return num, correct_answer


def even_game():
	counter = 0
	user_name = welcome_user()
	print(brain_constants.GAME_DESCRIPTIONS["brain-even"])

	while counter < 3:
		question, correct_answer = initiate_even()
		print(question)
		user_answer = input()

		if user_answer == correct_answer:
			print("Correct!")
			counter += 1
		else:
			print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}"\n Let's try again!''')
			break

	if counter == 3:
		print(f"Congratulations,{user_name}")


def main():
	even_game()

if __name__ == "__main__":
	main()
