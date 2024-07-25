# coding_game.py

def game_intro():
    print("Welcome to Code Quest Adventure!")
    print("In this game, you'll solve coding puzzles to advance.")
    print("Type your solutions directly and press Enter to submit.")
    print("You'll earn points for each correct solution.")
    print("Let's get started!\n")

def get_player_input(prompt):
    return input(prompt)

def evaluate_solution(solution, expected_output):
    try:
        player_output = eval(solution)
        return player_output == expected_output, player_output
    except Exception as e:
        return False, str(e)

def give_feedback(is_correct, player_output, expected_output, points):
    if is_correct:
        print(f"Correct! Well done. You earned {points} points.\n")
    else:
        print(f"Incorrect. Your output: {player_output}. Expected: {expected_output}.\n")

def scenario_1(score):
    print("Scenario 1: Basic Arithmetic")
    print("Solve: What is 2 + 2?")
    expected_output = 4
    points = 10
    while True:
        solution = get_player_input("Enter your solution: ")
        is_correct, player_output = evaluate_solution(solution, expected_output)
        give_feedback(is_correct, player_output, expected_output, points)
        if is_correct:
            score += points
            break
    return score

def scenario_2(score):
    print("Scenario 2: String Manipulation")
    print("Solve: Reverse the string 'hello'.")
    expected_output = 'olleh'
    points = 10
    while True:
        solution = get_player_input("Enter your solution: ")
        is_correct, player_output = evaluate_solution(solution, expected_output)
        give_feedback(is_correct, player_output, expected_output, points)
        if is_correct:
            score += points
            break
    return score

def scenario_3(score):
    print("Scenario 3: Looping Constructs")
    print("Solve: Sum all numbers from 1 to 5 (inclusive).")
    expected_output = 15
    points = 10
    while True:
        solution = get_player_input("Enter your solution: ")
        is_correct, player_output = evaluate_solution(solution, expected_output)
        give_feedback(is_correct, player_output, expected_output, points)
        if is_correct:
            score += points
            break
    return score

def scenario_4(score):
    print("Scenario 4: Conditional Statements")
    print("Solve: Check if 10 is greater than 5.")
    expected_output = True
    points = 10
    while True:
        solution = get_player_input("Enter your solution: ")
        is_correct, player_output = evaluate_solution(solution, expected_output)
        give_feedback(is_correct, player_output, expected_output, points)
        if is_correct:
            score += points
            break
    return score

def scenario_5(score):
    print("Scenario 5: Functions")
    print("Solve: Define a function that returns the square of a number.")
    expected_output = 25
    points = 20
    while True:
        solution = get_player_input("Enter your solution (test with 5): ")
        try:
            exec(solution)
            is_correct = 'square(5)' in locals() and square(5) == expected_output
            player_output = square(5) if is_correct else "Function did not return expected output."
            give_feedback(is_correct, player_output, expected_output, points)
            if is_correct:
                score += points
                break
        except Exception as e:
            give_feedback(False, str(e), expected_output, points)
    return score

def scenario_6(score):
    print("Scenario 6: Lists")
    print("Solve: Create a list of numbers from 1 to 5 and get the sum.")
    expected_output = 15
    points = 20
    while True:
        solution = get_player_input("Enter your solution: ")
        try:
            exec(solution)
            is_correct = 'numbers' in locals() and sum(numbers) == expected_output
            player_output = sum(numbers) if is_correct else "Sum did not match expected output."
            give_feedback(is_correct, player_output, expected_output, points)
            if is_correct:
                score += points
                break
        except Exception as e:
            give_feedback(False, str(e), expected_output, points)
    return score

def scenario_7(score):
    print("Scenario 7: Dictionaries")
    print("Solve: Create a dictionary with 'a': 1, 'b': 2, 'c': 3 and return the value of 'b'.")
    expected_output = 2
    points = 20
    while True:
        solution = get_player_input("Enter your solution: ")
        try:
            exec(solution)
            is_correct = 'my_dict' in locals() and my_dict['b'] == expected_output
            player_output = my_dict['b'] if is_correct else "Value did not match expected output."
            give_feedback(is_correct, player_output, expected_output, points)
            if is_correct:
                score += points
                break
        except Exception as e:
            give_feedback(False, str(e), expected_output, points)
    return score

def scenario_8(score):
    print("Scenario 8: File Operations")
    print("Solve: Write 'Hello, World!' to a file named 'hello.txt'.")
    expected_output = 'Hello, World!'
    points = 30
    while True:
        solution = get_player_input("Enter your solution: ")
        try:
            exec(solution)
            with open('hello.txt', 'r') as file:
                content = file.read()
            is_correct = content == expected_output
            player_output = content if is_correct else "File content did not match expected output."
            give_feedback(is_correct, player_output, expected_output, points)
            if is_correct:
                score += points
                break
        except Exception as e:
            give_feedback(False, str(e), expected_output, points)
    return score

def scenario_9(score):
    print("Scenario 9: Exception Handling")
    print("Solve: Write a try-except block that catches a ZeroDivisionError.")
    expected_output = "Caught division by zero!"
    points = 30
    while True:
        solution = get_player_input("Enter your solution: ")
        try:
            exec(solution)
            if 'result' in locals():
                is_correct = result == expected_output
                player_output = result if is_correct else "Output did not match expected output."
                give_feedback(is_correct, player_output, expected_output, points)
                if is_correct:
                    score += points
                    break
        except Exception as e:
            give_feedback(False, str(e), expected_output, points)
    return score

def main():
    game_intro()
    score = 0
    score = scenario_1(score)
    score = scenario_2(score)
    score = scenario_3(score)
    score = scenario_4(score)
    score = scenario_5(score)
    score = scenario_6(score)
    score = scenario_7(score)
    score = scenario_8(score)
    score = scenario_9(score)
    print(f"Congratulations! You've completed the Coding Adventure Game with a score of {score} points.")

if __name__ == "__main__":
    main()
