import random
from random import randint

QUESTION = 'What is the result of the expression?'


def function():
    number1 = randint(0, 20)
    number2 = randint(0, 20)
    operators = '+ - *'
    list = operators.split()
    random_operators = random.choice(list)
    question = f'{number1} {random_operators} {number2}'

    def is_calc():
        if random_operators == '+':
            result = number1 + number2
            return result
        elif random_operators == '-':
            result = number1 - number2
            return result
        else:
            result = number1 * number2
            return result

    answer = is_calc()

    return str(answer), question
