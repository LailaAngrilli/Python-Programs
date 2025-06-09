#!/usr/bin/env python3


# Functions
def next_number(x: int) -> int:
    x ^= (x * 64) % 16777216
    x ^= (x // 32) % 16777216
    x ^= (x * 2048) % 16777216
    return x


# Input anf Output
# Input
numberGeneration = int(input("How many new secret numbers should be generated? "))
numbersInput = []
print("\nEnter each number, line by line.",
      "\nPress Enter on an empty line to submit.")

while True:
    line = input().strip()
    if not line:
        break
    try:
        numbersInput.append(int(line))
    except ValueError:
        print("Please enter a valid integer.")

# Calculate answer
answer = 0
for number in numbersInput:
    for 番号 in range(2000):
        number = next_number(number)
    answer += number

# Output
print(f"The sum of the secret numbers is {answer}")
