# Complete the function to return the tens digit and the units digit of any interger
import math
def two_digits(number):
  tens = math.floor(number/10)
  units = number - (tens*10)
  return tens, units
   

# Invoke the function with any two digit integer as its argument
print(two_digits(79))
