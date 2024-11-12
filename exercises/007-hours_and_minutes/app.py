import math
def hours_minutes(seconds):
  hours = math.floor(seconds/3600)
  minutes = math.floor((seconds - (hours * 3600))/60)
  return hours, minutes

# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
