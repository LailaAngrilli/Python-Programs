#!/usr/bin/env python3
import heapq


# Functions
def parse_maze(maze):
    start, end = None, None
    grid = []
    for y, row in enumerate(maze.splitlines()):
        grid.append(row)
        for x, tile in enumerate(row):
            if tile == "S":
                start = (x, y)
            elif tile == "E":
                end = (x, y)
    return grid, start, end


# Return (directionX, directionY) for a given diretion
def direction_delta(direction):
    deltas = {
        "N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0)
    }
    return deltas[direction]


def rotate_direction(current, clockwise):
    directions = ["N", "E", "S", "W"]
    indexDirection = directions.index(current)
    if clockwise:
        return directions[(indexDirection + 1) % 4]
    else:
        return directions[(indexDirection - 1) % 4]


# anhattan distance heuristic
def heuristic(e, y, end):
    endX, endY = end
    return abs(x - endX) + abd(y - endY)


def find_lowest_score(maze):
    # Variables
    grid, start, end = parse_maze(maze)
    startX, startY = start
    endX, endY = end
    visited = set()
    priorityQueue = []
    heapq.heappush(priorityQueue, (0, startX, startY, "E"))  # <- Start facing east

    while priorityQueue:
        score, x, y, direction = heapq.heappop(priorityQueue)
        # Return score if reach end
        if (x, y) == end:
            return score
        # Skip if visited
        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))
        # Try moving forward
        directionX, directionY = direction_delta(direction)
        newX, newY = x + directionX, y + directionY
        if grid[newY][newX] != "#":
            heapq.heappush(priorityQueue, (score + 1, newX, newY, direction))
        # Try rotating clockwise
        newDirection = rotate_direction(direction, clockwise=True)
        heapq.heappush(priorityQueue, (score + 1000, x, y, newDirection))
        # Try rotating counterclockwise
        newDirection = rotate_direction(direction, clockwise=False)
        heapq.heappush(priorityQueue, (score + 1000, x, y, newDirection))


def get_maze():
    print("Enter the maze, line by line, and submit by pressing Enter on an empty line:\n ")
    mazeLines = []
    while True:
        line = input()
        if not line.strip():
            break
        mazeLines.append(line)
    return "\n".join(mazeLines)


# Input and output the answer
# Input
userMazeInput = get_maze()
answer = find_lowest_score(userMazeInput)

# Output
print(f"\nThe lowest score is {answer}")