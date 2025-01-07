#!/usr/bin/env python3

# Create Variables, Lists and Sort Them
# Group Variables
listGroupA = []
listGroupB = []
# Other Variables
length = 0
listDistance = []
totalDistance = 0


# Get inputs
# Get input for length of lists
while True:
  try:
    length = int(input("How many numbers do you want the list to be? "))
  except ValueError:
    print("That's not a whole number. Try again!")
    continue
  else:
    break

# Get input for listGroupA
print("What numbers would you like to add to Group A? (Add numbers individually)")
i = 0
while i < length:
  while True:
    try:
      temp = int(input("Number: "))
    except ValueError:
      print("That's not a whole number. Try again!")
      continue
    else:
      i += 1
      listGroupA.append(temp)
      break
print(listGroupA)

# Get input for listGroupB
print("What numbers would you like to add to Group B? (Add numbers individually)")
i = 0
while i < length:
  while True:
    try:
      temp = int(input("Number: "))
    except ValueError:
      print("That's not a whole number. Try again!")
      continue
    else:
      i += 1
      listGroupB.append(temp)
      break
print(listGroupB)


# Main Code
listGroupA.sort()
listGroupB.sort()
# Add differences to list listDistance
i = 0
while i < length:
  listDistance.append(abs(listGroupA[i] - listGroupB[i]))
  i += 1

# Calculate sum of distance
for x in listDistance:
  totalDistance += x


# Fancy Output Results
tempDistances = map(str, listDistance)
tempOutput = " + ".join(tempDistances)
print("\n \n")
print("Sort Groups:")
print(listGroupA)
print(listGroupB)
print("\n")
print("Distance Sum:")
print(tempOutput + " = " + str(totalDistance))
