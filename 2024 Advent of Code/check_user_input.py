#!/usr/bin/env python3

def check_integer(prompt):
    while True:
      try:
        userInput = int(input(prompt))
      except ValueError:
        print("That's not a while number. Try again!")
        continue
      else:
        return userInput

def check_enter_on_empty(listName, variableName):
  while True:
    variableName = input().strip()
    if not variableName:  # ← Stop when pressed Enter on empty line
      break
    listName.append(variableName)
  return listName