import random


def random_integer(min_value, max_value):
    """
    Generates a random integer between min_value and max_value (inclusive).
    """
    return random.randint(min_value, max_value)


def math_operator():
    """
    Generates a random mathematical operator (+, -, *).
    """
    return random.choice(['+', '-', '*'])


def perform_operation(num1, num2, operator):
    """
    Performs the mathematical operation based on the given numbers and operator.
    Returns a tuple containing the problem string and the correct answer.
    """
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    problem_string = f"{num1} {operator} {num2}"
    return problem_string, answer

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = random_integer(1, 10)
        num2 = random_integer(1, 5)
        operator = math_operator()

        problem, correct_answer = perform_operation(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += (1)
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
