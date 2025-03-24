#!/usr/bin/env python3


# Variables
blinks = 25


# Functions
def process_stone(stoneInput, blinks):
  stones = stoneInput
  for x in range(blinks):
    newStones = []
    for stone in stones:
      # Rule 1: [See Advent of Code 2024 Day 11]
      if stone == "0":
        newStones.append("1")
      # Rule 2: [See Advent of Code 2024 Day 11]
      elif len(stone) % 2 == 0:
        half = len(stone) // 2
        left = stone[:half].lstrip("0") or "0"
        right = stone[half:].lstrip("0") or "0"
        newStones.extend([left, right])
      # Rule 3: [See Advent of Code 2024 Day 11]
      else:
        newStones.append(str(int(stone) * 2024))
    stones = newStones # <- Updates stone for next blink
  return len(stones)



# Input and Output
# Input
stoneInput = ["125", "17"]
totalStones = process_stone(stoneInput, blinks)

# Output
if blinks == 1:
  print(f"There are {totalStones} after {blinks} blink.")
else:
  print(f"There are {totalStones} after {blinks} blinks.")