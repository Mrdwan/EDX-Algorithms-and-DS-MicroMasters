# Input format: Integers a and b on the same line (separated by a space).
# Output format: The sum of a and b
# Constraints : 0 <= a, b <= 9
# Sample:
#   Input: 9 7
#   Output: 16

import sys

input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
print(a + b)