#!/usr/bin/env python3


# Functions
def run_program(registers, program):
    # Variables
    A, B, C = registers
    instructionPointer = 0
    output = []

    # Functions
    def get_combination_operand_value(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        else:
            raise ValueError("Invalid combo operand (7 is reserved).")

    def modulo_eight(value):
        return value % 8

    # Main loop
    while instructionPointer < len(program):
        # Variables
        opcode = program[instructionPointer]
        operand = program[instructionPointer + 1]
        instructionPointer += 2
        # Code
        if opcode == 0:
            denom = 2 ** get_combination_operand_value(operand)
            A = A // denom
        elif opcode == 1:
            B = B ^ operand
        elif opcode == 2:
            B = modulo_eight(get_combination_operand_value(operand))
        elif opcode == 3:
            if A != 0:
                instructionPointer = operand
        elif opcode == 4:
            B = B ^ C
        elif opcode == 5:
            output.append(modulo_eight(get_combination_operand_value(operand)))
        elif opcode == 6:
            denom = 2 ** get_combination_operand_value(operand)
            B = A // denom
        elif opcode == 7:  # cdv
            denom = 2 ** get_combination_operand_value(operand)
            C = A // denom
        else:
            raise ValueError(f"Invalid opcode: {opcode}")
    # Output as string list
    return ",".join(map(str, output))


# Get user input and then output
# Input
print("Enter initial register values (A, B, C) separated by commas: ")
registersInput = input().strip()
registers = tuple(map(int, registersInput.split(',')))
print("Enter program as a comma-separated list of 3-bit numbers: ")
programInput = input().strip()
program = list(map(int, programInput.split(',')))

# Output
output = run_program(registers, program)
print(f"The output is {output}")