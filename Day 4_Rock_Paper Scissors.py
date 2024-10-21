import random
Choice=int(input("What do you choose? Type 0 for rock, 1 for papers or 2 for scissor:"))
Computer=int(random.randint(0,2))
print("Computer chose: "+ str(Computer))
if Choice==Computer:
    print("Its a Draw!")
if Choice==0 and Computer==1:
    print("You LOSE!")
if Choice==0 and Computer==2:
    print("You WIN!")
if Choice==1 and Computer==0:
    print("You WIN!")
if Choice==1 and Computer==2:
    print("You LOSE!")
if Choice==2 and Computer==0:
    print("You LOSE!")
if Choice==2 and Computer==1:
    print("You WIN!")