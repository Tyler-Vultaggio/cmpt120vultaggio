#CMPT 120 Intro to Programming
#Lab #5 – Conditional Execution and Strings
#Author: Tyler Vultaggio
#Date: 10/14/2019

def main():

    Answer = "dog"

    while True:
        print("I am thinking of an animal: ")
        userGuess = input("Take a guess: ")
        if userGuess.lower() == Answer:
            print("Congrats you guessed the word!")
            break
        elif userGuess.lower() == "quit":
            print("You quit the game.")
            break
        else:
            print("Wrong! Try again!")

main()
