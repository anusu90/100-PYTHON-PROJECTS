#First we import math module

import math

#Then we need to take input from the user
n = int(input('Enter the number of digits after decimal that needs to be printed: '))

pi = math.pi

# Now two posibilities emerege:
# 1. we round of:
# 2. we dont round of:

piDigitRounded = round(pi,n)
piDigitNotRounded = float(str(pi)[:n+2])

#printing the output

print(f'the value of pi upto {n} digits when rounded off is {piDigitRounded} and when not rounded off is {piDigitNotRounded}')
