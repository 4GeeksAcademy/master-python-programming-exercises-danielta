# Complete the function to return the total cost in dollars and cents of (n) cupcakes
import math
def total_cost(d, c, n):
    # cpc = float(str(d)+'.'+str(c))
    # cpc = d + (c/100)
    # cost = cpc * n
    cents = int(str(c*n)[-2]+str(c*n)[-1])
    dollars = d*n + math.floor((c*n)/100)
    return dollars, cents





# Invoke the function with three integers: total_cost(dollars, cents, number_of_cupcakes)
print(total_cost(15,22,4))
