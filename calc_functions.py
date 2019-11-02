#CMPT 120 Intro to Programming
#clac_functions.py
#Author: Tyler Vultaggio
#Date: 11/1/2019

#Does the multiplcation of the equation.
def doMulti(equation):
    while "*" in equation:
        i = equation.index("*")
        equation[i-1] = float(equation[i-1]) * float(equation[i+1])
        del equation[i+1]
        del equation[i]
        
#Does the divsion of the equation.
def doDivi(equation):
    while "/" in equation:
        i = equation.index("/")
        equation[i-1] = float(equation[i-1]) / float(equation[i+1])
        del equation[i+1]
        del equation[i]
        
#Does the addtion of the equation.  
def doAdd(equation):
    while "+" in equation:
        i = equation.index("+")
        equation[i-1] = float(equation[i-1]) + float(equation[i+1])
        del equation[i+1]
        del equation[i]
        
#Does the subtration of the equation.
def doSub(equation):
    while "-" in equation:
        i = equation.index("-")
        equation[i-1] = float(equation[i-1]) - float(equation[i+1])
        del equation[i+1]
        del equation[i]
