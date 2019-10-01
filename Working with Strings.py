#CMPT 120 Intro to Programming
#Lab #5 – Working with Strings and Functions
#Author: Tyler Vultaggio
#Date: 10/1/2019

def userInput():
    # get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    firstLast = [first, last]
    return firstLast

def userName(firstLast):
    uname = firstLast[0] + "." + firstLast[1]
    return uname

def passWord():
    # ask user to create a new password
    passwd = input("Create a new password: ")
    if len(passwd) < 8:
        while len(passwd) < 8:
            print("Fool of a Took! That password is feeble!")
            passwd = input("Create a new password: ")
        print("The force is strong in this one…")
    return passwd


def main():
    firstLast = userInput()
    uname = userName(firstLast)
    password = passWord()
    print(password)
    # TODO modify this to ensure the password has at least 8 characters
    print("Account configured. Your new email address is", uname + "1@marist.edu")
    
main()
