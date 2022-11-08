import prompt

def run_game(name_game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    game = name_game.game
    print(game)

    counter = 1

    while counter < 3:
        answer, question = name_game.function()

        print(f'Question: {question}')
        user_answer = input('You answer: ')

        if answer == user_answer:
            print('Correct!')
            counter = counter + 1

        elif answer != user_answer:
            return print(f'{user_answer} is wrong answer ;(. Correct answer was {answer}.')
        else:
            return print('error')




    print(f'Congratulations, {name}')



