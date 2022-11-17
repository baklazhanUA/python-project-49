import prompt


def run_game(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    play = game.QUESTION
    print(play)

    counter = 1

    while counter <= 3:
        answer, question = game.get_game()
        print(f'Question: {question}')
        user_answer = prompt.string('You answer: ')

        if user_answer == answer:
            print('Correct!')
            counter = counter + 1

        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
