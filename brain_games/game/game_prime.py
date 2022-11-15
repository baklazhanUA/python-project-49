from random import randint

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def function():
    question = randint(2, 101)

    def is_prime(number):
        i = 2
        while number % i != 0:
            i = i + 1
        if number == i:
            return True

    if is_prime(question):
        answer = 'yes'
        return answer, question
    elif not is_prime(question):
        answer = 'no'
        return answer, question
