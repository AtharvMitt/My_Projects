import random
target="yes"
import os
while target=="yes":
    os.system("cls")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    Answer=int(random.randint(1,100))
    Choice=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if Choice=="easy":
        Mistakes=10
    elif Choice=="hard":
        Mistakes=5
    Guess=int(input("Make a guess: "))

    while Mistakes>0:
        if int(Guess)==Answer:
            print("You got it! The answer was "+str(Answer))
            break
        elif int(Guess)>Answer:
            print("Too high.")
            Mistakes-=1
            print("You have "+str(Mistakes)+" guesses left")
            Guess=input("Guess again: ")
        else:
            print("Too low.")
            Mistakes-=1
            print("You have "+str(Mistakes)+" guesses left")
            Guess=input("Guess again: ")
    if Mistakes==0:
        print("OOF, you ran out of guessses! The answer was: "+str(Answer))
    target=input("Do you wish to try again?(yes/no): \n")
print("Thank you for playing!")