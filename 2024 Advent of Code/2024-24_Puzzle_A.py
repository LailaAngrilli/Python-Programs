#!/usr/bin/env python3


# Functions
def simulate_gates(inputValues, gateDefinitions):
    # Variables
    wires = {}
    gates = []

    # Parse wires
    for wire, value in inputValues.items():
        wires[wire] = int(value)

    # Parse and process gates
    for definition in gateDefinitions:
        try:
            parts = definition.split(" -> ")
            if len(parts) != 2:
                raise ValueError(f"Invalid gate definition: {definition}")
            operation = parts[0]
            outputWire = parts[1]
            if " AND " in operation:
                a, b = operation.split(" AND ")
                gates.append((a, b, "AND", outputWire))
            elif " OR " in operation:
                a, b = operation.split(" OR ")
                gates.append((a, b, "OR", outputWire))
            elif " XOR " in operation:
                a, b = operation.split(" XOR ")
                gates.append((a, b, "XOR", outputWire))
            else:
                raise ValueError(f"Unknown operation in: {operation}")
        except ValueError as e:
            print(f"Error parsing gate definition: {definition}")
            raise e

    # Evaluate outputs
    unresolvedGates = gates
    while unresolvedGates:
        resolvedGates = []
        for a, b, op, output in unresolvedGates:
            if a in wires and b in wires:
                if op == "AND":
                    wires[output] = wires[a] & wires[b]
                elif op == "OR":
                    wires[output] = wires[a] | wires[b]
                elif op == "XOR":
                    wires[output] = wires[a] ^ wires[b]
                resolvedGates.append((a, b, op, output))
        unresolvedGates = [gate for gate in unresolvedGates if gate not in resolvedGates]

    # Z-Wire Outputs
    zWires = {k: v for k, v in wires.items() if k.startswith('z')}
    maxIndex = max(int(k[1:]) for k in zWires)  # Find the largest suffix
    binaryDigits = [str(zWires.get(f"z{i:02}", 0)) for i in range(maxIndex + 1)]

    # Decimal Conversion
    binaryNumber = "".join(reversed(binaryDigits))
    return int(binaryNumber, 2)


def get_user_input():
    # Get wires
    print("Enter initial wire values (e.g., x00: 1, y01: 0).",
          "\nPress Enter on empty line to submit.")
    inputValues = {}
    while True:
        line = input("Wire value: ").strip()
        if not line:
            break
        if ":" in line:
            wire, value = line.split(":")
            inputValues[wire.strip()] = int(value.strip())
        else:
            print("Invalid format. Please use 'wire: value' format.")

    # Get gates
    print("Enter gate definitions (e.g., x00 AND y00 -> z00).",
          "\nPress Enter on empty line to submit.")
    gateDefinitions = []
    while True:
        line = input("Gate definition: ").strip()
        if not line:
            break
        if "->" in line:
            gateDefinitions.append(line)
        else:
            print("Invalid format. Please use 'input OPERATOR input -> output' format.")

    return inputValues, gateDefinitions


# Get inputs and outputs
inputValues, gateDefinitions = get_user_input()
output = simulate_gates(inputValues, gateDefinitions)
print(f"\nThe decimal output is: {output}")
