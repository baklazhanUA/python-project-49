import random
from random import randint

QUESTION = 'What is the result of the expression?'
number1 = randint(0, 20)
number2 = randint(0, 20)


def is_random_operator():
    sign = '+ - *'
    list = sign.split()
    random_sign = random.choice(list)
    return random_sign


operator = is_random_operator()


def is_calc():
    if operator == '+':
        result = number1 + number2
        return result
    elif operator == '-':
        result = number1 - number2
        return result
    else:
        result = number1 * number2
        return result


answer = is_calc()


def get_game():
    question = f'{number1} {operator} {number2}'
    return str(answer), question
