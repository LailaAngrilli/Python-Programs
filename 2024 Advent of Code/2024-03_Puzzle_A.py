#!/usr/bin/env python3
import re

# Variables and Et Cetera
mulSequence = ""


def parse_and_sum(stringInput):
    # Extract pattern
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    match = re.findall(pattern, stringInput)

    # Convert pairs from string to integers and then calculate sum
    pairs = [(int(x), int(y)) for x, y in match]
    totalSum = sum(x * y for x, y in pairs)

    # Display Output
    print(f"The mul pairs are: {', '.join(map(str, pairs))} \n")
    print(f"The total sum: {' + '.join(f'{x}*{y}' for x, y in pairs)} = {totalSum}")


mulSequence = str(input("Enter string input: "))
parse_and_sum(mulSequence)