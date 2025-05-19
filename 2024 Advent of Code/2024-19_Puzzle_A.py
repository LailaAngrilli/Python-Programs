#!/usr/bin/env python3
import sys


# Functions
def get_user_input():
    print("Enter the data in the following format:",
          "\nFirst Line: Towel patterns seperated by comma (e.g., PatternOne, PatternTwo)",
          "\nSecond Line: Blank",
          "\nSubsequent Lines: Desired designs (one per line)",
          "\nTo Submit: Press Enter on empty line to submit."
          )
    try:
        userInput = sys.stdin.read().strip()  # <- Read user input
        # Check format
        if "\n\n" not in userInput:
            raise ValueError("Invalid input format. Ensure towel patterns and designs are separated by a blank line.")
        return userInput
    except EOFError:
        raise ValueError("Please ensure the format is correct.")


def parse_input(inputData):
    # Split into patterns and designs
    parts = inputData.strip().split("\n\n")
    if len(parts) < 2:
        raise ValueError("Invalid input format. Ensure towel patterns and designs are separated by a blank line.")
    towelPatterns = parts[0].split(", ")
    designs = parts[1].split("\n")
    return towelPatterns, designs


def can_construct(design, patterns, memo):
    # Check if design can be constructed
    if design in memo:
        return memo[design]
    if not design:  # ← If empty
        return True

    for pattern in patterns:
        if design.startswith(pattern):
            remainder = design[len(pattern):]
            if can_construct(remainder, patterns, memo):
                memo[design] = True
                return True

    memo[design] = False
    return False


def count_possible_designs(inputData):
    # Variables
    towelPatterns, designs = parse_input(inputData)
    count = 0
    memo = {}

    for design in designs:
        if can_construct(design, towelPatterns, memo):
            count += 1

    return count


# Input and Output
# Input
userInput = get_user_input()
answer = count_possible_designs(userInput)

# Output
print(f"Number of possible designs: {answer}")