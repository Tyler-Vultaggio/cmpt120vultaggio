#Introduction to Programming
#Author: Tyler Vultaggio
#Date: 9/22/2019


def main():

    userNumber = eval(input("Enter a Number: "))

    num1 = 0
    num2 = 1

    
    if userNumber < 0: 
        print("invalid number input!") 
    elif userNumber == 0: 
        print(num1) 
    elif userNumber == 1: 
        print(num2) 
    else: 
        for i in range(2,userNumber+1): 
            num3 = num1 + num2 
            num1 = num2 
            num2 = num3

        print(num2)

main()
