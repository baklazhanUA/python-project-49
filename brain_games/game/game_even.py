from random import randint


game = 'Answer "yes" if the number is even, otherwise answer "no".'


def function():

    question = randint(0, 20)
    if question % 2 == 0:
        answer = 'yes'

    elif question % 2 != 0:
        answer = 'no'

    return answer, question
