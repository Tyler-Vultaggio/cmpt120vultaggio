#CMPT 120 Intro to Programming
#Project 2 – Calculator V2.0
#Author: Tyler Vultaggio
#Date: 10/30/2019

from graphics import *

#This creates the grapical window for the program.
win = GraphWin("Calculator", 450, 750)
win.setBackground("white")
win.setCoords

#equation = ""

def createCalculator():
#Every button will be 100px wide and 100px tall.
# 0,0 will be 25,25 for this so that a border is created around the calculator.

    #buttons 0-9
    buttonZero = Rectangle(Point(25,605), Point(120,700))
    buttonZero.draw(win)
    zero = Text(Point(72.5,652.5), "0")
    zero.setSize(32)
    zero.draw(win)
    
    buttonOne = Rectangle(Point(25,505), Point(120,595))
    buttonOne.draw(win)
    one = Text(Point(72.5,552.5), "1")
    one.setSize(32)
    one.draw(win)
    
    buttonTwo = Rectangle(Point(125,505), Point(220,595))
    buttonTwo.draw(win)
    two = Text(Point(172.5,552.5), "2")
    two.setSize(32)
    two.draw(win)
    
    buttonThree = Rectangle(Point(225,505), Point(325,595))
    buttonThree.draw(win)
    three = Text(Point(272.5,552.5), "3")
    three.setSize(32)
    three.draw(win)
    
    buttonFour = Rectangle(Point(25,405), Point(120,495))
    buttonFour.draw(win)
    four = Text(Point(72.5,452.5), "4")
    four.setSize(32)
    four.draw(win)
    
    buttonFive = Rectangle(Point(125,405), Point(220,495))
    buttonFive.draw(win)
    five = Text(Point(172.5,452.5), "5")
    five.setSize(32)
    five.draw(win)
    
    buttonSix = Rectangle(Point(225,405), Point(325,495))
    buttonSix.draw(win)
    six = Text(Point(272.5,452.5), "6")
    six.setSize(32)
    six.draw(win)
    
    buttonSeven = Rectangle(Point(25,305), Point(120,395))
    buttonSeven.draw(win)
    seven = Text(Point(72.5,352.5), "7")
    seven.setSize(32)
    seven.draw(win)
    
    buttonEight = Rectangle(Point(125,305), Point(220,395))
    buttonEight.draw(win)
    eight = Text(Point(172.5,352.5), "8")
    eight.setSize(32)
    eight.draw(win)
    
    buttonNine = Rectangle(Point(225,305), Point(325,395))
    buttonNine.draw(win)
    nine = Text(Point(272.5,352.5), "9")
    nine.setSize(32)
    nine.draw(win)
    

    #Operational buttons
    buttonDecimal = Rectangle(Point(125,605), Point(220,700))
    buttonDecimal.draw(win)
    decimal = Text(Point(172.5,652.5), ".")
    decimal.setSize(32)
    decimal.draw(win)
    
    buttonNegative = Rectangle(Point(225,605), Point(325,700))
    buttonNegative.draw(win)
    negative = Text(Point(272.5,652.5), "+/-")
    negative.setSize(32)
    negative.draw(win)
    
    buttonEquals = Rectangle(Point(330,505), Point(425,700))
    buttonEquals.draw(win)
    equals = Text(Point(377.5,597.5), "=")
    equals.setSize(32)
    equals.draw(win)
    
    buttonAddition = Rectangle(Point(330,305), Point(425,495))
    buttonAddition.draw(win)
    addition = Text(Point(377.5,397.5), "+")
    addition.setSize(32)
    addition.draw(win)
    
    buttonSubtraction = Rectangle(Point(330,205), Point(425,295))
    buttonSubtraction.draw(win)
    subtraction = Text(Point(377.5,247.5), "-")
    subtraction.setSize(32)
    subtraction.draw(win)
    
    buttonClear = Rectangle(Point(25,205), Point(120,295))
    buttonClear.draw(win)
    clear = Text(Point(72.5,252.5), "C")
    clear.setSize(32)
    clear.draw(win)
    
    buttonDivision = Rectangle(Point(125,205), Point(220,295))
    buttonDivision.draw(win)
    division = Text(Point(172.5,252.5), "/")
    division.setSize(32)
    division.draw(win)
    
    buttonMultiplication = Rectangle(Point(225,205), Point(325,295))
    buttonMultiplication.draw(win)
    multiplication = Text(Point(272.5,252.5), "*")
    multiplication.setSize(32)
    multiplication.draw(win)
    
    #Display box
    inputBox = Rectangle(Point(25,25), Point(425,200))
    inputBox.draw(win)
    
def getInput():
    user = win.getMouse()
    return user

def getOutput(click, equation):
    x = click.getX()
    y = click.getY()
    if x > 25 and x < 120 and y > 605 and y < 700:
        print("0")
        return "0"
    
    elif x > 25 and x < 120 and y > 505 and y < 595:
        print("1")
        return "1"
    
    elif x > 125 and x < 220 and y > 505 and y < 595:
        print("2")
        return "2"
    
    elif x > 225 and x < 325 and y > 505 and y < 595:
        print("3")
        return "3"
    
    elif x > 25 and x < 120 and y > 405 and y < 495:
        print("4")
        return "4"
    
    elif x > 125 and x < 220 and y > 405 and y < 495:
        print("5")
        return "5"
    
    elif x > 225 and x < 325 and y > 405 and y < 495:
        print("6")
        return "6"
    
    elif x > 25 and x < 120 and y > 305 and y < 395:
        print("7")
        return "7"
    
    elif x > 125 and x < 220 and y > 305 and y < 395:
        print("8")
        return "8"
    
    elif x > 225 and x < 325 and y > 305 and y < 395:
        print("9")
        return "9"
    elif x > 225 and x < 325 and y > 205 and y < 295:
        print(" * ")
        return " * "
    elif x > 125 and x < 220 and y > 205 and y < 295:
        print(" / ")
        return " / "
    elif x > 330 and x < 425 and y > 205 and y < 295:
        print(" - ")
        return " - "
    elif x > 330 and x < 425 and y > 305 and y < 495:
        print(" + ")
        return " + "
    elif x > 125 and x < 220 and y > 605 and y < 700:
        print(".")
        return "."
    elif x > 225 and x < 325 and y > 605 and y < 700:
        print("+/-")
        return ""
    elif x > 330 and x < 425 and y > 505 and y < 700:
        print("=")
        calculate(equation)
    else:
        return ""

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

def calculate(equation):
    newEquation = equation.split()
    doMulti(newEquation)
    doDivi(newEquation)
    doAdd(newEquation)
    doSub(newEquation)
    print(newEquation)
    
    
    
def main():
    equation = ""
    createCalculator()
    while True:
        user = getInput()
        new = getOutput(user, equation)
        if not(user.getX() > 330 and user.getX() < 425 and user.getY() > 505 and user.getY() < 700):
            equation = equation + new
        if user.getX() > 25 and user.getX() < 120 and user.getY() > 205 and user.getY() < 295:
            print("C")
            equation = ""
        
        print(equation)



main()























