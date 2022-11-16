from random import randint

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def get_game():
    question = randint(1, 20)

    if is_even(question):
        answer = 'yes'
    elif not is_even(question):
        answer = 'no'

    return answer, question
