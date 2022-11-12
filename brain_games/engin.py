import prompt
from .cli import welcome_user


def run_game(name_game):

    print('Welcome to the Brain Games!')
    name = welcome_user()
    game = name_game.game
    print(game)

    incorrect_answer = 'is wrong answer ;(. Correct answer was'
    counter = 1

    while counter <= 3:
        answer, question = name_game.function()
        print(f'Question: {question}')
        user_answer = prompt.string('You answer: ')

        if user_answer == answer:
            print('Correct!')
            counter = counter + 1

        elif user_answer != answer:
            print(f"'{user_answer}' {incorrect_answer} '{answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
