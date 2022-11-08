import random
from random import randint

game = 'What is the result of the expression?'


def function():

    number1 = randint(0, 999)
    number2 = randint(0, 999)
    a = f'{number1} + {number2}'
    a_answer = number1 + number2
    b = f'{number1} - {number2}'
    b_answer = number1 - number2
    c = f'{number1} * {number2}'
    c_answer = number1 * number2

    list = [a , b , c]
    question = random.choice(list)
    if question == a:
        answer = a_answer
    elif question == b:
        answer = b_answer
    elif question == c:
        answer = c_answer

    return answer, question