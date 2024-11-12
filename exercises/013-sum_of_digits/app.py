# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
  first = str(num)[0]
  second = str(num)[1]
  third = str(num)[2]
  return int(first)+int(second)+int(third)


# Invoke the function with any three-digit number
print(digits_sum(123))
