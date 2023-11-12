import unittest
from math_quiz import random_integer, math_operator, perform_operation

class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_value = 1
        max_value = 10
        for _ in range(1000):  # Test a large number of random values
            random_num = random_integer(min_value, max_value)
            self.assertTrue(min_value <= random_num <= max_value)

    def test_math_operator(self):
        # Test if the generated operator is one of the expected values
        valid_operators = {'+', '-', '*'}
        generated_operator = math_operator()
        self.assertIn(generated_operator, valid_operators)

    def test_perform_operation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 4, '-', '8 - 4', 4),
            (3, 2, '*', '3 * 2', 6),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = perform_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
