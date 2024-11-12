# Complete the function to return the swapped digits of a given two-digit integer
import math
def swap_digits(num):
  number = str(num)[1] + str(num)[0]
  return int(number)
   
# Invoke the function with any two-digit integer as its argument
print(swap_digits(30))
