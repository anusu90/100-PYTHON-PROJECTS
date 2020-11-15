#First we import math module and declare pi
import math
pi = math.pi

def piDigits (n):
    # Now two posibilities emerege:
    # 1. we round of:
    # 2. we dont round of:
    piDigitRounded = round(pi,n)
    piDigitNotRounded = float(str(pi)[:n+2])

    #printing the output
    return (f'the value of pi upto {n} digits when rounded off is {piDigitRounded} and when not rounded off is {piDigitNotRounded}')

#WE WILL KEEP THE MAXIMUM DIGITS TO BE AT 20 AND MAXIMUM TRY TO BE 3
attempt = 0
while (attempt<3):
    n = int(input('Enter the number of digits after decimal that needs to be printed: '))
    if (n>20):
        print("Maximum number of allowed digits is 20. Please try again")
        attempt += 1
    else:
        print(piDigits(n))
        break

if (attempt == 3): print('You have exceeded maximum limit. Try later.')