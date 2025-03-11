#!/usr/bin/env python3


# Functions
def checksum(diskInput):
    disk = []
    for i in range(0, len(diskInput), 2):
        disk.extend(diskInput[i] * [i // 2])
        if i + 1 < len(diskInput):
            disk.extend(diskInput[i + 1] * [-1])

    empty = [i for i, character in enumerate(disk) if character == -1]
    i = 0
    while True:
        while disk[-1] == -1:
            disk.pop()
        target = empty[i]
        if target >= len(disk):
            break
        disk[target] = disk.pop()
        i += 1

    answer = sum(i * character for i, character in enumerate(disk))
    return answer


# Inout and Output
# Input
diskInput = input("Enter disk map: ").strip()
diskMap = list(map(int, diskInput))
diskInput = "2333133121414131402"
diskMap = list(map(int, diskInput.strip()))
# Output
answer = checksum(diskMap)
print(f"The resulting filesystem checksum is {answer}")
# Answer should be 1928