from random import randint

game = 'Find the greatest common divisor of given numbers.'


def function():

    number1 = randint(0, 100)
    number2 = randint(0, 100)
    question = f'{number1} {number2}'

    if number1 != 0 and number2 != 0:

        if number1 > number2:
            a = number1 % number2
            answer = number2 % a

        elif number1 < number2:
            a = number2 % number1
            answer = number1 % a

    return str(answer), question
