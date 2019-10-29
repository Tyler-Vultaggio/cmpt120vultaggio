# CMPT 120 Intro to Programming
# Lab #8 – Matrices and Lookup
# Author: Tyler Vultaggio
# Created: 10-29-2019

#reward, punish, threaten, joke
AI = [[3,0,4,0], #Anger
      [5,0,2,1], #Disgust
      [5,0,4,3], #Fear
      [3,4,2,3], #Happiness
      [3,0,2,5], #Sadness
      [3,1,2,3]] #Surprise

# This is my Introduciton funciton.
def intro():
    print("Hello welcome to the AI that has emotions!")
    print("Our AI is angry right now and you are going to chose an action that will effect it's emtion.")

    
# This is where the user chooses their action.
def getInteraction():
    user = input("What action do you want to do? (reward, punish, threaten, joke): ")
    while True:
        if user.lower() == "reward":
           return 0
        elif user.lower() == "punish":
            return 1
        elif user.lower() == "threaten":
            return 2
        elif user.lower() == "joke":
            return 3
        else:
            user = input("What action do you want to do? (reward, punish, threaten, joke): ")    

# This changes the AI's emotion based off of the users action input.
def changeEmotion(user, emotion):
    newEmotion = AI[emotion][user]
    return newEmotion

# This prints out the AI's emotion to the user.
def giveEmotion(emotion):
    emotions = ["I am so mad at you right now!","I can't believe what you just did.","How could you do that.","I have such a big smile on my face!","I'm going to cry.","WOW!"]
    print(emotions[emotion])


# This is the main where all of the other functions are called, to make the program work.
def main():
    intro()
    emotion = 0
    while True:
        action = getInteraction()
        emotion = changeEmotion(action, emotion)
        giveEmotion(emotion)
        leave = input("Would you like to go again Yes or No: ")
        if leave.lower() == "no":
            break
    
    
main()
