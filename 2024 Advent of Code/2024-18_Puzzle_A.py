#!/usr/bin/env python3
from collections import deque


# Functions
def simulate_memory(gridSize, bytePositions, stepsToSimulate):
  grid = [["." for character in range(gridSize)] for character in range(gridSize)]
  for i, (x, y) in enumerate(bytePositions):
    if i >= stepsToSimulate:
      break
    grid[y][x] = "#"
  return grid

def find_shortest_path(grid):
  # Variables
  gridSize = len(grid)
  start = (0, 0)
  end = (gridSize - 1, gridSize - 1)
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  queue = deque([(start, 0)])
  visited = set([start])
  while queue:
    (x, y), steps = queue.popleft()
    # Return number of steps if end is reached
    if (x, y) == end:
      return steps
    # Look at neighbours
    for directionX, directionY in directions:
      newX, newY = x + directionX, y + directionY
      # Stay within bounds
      if 0 <= newX < gridSize and 0 <= newY < gridSize:
        if grid[newY][newX] == "." and (newX, newY) not in visited:
          visited.add((newX, newY))
          queue.append(((newX, newY), steps + 1))
  # If no path, return -1
  return -1


# Input and Output
# Inputs for bytePositions
bytePositions = input("Enter byte positions as a list of tuples (e.g., [(1, 1), (2, 2)]):\n ")
# Convert string into list of tuples
bytePositions = eval(bytePositions)
# Input for number of steps
steps = int(input(f"Enter the number of steps to simulate: "))

# Calculation for gridSize
maxX = max(x for x, y in bytePositions)
maxY = max(y for x, y in bytePositions)
gridSize = max(maxX, maxY) + 1

# Set grid variable
grid = simulate_memory(gridSize, bytePositions, steps)

# Find the shortest path
shortestPathSteps = find_shortest_path(grid)

# Output the results
print("\n")
print(steps)
print(bytePositions)
if shortestPathSteps == -1:
  print("There is no possible path")
elif shortestPathSteps == 1:
  print(f"The shortest path has {shortestPathSteps} step")
else:
  print(f"The shortest path has {shortestPathSteps} steps")
