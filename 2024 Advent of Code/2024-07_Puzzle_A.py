#!/usr/bin/env python3
from itertools import product

# Variables
inputs = []


# Functions
def evaluate_left_to_right(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
    return result


def find_equation(result, numbers):
    operators = ["+", "*"]
    numberOfOperators = len(numbers) - 1
    equations = []

    # Generate all possble combination of operators
    for operatorsInEquation in product(operators, repeat=numberOfOperators):
        if evaluate_left_to_right(numbers, operatorsInEquation) == result:
            equation = str(numbers[0])
            for i, operator in enumerate(operatorsInEquation):
                equation += f" {operator} {numbers[i + 1]}"
            equations.append(equation)
    return equations


# Input and Output
# Ask for input
print("Enter inputs in the format 'RESULT: NUMBER NUMBER [NUMBER...]'")
print("Press Enter on an empty line to submit.")
while True:
    userInput = input().strip()
    if not userInput:
        break
    if ":" not in userInput:
        print("Input is not in the correct format. Please try again.")
        continue
    try:
        result, numbers = userInput.split(":")
        result = int(result.strip())
        numbers = list(map(int, numbers.strip().split()))
        inputs.append((result, numbers))
    except ValueError:
        print("Invalid format. Please try again.")

# Prcess Input
for result, numbers in inputs:
    equations = find_equation(result, numbers)
    if equations:
        print(f"{result}")
        for equation in equations:
            print(f"- {equation}")
        print("\n")
    else:
        print(f"No equations found for {result} with numbers {numbers}\n")