from random import randint
import math

QUESTION = 'Find the greatest common divisor of given numbers.'


def get_game():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    question = f'{number1} {number2}'
    answer = math.gcd(number1, number2)

    return str(answer), question
