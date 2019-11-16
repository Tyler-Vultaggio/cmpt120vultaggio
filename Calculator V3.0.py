#CMPT 120 Intro to Programming
#Project 3 – Calculator V3.0
#Author: Tyler Vultaggio
#Date: 11/13/2019

from graphics import *

#This creates the grapical window for the program.
win = GraphWin("Calculator", 450, 750)
win.setBackground("white")
win.setCoords

#Display box
inputBox = Rectangle(Point(25,25), Point(425,90))
inputBox.draw(win)
text = Text(Point(225, 57.5), "")
text.draw(win)

def drawButton(button, win):
    x1 = button[0]
    y1 = button[1]
    x2 = button[2]
    y2 = button[3]
    label = button[4]

    rec = Rectangle(Point(x1, y1), Point(x2, y2))

    rec.draw(win)
    text = Text(Point((x2 - x1)/2 + x1,(y2 - y1)/2 + y1), label)
    text.setSize(32)
    text.draw(win)

def isButtonPressed(button, click):
    x1 = button[0]
    y1 = button[1]
    x2 = button[2]
    y2 = button[3]
    return click.getX() >= x1 and click.getX() <= x2 and click.getY() >= y1 and click.getY() <= y2

def drawKeypad(buttons, win):
    for button in buttons:
        drawButton(button, win)


def displayEquation(equation, win):
    #Display box
    text.setText(equation)
    #text.draw(win)
    

def getLabel(buttons, click):
    for button in buttons:
        if isButtonPressed(button, click):
            return button[4]

def buildEquation(equation, label):
        return equation + label


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

def solveEquation(equation):
    newEquation = equation.split()
    doDivi(newEquation)
    doMulti(newEquation)
    doAdd(newEquation)
    doSub(newEquation)
    print(type(newEquation))
    return newEquation

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    str1 = str1.replace("[","")
    str1 = str1.replace("]","")
    return str1
    
    
def main():
    buttons = [[25, 605, 120, 700, "0"], [25, 505, 120, 595, "1"], [125, 505, 220, 595, "2"],
               [225, 505, 325, 595, "3"], [25, 405, 120, 495, "4"], [125, 405, 220, 495, "5"],
               [225, 405, 325, 495, "6"], [25, 305, 120, 395, "7"], [125, 305, 220, 395, "8"],
               [225, 305, 325, 395, "9"], [125, 605, 220, 700, "."], [225, 605, 325, 700, "+/-"],
               [330, 505, 425, 700, "="], [330, 305, 425, 495, " + "], [330, 205, 425, 295, " - "],
               [25, 205, 120, 295, "C"], [125, 205, 220, 295, " / "], [225, 205, 325, 295, " * "],
               [25, 105, 120, 195, "M+"], [125, 105, 220, 195, "M-"], [225, 105, 325, 195, "MR"],
               [330, 105, 425, 195, "MC"], [0, 0, 450, 750, ""]]
    equation = ""
    memory = "0"
    drawKeypad(buttons, win)
    #createCalculator()
    while True:
        click = win.getMouse()
        label = getLabel(buttons, click)
        if label == "C":
            equation = ""
        elif label == "=":
            memory = solveEquation(equation)
            memory = str(memory)
            memory = listToString(memory)
            display = solveEquation(equation)
            equation = str(equation)
        elif label == "M+":
            equation = equation + " + " + memory
            display = equation
        elif label == "M-":
            equation = equation + " - " + memory
            display = equation
        elif label == "MR":
            equation = equation + memory
            display = equation
        elif label == "MC":
            memory == ""
            display = equation
        else:
            equation = buildEquation(equation, label)
            display = equation
            
        displayEquation(display, win)
        print(equation)



main()























