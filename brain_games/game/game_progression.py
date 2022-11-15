import random
from random import randint

QUESTION = 'What number is missing in the progression?'


def function():

    def progression_generation():
        result = randint(2, 30)
        step_index = randint(2, 9)
        start_i = 0
        stop_i = randint(5, 10)
        result_progression = ''

        while start_i <= stop_i:
            result = result + step_index
            start_i = start_i + 1
            result_progression = result_progression + f'{str(result)} '

        return result_progression

    progression = progression_generation()
    list_progression = progression.split()
    answer = random.choice(list_progression)
    question = progression.replace(answer, '..')
    return answer, question
