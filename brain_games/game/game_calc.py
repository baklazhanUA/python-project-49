from random import randint, choice

QUESTION = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def is_calc(first_number, random_operator, second_number):
    if random_operator == '+':
        answer = first_number + second_number

    elif random_operator == '-':
        answer = first_number - second_number

    else:
        answer = first_number * second_number
    return answer


def get_game():
    first_number = randint(0, 20)
    second_number = randint(0, 20)

    random_operator = choice(OPERATORS)
    question = f'{first_number} {random_operator} {second_number}'
    answer = is_calc(first_number, random_operator, second_number)

    return str(answer), question
