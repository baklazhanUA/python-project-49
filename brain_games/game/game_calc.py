from random import randint, choice

QUESTION = 'What is the result of the expression?'
number1 = randint(0, 20)
number2 = randint(0, 20)


def is_random_operator():
    sign = '+ - *'
    list = sign.split()
    random_sign = choice(list)
    return random_sign


operator = is_random_operator()
question = f'{number1} {operator} {number2}'


def get_game():
    if operator == '+':
        answer = number1 + number2

    elif operator == '-':
        answer = number1 - number2

    else:
        answer = number1 * number2

    return str(answer), question
