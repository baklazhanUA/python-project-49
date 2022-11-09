from random import randint

game = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def function():
    question = randint(2, 101)
    i = 2
    while question % i != 0:
        i = i + 1
        if question == i:
            answer = 'yes'
            return answer, question

    answer = 'no'
    return answer, question
