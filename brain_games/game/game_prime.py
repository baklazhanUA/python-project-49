from random import randint

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    i = 2
    while number % i != 0:
        i = i + 1
    if number == i:
        return True


def get_game():
    question = randint(2, 101)

    if is_prime(question):
        answer = 'yes'

    else:
        answer = 'no'

    return answer, question
