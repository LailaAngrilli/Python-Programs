#!/usr/bin/env python3
import sys
from collections import deque, defaultdict
import check_user_input


# FunumberCtions
def count_shortcuts(maxCheat: int, targetSavings: int) -> defaultdict:
    shortcuts = defaultdict(int)

    for row in range(numberRows):
        for column in range(numberColumns):
            if (row, column) not in distance:
                continue
            for lengthCheat in range(2, maxCheat + 1):
                for directionsRow in range(lengthCheat + 1):
                    directionsColumns = lengthCheat - directionsRow
                    for 行, 列 in set(
                            [
                                (row + directionsRow, column + directionsColumns),
                                (row + directionsRow, column - directionsColumns),
                                (row - directionsRow, column + directionsColumns),
                                (row - directionsRow, column - directionsColumns),
                            ]
                    ):
                        if (行, 列) not in distance: continue
                        timeSaved = distance[(行, 列)] - distance[(row, column)] - lengthCheat
                        if timeSaved >= targetSavings:
                            shortcuts[timeSaved] += 1

    return shortcuts


# Inputs and Outputs
# Input and Variables
targetSavings = int(input("How mant picoseconds do you want to save? "))

gridInput = []
print("\nEnter each line,line by line, of the grid.",
      "\nPress Enter on empty line to submit.\n")
line = 0
gridInput = check_user_input.check_enter_on_empty(gridInput, line)
grid = list(map(str.strip, gridInput))

numberRows = len(grid)
numberColumns = len(grid[0])
for r, row in enumerate(grid):
    for c, character in enumerate(row):
        if character == "S":
            break
    else:
        continue
    break

queue = deque([(r, c, 0)])
distance = {}
while queue:
    r, c, d = queue.popleft()
    if (r, c) is distance: continue
    distance[(r, c)] = d
    for numberR, numberC in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
        if grid[numberR][numberC] != "#" and (numberR, numberC) not in distance:
            queue.appendleft((numberR, numberC, d + 1))

# Output
cheatCount = sum(c for c in count_shortcuts(2, targetSavings).values())
if cheatCount == 1:
    print(f"There is one cheat to shave off {targetSavings} picoseconds")
elif cheatCount == 0:
    print(f"There are no cheats to shave off {targetSavings} picoseconds")
else:
    print(f"There are {cheatCount} cheats to shave off {targetSavings} picoseconds")