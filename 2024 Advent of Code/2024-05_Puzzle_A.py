#!/usr/bin/env python3


# Functions
# Get rules
def get_rules():
    print("Enter rule order in X|Y format. Press Enter on empty line when done. ")
    rules = []
    while True:
        ruleInput = input().strip()
        if not ruleInput:  # ← Stop when pressed Enter on empty line
            break
        if "|" in ruleInput:
            try:
                x, y = map(int, ruleInput.split("|"))
                rules.append((x, y))
            except ValueError:
                print("Invalid input. Inputs must be integers in the format X|Y ")
        else:
            print("Invalid input. Inputs must be integers in the format X|Y ")
    return rules


# Get pages by update
def get_pages():
    print("Enter pages in each update, seperated by comma. Press Enter on empty line when done\n")
    pages = []
    while True:
        pageInput = input().strip()
        if not pageInput:  # ← Stop when pressed Enter on empty line
            break
        try:
            pagesByUpdate = list(map(int, pageInput.split(",")))
            pages.append(pagesByUpdate)
        except ValueError:
            print("Invalid input. Inputs must be integers sperated by commas.\n")
    return pages


# Check if in correct order
def check_order(pages, rules):
    for x, y in rules:
        if x in pages and y in pages:
            if pages.index(x) > pages.index(y):
                return False, f"Breaks Rule {x}|{y}"
    return True, "Correct Order"


# Get middle number and calcualte the sum
def get_middle_and_sum(correctOrder):
    middleNumbers = []
    for pages in correctOrder:
        middleIndex = len(pages) // 2
        middleNumbers.append(pages[middleIndex])
    return middleNumbers, sum(middleNumbers)


# Ask for input and generate output
rules = get_rules()
pages = get_pages()
correctOrder = []
# Prints which are correct and which are incorrect based on rules
for i, pages in enumerate(pages, start = 1):
    isCorrect, message = check_order(pages, rules)
    if isCorrect:
        correctOrder.append(pages)
        print(f"Update {i}: Correct Order")
    else:
        print(f"Update {i}: Not in the Correct Order -- {message}")
print("\n")

# Prints correct order only
print("Updates in Correct Order")
for pages in correctOrder:
    print(pages)
print("\n")

# Print middle and sum
middleNumbers, totalSum = get_middle_and_sum(correctOrder)
print(f"Middle Numbers: {middleNumbers}")
print(f"Total sum of middle numbers: {totalSum}")
