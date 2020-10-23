import random
import operator


def random_problem():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)

    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num_1, num_2)
    print('What is {} {} {}?'.format(num_1, operation, num_2))

    return answer


def ask_question():
    answer = random_problem()
    guess = float(input())
    return guess == answer


def game():
    print('How well do you know math?\n')
    score = 0

    for _ in range(5):
        if ask_question() == True:
            score += 1
            print('Correct!')
        else:
            print('Incorrect!')
    print('Your score is {}'.format(score))


game()