#!/usr/bin/env python3


# Functions
# Function to get word search text
def word_search():
  print("Enter the word search text, row by row, \nand then press Enter on an empty line when done")
  wordSearchText = []
  while True:
      row = input().strip().upper()
      if not row:  # ← Stop when pressed Enter on empty line
          break
      wordSearchText.append(row)
  return wordSearchText

# Funtion to find and count how many times {word} appears
def find_word(text, word):
  # Variables
  rows = len(text)
  columns = len(text[0]) if rows > 0 else 0
  wordLength = len(word)
  count = 0
  directions = [
      (0, 1),   # Right
      (1, 0),   # Down
      (1, 1),   # Down-Right
      (1, -1),  # Down-Left
      (0, -1),  # Left
      (-1, 0),  # Up
      (-1, -1), # Up-left
      (-1, 1)   # Up-right
  ]

  for row in range(rows):
    for column in range(columns):
      for directionRow, directionColumn in directions:
        # Check if the word fits within the grid boundariess
        if 0 <= row + directionRow * (wordLength - 1) < rows and 0 <= column + directionColumn * (wordLength - 1) < columns:
          check = True
          for i in range(wordLength):
            if text[row + i * directionRow][column + i * directionColumn] != word[i]:
              check = False
              break
          if check:
            count += 1

  return count



# Get inputs
wordSearchText = word_search()
word = input("What word are you searching for? ").strip().upper()
count = find_word(wordSearchText, word)

# Output
print("\n")
if count == 1:
  print(f"{word} appears {count} time in this word search.")
else:
  print(f"{word} appears {count} times in this word search.")