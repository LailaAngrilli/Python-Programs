#!/usr/bin/env python3


# Functions
def parse_map(mapInput):
    grid = [list(row) for row in mapInput.splitlines()]
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}  # ← Needs to be in this order, otherwise doesn't work properly

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in directions:
                return grid, (i, j), directions[cell]

    raise ValueError("Map must contain a guard (indicated with either ^, v, > or <)")


# Simulate the guard's movement and mark them
def move_guard(grid, start, direction):
    # Set up stuff
    rows, columns = len(grid), len(grid[0])
    directions = ["^", ">", "v", "<"]  # ← Needs to be in this order, otherwise doesn't work properly
    directionCoordinates = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # ← Needs to be in this order, otherwise doesn't work properly
    x, y = start
    directionIndex = directionCoordinates.index(direction)
    visited = set()

    # Mark visited potions with X and determine next position
    while 0 <= x < rows and 0 <= y < columns:
        visited.add((x, y))
        if grid[x][y] != "#":
            grid[x][y] = "X"
        # Determine next position
        directionX, directionY = directionCoordinates[directionIndex]
        nextPositionX, nextPositionY = x + directionX, y + directionY
        # Movement (Turn right if obstructed, else go forward)
        if 0 <= nextPositionX < rows and 0 <= nextPositionY < columns and grid[nextPositionX][nextPositionY] == "#":
            directionIndex = (directionIndex + 1) % 4
        else:
            x, y = nextPositionX, nextPositionY
    return visited


# Inputs and Outputs
print("Enter the map (for free spaces use '.', for obstructions use '#' and for the guard use '^', 'v', '<' or '>').")
print("Press Enter on empty line to submit: ")
mapInput = ""
while True:
    line = input()
    if not line.strip():
        break
    mapInput += line + "\n"

grid, start, direction = parse_map(mapInput.strip())
visitedPositions = move_guard(grid, start, direction)

print("Positions Guard Has Visited:")
for row in grid:
    print("".join(row))
print(f"The guard has visited {len(visitedPositions)} distinct positions.")