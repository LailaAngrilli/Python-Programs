#!/usr/bin/env python3
from collections import deque


def get_map():
  print("Enter the topographical map row by row, using 0-9 to indicate the height.")
  print("Press Enter on empty line to submit: ")
  mapInput = []
  while True:
    row = input().strip()
    if not row:  # ← Ends input when empty line
      break
    mapInput.append([int(character) for character in row])
  return mapInput

def find_trailheads(mapInput):
  trailheads = []
  for i, row in enumerate(mapInput):
    for j, heightValue in enumerate(row):
      if heightValue == 0:  # ← Identify trailheads (i.e., 0-heights)
        trailheads.append((i, j))
  return trailheads

def calculate_trailhead_score(mapInput, trailhead):
  rows, columns = len(mapInput), len(mapInput[0])
  directions = [
    (-1, 0), # Up
    (1, 0),  # Down
    (0, -1), # Left
    (0, 1)   # Right
  ]
  queue = deque([trailhead])
  visited = set()
  score = 0
  visited.add(trailhead)
  while queue:
    x, y = queue.popleft()
    currentHeight = mapInput[x][y]
    for directionX, directionY in directions:
      numberX, numberY = x + directionX, y + directionY
       # Check bounds and height increment
      if 0 <= numberX < rows and 0 <= numberY < columns and (numberX, numberY) not in visited:
        if mapInput[numberX][numberY] == currentHeight + 1:
          queue.append((numberX, numberY))
          visited.add((numberX, numberY))
          # ← Identify trailheads (i.e., 0-heights
          if mapInput [numberX][numberY] == 9:
            score += 1
  return score


# Inputs and Outputs
# Inputs
mapInput = get_map()
trailheads = find_trailheads(mapInput)
totalScore = 0
scores = []
for trailhead in trailheads:
  score = calculate_trailhead_score(mapInput, trailhead)
  scores.append(score)
  totalScore += score

# Outputs
print(f"\nThere are {len(trailheads)} trailheads.")
print(f"The trailhead scores are: {', '.join(map(str, scores))}.")
print(f"The total sum of the scores of all trailheads is {totalScore}.")