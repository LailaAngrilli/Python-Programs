#!/usr/bin/env python3


# Variables
totalTokens = 0
totalPrizes = 0
details = []
aTokens = 3
bTokens = 1


# Functions
def can_reach_prize(prizeX, prizeY, aX, aY, bX, bY, aTokens, bTokens): # ← Check if prize can be reached
  minTokens = float("inf")
  bestSolution = None
  # Iterate all possible presses of Button A (up to 100)
  for aPresses in range(101):
    if bX == 0 or bY == 0: # <- Avoid devision by 0
      continue
    # Calculate remaining movements
    remainingX = prizeX - aPresses * aX
    remainingY = prizeY - aPresses * aY
    # Ensure remaining movements can be achieved by Button B presses
    if remainingX % bX == 0 and remainingY % bY == 0:
      bPressesX = remainingX // bX
      bPressesY = remainingY // bY
      # Both must match for Button B presses
      if bPressesX == bPressesY and 0 <= bPressesX <= 100:
        tokens = (aTokens * aPresses) + (bTokens * bPressesX)
        if tokens < minTokens:
          minTokens = tokens
          bestSolution = (aPresses, bPressesX)
  if bestSolution:
    return True, bestSolution
  else:
    return False, None

# Collect claw machine info from user
def get_user_input():
  machines = []
  numberOfMachines = int(input("Enter number of claw machines: "))
  for i in range(numberOfMachines):
    print(f"\nEnter details for Claw Machine {i + 1}:")
    aX = int(input("Button A X increment: "))
    aY = int(input("Button A Y increment: "))
    bX = int(input("Button B X increment: "))
    bY = int(input("Button B Y increment: "))
    prizeX = int(input("Prize X location:: "))
    prizeY = int(input("Prize Y location: "))
    machines.append({
      "A": (aX, aY),
      "B": (bX, bY),
      "Prize": (prizeX, prizeY)
    })
  return machines


# Inputs and Outputs
# Inputs
machines = get_user_input()
for i, machine in enumerate(machines):
  # Set variables
  aX, aY = machine["A"]
  bX, bY = machine["B"]
  prizeX, prizeY = machine["Prize"]
  canWin, presses = can_reach_prize(prizeX, prizeY, aX, aY, bX, bY, aTokens, bTokens)

  if canWin:
    aPresses, bPresses = presses
    tokens = (aTokens * aPresses) + (bTokens * bPresses)
    totalTokens += tokens
    totalPrizes += 1
    details.append(f"Machine {i + 1}: Prize won with A: {aPresses} B: {bPresses} (Tokens Used: {tokens})")
  else:
    details.append(f"Machine {i + 1}: Prize cannot be won.")

# Outputs
print("\n\nResults:")
print(f"Total Prizes Won: {totalPrizes}")
print(f"Total Tokens Used: {totalTokens}")
print("\nDetails:")
for detail in details:
  print(f"{detail}")

