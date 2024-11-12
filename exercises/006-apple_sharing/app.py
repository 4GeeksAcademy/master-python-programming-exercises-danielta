import math

def apple_sharing(n,k):
  aps = math.floor(k/n)
  rem = k - (aps * n)
  return aps, rem
 

print(apple_sharing(6,50))
