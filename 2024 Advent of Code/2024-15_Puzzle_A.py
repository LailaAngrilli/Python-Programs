#!/usr/bin/env python3


# Variables + Inputs
# Grid input
print("Enter the grid (press Enter on empty line to submit): \n")
gridInput = []
while True:
    row = input()
    if row.strip() == "":
        break
    gridInput.append(row.strip())
grid = [list(row) for row in gridInput]
# Moves input
moves = input("Enter the moves (all one line, no spaces): \n").strip().replace(" ", "")
# Moves map
moveMap = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}


# Main
for r, row in enumerate(grid):
  for c, character in enumerate(row):
    if character == "@":
      break
  else:
    continue
  break

for move in moves:
  # Variables
  directionRow, directionColumn = moveMap[move]
  newRow, newColumn = r + directionRow, c + directionColumn
  doMove = True
  while True:
    if grid[newRow][newColumn] == "#":
      doMove = False
      break
    if grid[newRow][newColumn] == ".":
      break
    if grid[newRow][newColumn] == "O":
      newRow, newColumn = newRow + directionRow, newColumn + directionColumn
    else:
      assert False
  if not doMove:
        continue
  grid[r][c] = "."
  r, c = r + directionRow, c + directionColumn
  if grid[r][c] == "O":
        grid[newRow][newColumn] = "O"
  grid[r][c] = "@"

# Calculate ad output the answer
answer = sum(
    r * 100 + c for r,
    row in enumerate(grid) for c,
    character in enumerate(row) if character == "O"
)
print(f"\nThe sum of all boxes' GPS coordinates is {answer}")