#!/usr/bin/env python3
from collections import defaultdict
import check_user_input


# Functions
def find_triples_with_t(connections):
  # Create the networkMap
  networkMap = defaultdict(set)
  for connection in connections:
    a, b = connection.split("-") # a = computerOne, b = computerTwo
    networkMap[a].add(b)
    networkMap[b].add(a)
  # Find all triples-- or whatever a group of three is called
  triples = set()
  for a in networkMap:
    for b in networkMap[a]:
      if b > a:
        for c in networkMap[b]:
          if c > b and c in networkMap[a]:
            triple = tuple(sorted([a, b, c]))
            triples.add(triple)
  # Find those with T
  triples_with_t = [triple for triple in triples if any(node.startswith('t') for node in triple)]
  return len(triples_with_t), triples_with_t



# Inputs and variables and outputs
# Inputs and variables
print(
  "Enter connections, one per line.",
  "\nPress Enter on empty to submit."
)
connections = []
line = 0
connections = check_user_input.check_enter_on_empty(connections, line)
numberOftriples, triples = find_triples_with_t(connections)

# Output
print(f"\nNumber of triples with 'T': {numberOftriples}")
print("Triples:")
for triple in triples:
   print(triple)


