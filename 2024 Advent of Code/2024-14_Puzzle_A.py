#!/usr/bin/env python3
import sys

# Variables
gridWidth = 101
gridHeight = 103
seconds = 100


# Functions
def get_robot_data(userInput):
    robots = []
    for line in userInput.strip().split("\n"):
        position, velocity = line.split(" v=")
        positionX, positionY = map(int, position[2:].split(","))
        velocityX, velocityY = map(int, velocity.split(","))
        robots.append(((positionX, positionY), (velocityX, velocityY)))
    return robots


def update_positions(robots, gridWidth, gridHeight, seconds):
    newPositions = []
    for (positionX, positionY), (velocityX, velocityY) in robots:
        newX = (positionX + velocityX * seconds) % gridWidth
        newY = (positionY + velocityY * seconds) % gridHeight
        newPositions.append((newX, newY))
    return newPositions


def count_robots_in_quadrants(position, gridWidth, gridHeight):
    midX, midY = gridWidth // 2, gridHeight // 2
    quadrant_counts = [0, 0, 0, 0]
    for x, y in position:
        if x == midX or y == midY:  # Ignore if on middle line
            continue
        elif x < midX and y < midY:  # Top Left
            quadrant_counts[0] += 1
        elif x >= midX and y < midY:  # Top Right
            quadrant_counts[1] += 1
        elif x < midX and y >= midY:  # Bottom Left
            quadrant_counts[2] += 1
        elif x >= midX and y >= midY:  # Bottom Right
            quadrant_counts[3] += 1
    return quadrant_counts


def calculate_safety_factor(quadrant_counts):
    factor = 1
    for count in quadrant_counts:
        factor *= count
    return factor


# Input and Output
# Input
print("Enter robot data, one robot per line (Ctrl + D or Ctrl + Z to submit)): ")
userInput = sys.stdin.read()
robots = get_robot_data(userInput)
positionsAfterTime = update_positions(robots, gridWidth, gridHeight, seconds)
quadrantCounts = count_robots_in_quadrants(positionsAfterTime, gridWidth, gridHeight)
safetyFactor = calculate_safety_factor(quadrantCounts)

# Output
print(f"Safety Factor: {safetyFactor}")