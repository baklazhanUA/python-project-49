from random import randint
import math
game = 'Find the greatest common divisor of given numbers.'


def function():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    question = f'{number1} {number2}'
    answer = math.gcd(number1, number2)

    return str(answer), question


print(function())
