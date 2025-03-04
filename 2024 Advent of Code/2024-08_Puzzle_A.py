#!/usr/bin/env python3
from collections import defaultdict
from itertools import combinations


# Functions
def count_antinodes(mapInput):
    # Variables
    antenna = defaultdict(set)
    numberOfRows = len(mapInput)
    numberOfColumn = len(mapInput[0])
    antinodes = set()  # <- To store unique antinode positons

    # Find antennas and their positons
    for row, line in enumerate(mapInput):
        for column, character in enumerate(line):
            if character != ".":
                antenna[character].add((row, column))

    # Check for antinodes in each frequency "type"
    for frequency in antenna:
        for (rowOne, columnOne), (rowTwo, columnTwo) in combinations(antenna[frequency], 2):
            antinodes.add((2 * rowOne - rowTwo, 2 * columnOne - columnTwo))
            antinodes.add((2 * rowTwo - rowOne, 2 * columnTwo - columnOne))
    answer = len([1 for r, c in antinodes if 0 <= r < numberOfRows and 0 <= c < numberOfColumn])
    return answer


# Inout and Output
# Input
print("Enter map (using '.' for empty spaces and a single letter/digit for antennas)")
print("Press Enter on an empty line to submit.")
mapInput = []
while True:
    line = input().strip()
    if not line:
        break
    mapInput.append(line)
# Output
answer = count_antinodes(mapInput)
print(f"The number of unique antinode positions is: {answer}")