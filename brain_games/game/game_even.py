from random import randint

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def function():
    question = randint(1, 20)

    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False

    if is_even(question):
        answer = 'yes'
    elif not is_even(question):
        answer = 'no'

    return answer, question
