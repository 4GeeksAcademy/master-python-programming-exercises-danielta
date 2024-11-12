# Complete the function to return the tens digit of a given integer
def tens_digit(num):
  tenth = str(num)[len(str(num))-2]
  return int(tenth)


# Invoke the function with any integer
print(tens_digit(179))
