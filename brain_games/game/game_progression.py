from random import randint

game = 'What number is missing in the progression?'


def function():
    result = randint(2, 30)
    step_index = randint(2, 9)
    start_i = 0
    stop_i = randint(5, 10)
    question = ''
    random = randint(1, stop_i)
    answer = ''

    while start_i <= stop_i:

        result = result + step_index
        start_i = start_i + 1
        question = question + f'{str(result)} '
        if random == start_i:
            result = result + step_index
            start_i = start_i + 1
            question = question + '.. '
            answer = result

    return answer, question
