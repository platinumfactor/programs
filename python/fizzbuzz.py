# The venerable fizzbuzz

import sys

size = int(input('Enter integer range '))

for x in range(size):
  if (x % 3 == 0) and (x % 5 == 0):
    print("fizzbuzz ", x)
  elif (x % 3 == 0):
    print("fizz ", x)
  elif (x % 5 == 0):
    print("buzz ", x)
  else:
    continue
