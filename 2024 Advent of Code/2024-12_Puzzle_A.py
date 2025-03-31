#!/usr/bin/env python3
import check_user_input


# Functions
def calculate_total_fencing_cost(gardenMap):
    # Variables
    rows = len(gardenMap)
    columns = len(gardenMap[0])
    processed = [[False] * columns for temp in range(rows)]
    totalCost = 0

    # Functions
    # Check if within bounds
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < columns and not processed[x][y]

        # Caluclate area and perimeter using DFS

    def dfs(x, y, plantType):
        plot = [(x, y)]
        area = 0
        perimeter = 0
        processed[x][y] = True
        while plot:
            cx, cy = plot.pop()
            area += 1
            # Check directions (up, donw, left, right)
            for directionX, directionY in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                numberOfX, numberOfY = cx + directionX, cy + directionY
                if is_valid(numberOfX, numberOfY):
                    if gardenMap[numberOfX][numberOfY] == plantType:
                        processed[numberOfX][numberOfY] = True
                        plot.append((numberOfX, numberOfY))
                    else:
                        perimeter += 1
                # Out of bounds contribute to perimeter
                elif not (0 <= numberOfX < rows and 0 <= numberOfY < columns):
                    perimeter += 1
                # Neighbouring plant contribute to perimeter
                elif gardenMap[numberOfX][numberOfY] != plantType:
                    perimeter += 1
        return area, perimeter

    # Calculations
    for i in range(rows):
        for j in range(columns):
            if not processed[i][j]:
                plantType = gardenMap[i][j]
                area, perimeter = dfs(i, j, plantType)
                cost = area * perimeter
                totalCost += cost
                print(f"Region of plant {plantType}: Area = {area}, Perimeter = {perimeter}, Cost = {cost}")
    return totalCost


# Input and Output
# Input
print("Enter the garden map, with each row on a new line.")
print("Press Enter on an empty line to submit.")
gardenMap = []
row = 1
check_user_input.check_enter_on_empty(gardenMap, row)

# Output
if gardenMap:
    totalCost = calculate_total_fencing_cost(gardenMap)
    print(f"The total price for fencing is: {totalCost}")
else:
    print("No garden map provided.")