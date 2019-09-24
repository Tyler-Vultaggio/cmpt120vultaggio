#Introduction to Programming
#Author: Tyler Vultaggio
#Date: 9/22/2019

import math

def main():

    n = eval(input("Enter a number: "))

    count = 0
    number = 0

    for i in range(1,n*2+1,2):
        count = count+1
        if count%2==0:
            number = number - (4/i)
        else:
            number = number + (4/i)
        
    print(number)
    diff = math.pi - number
    print("The difference from the approximation and the actual vaule of pi is: ", diff)

main()
