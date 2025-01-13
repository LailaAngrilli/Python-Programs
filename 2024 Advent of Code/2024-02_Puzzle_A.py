#!/usr/bin/env python3
import check_user_input


# Functions
def get_matrix_input():
    # Get input for number of rows and number of numbers per row
    rowNumber = check_user_input.check_integer("Enter the number of rows: ")
    numberPerRow = check_user_input.check_integer("Enter the number of numbers per rows: ")

    rowStorage = []
    # Create rows
    for i in range(rowNumber):
        print(f"Enter the numbers for row {i + 1}: ")
        row = []
        while len(row) < numberPerRow:
            try:
                # Collect the individual numbers
                number = int(input(f"Enter number {len(row) + 1} for row {i + 1}: "))
                row.append(number)
            except ValueError:
                print("That's not a while number. Try again!")
        rowStorage.append(row)
    return rowStorage


def is_row_safe(row):
    # Check if increasing or decreasing
    rowIncreasing = all(row[i] < row[i + 1] for i in range(len(row) - 1))
    rowDecreasing = all(row[i] > row[i + 1] for i in range(len(row) - 1))
    if not (rowIncreasing or rowDecreasing):
        return False

    # Check if differences are within 1-3
    return all(1 <= abs(row[i] - row[i + 1]) <= 3 for i in range(len(row) - 1))


# Counts number of safe reports
def count_safe(matrix):
    safeCounter = 0
    for row in matrix:
        if is_row_safe(row):
            safeCounter += 1
    return safeCounter


# Run functions and output number
reportMatrix = get_matrix_input()
safeReportsNumber = count_safe(reportMatrix)
if safeReportsNumber == 1:
    print(f"{safeReportsNumber} report is safe.")
else:
    print(f"{safeReportsNumber} reports are safe.")
