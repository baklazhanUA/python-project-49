from random import randint
import prompt


def main():
    counter = 1
    random_number = randint(1, 99)

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while counter <= 3:
        print(f'Question: {random_number}')
        answer = input('Your answer: ')

        if random_number % 2 == 0 and answer.lower() == 'yes':
            print('Correct!')
            counter = counter + 1
            random_number = randint(1, 99)

        elif random_number % 2 == 0 and answer.lower() == 'no':
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print("Let's try again, ", name, "!")
            return

        elif random_number % 2 != 0 and answer.lower() == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, ", name, "!")
            return

        elif random_number % 2 != 0 and answer.lower() == 'no':
            print('Correct!')
            counter = counter + 1
            random_number = randint(1, 99)
        else:
            print(answer, "= ERROR | Answer 'yes' or 'no'")
            return

    print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
