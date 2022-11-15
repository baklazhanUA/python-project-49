import prompt
from .cli import welcome_user


def run_game(name_game):

    print('Welcome to the Brain Games!')
    name = welcome_user()
    play = name_game.QUESTION
    print(play)

    counter = 1

    while counter <= 3:
        answer, question = name_game.function()
        print(f'Question: {question}')
        user_answer = prompt.string('You answer: ')

        if user_answer == answer:
            print('Correct!')
            counter = counter + 1

        elif user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
