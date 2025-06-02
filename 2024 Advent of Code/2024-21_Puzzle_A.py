#!/usr/bin/env python3
from collections  import deque
from itertools import product
import check_user_input


# Variables
numberPad = {
    (0, 0): "7",
    (0, 1): "8",
    (0, 2): "9",
    (1, 0): "4",
    (1, 1): "5",
    (1, 2): "6",
    (2, 0): "1",
    (2, 1): "2",
    (2, 2): "3",
    (3, 1): "0",
    (3, 2): "A",
}

directionalPad = {
    (0, 1): "^",
    (0, 2): "A",
    (1, 0): "<",
    (1, 1): "v",
    (1, 2): ">",
}



# Functions
def find_best_x_to_y(keypad, x, y):
  if x == y:
    return ["A"]
  queue = deque([(*x, "")])
  bestLength = 100
  optimalPaths = []
  while queue:
    row, column, path = queue.popleft()
    for newRow, newColumn, move in [
      (row + 1, column, "v"),
      (row - 1, column, "^"),
      (row, column + 1, ">"),
      (row, column - 1, "<")
    ]:
      if (newRow, newColumn) not in keypad:
        continue
      if len(path) + 1 > bestLength:
        return optimalPaths
      if (newRow, newColumn) == y:
          optimalPaths.append(path + move + "A")
          bestLength = min(len(path) + 2, bestLength)
      else:
          queue.append((newRow, newColumn, path + move))
  return optimalPaths


def keys_to_paths(keypadPaths, code):
    paths = [keypadPaths[(buttonOne, buttonTwo)] for buttonOne, buttonTwo in zip("A" + code, code)]
    return ["".join(segment) for segment in product(*paths)]



# Variables, Input and Ouput
# Variables
numberPadPaths = {
  (numberPad[pathOne],
  numberPad[pathTwo]): find_best_x_to_y(numberPad, pathOne, pathTwo) for pathOne in numberPad for pathTwo in numberPad
}

directionalPadPaths = {
  (directionalPad[pathOne],
  directionalPad[pathTwo]): find_best_x_to_y(directionalPad, pathOne, pathTwo) for pathOne in directionalPad for pathTwo in directionalPad
}

# Input
print("Enter each code, line by line. Press Enter on empty line to submit.\n")
lines = []
line = 0
lines = check_user_input.check_enter_on_empty(lines, line)

# Calulate awnser
complexitiesSum = 0
for code in lines:
  bestLength = float("inf")
  for pathOne in keys_to_paths(numberPadPaths, code):
    for pathTwo in keys_to_paths(directionalPadPaths, pathOne):
      for pathThree in keys_to_paths(directionalPadPaths, pathTwo):
        bestLength = min(len(pathThree), bestLength)
  complexitiesSum += int(code[:-1]) * bestLength

print(f"The sum of the {len(lines)} complexities is: {complexitiesSum}")