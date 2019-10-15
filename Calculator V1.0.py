#CMPT 120 Intro to Programming
#Project 1 – Calculator V1.0
#Author: Tyler Vultaggio
#Date: 10/14/2019

#Does the multiplcation of the equation.
def doMulti(equation):
    while "*" in equation:
        i = equation.index("*")
        equation[i-1] = float(equation[i-1]) * float(equation[i+1])
        del equation[i+1]
        del equation[i]



#Calls each function to solve the equation.
def main():
    userInput = str(input("Enter and equation: "))
    equation = userInput.split()
    doMulti(equation)
    print(equation)
    

main()
