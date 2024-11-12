# Complete the function to print the last two digits of an integer greater than 9
def last_two_digits(num):
    str_num = str(num) 
    last2 = str_num[len(str_num)-2] + str_num[len(str_num)-1]
    return int(last2)

# Invoke the function with any integer greater than 9
print(last_two_digits(1234))
