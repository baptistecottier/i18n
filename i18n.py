"""Global solver for i18n puzzles"""

import sys
import os

if __name__ == '__main__':
    day = sys.argv[1].zfill(2)
    project_path = os.path.abspath(os.getcwd())
    INPUT_PATH = f"{project_path}/puzzles/puzzle_{day}/"
    sys.path.append(INPUT_PATH)
    module = __import__(f"solver_{day}")

    with open(f"{INPUT_PATH}/test_input_{day}.txt", encoding = "utf-8") as file:
        test_input = file.read()
        test_input, expected_test_answer = test_input.rsplit('\n', 1)

    with open(f"{INPUT_PATH}/user_input_{day}.txt", encoding = "utf-8") as file:
        user_input = file.read()

    if 'preprocessing' in dir(module):
        user_input = module.preprocessing(user_input)
        test_input = module.preprocessing(test_input)

    computed_test_answer = str(module.solver(test_input))
    if  computed_test_answer == expected_test_answer:
        print("Test passed ✅")
        print("User answer:", module.solver(user_input))
    else:
        print("Test failed ❌. "
              f"Your answer: {computed_test_answer}. "
              f"Expected answer: {expected_test_answer}")
