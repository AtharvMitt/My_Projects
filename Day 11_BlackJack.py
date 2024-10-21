import random
again="y"
while again=="y":
    Cards=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    Player_Cards=[]
    Computer_Cards=[]
    for i in range(0,2):
        Card=Cards[random.randint(0,12)]
        Player_Cards.append(Card)
    for i in range(0,2):
        Card=Cards[random.randint(0,12)]
        Computer_Cards.append(Card)
    def hit():
        Card=Cards[random.randint(0,12)]
        Player_Cards.append(Card)
    def Comp_hit():
        Card=Cards[random.randint(0,12)]
        Computer_Cards.append(Card)
    def Sum_Player():
        Sum_Player=0
        for i in range(0,len(Player_Cards)):
            if Player_Cards[i]=="K" or Player_Cards[i]=="Q" or Player_Cards[i]=="J":
                Sum_Player+=10
            elif Player_Cards[i] in [2,3,4,5,6,7,8,9,10]:
                Sum_Player+=Player_Cards[i]
            else:
                continue
        for i in range(0,len(Player_Cards)):
            if Player_Cards[i]=="A":
                if (Sum_Player+11)<=21:
                    Sum_Player+=11
                else:
                    Sum_Player+=1
        return Sum_Player
    def Sum():
        Sum=0
        for i in range(0,len(Computer_Cards)):
            if Computer_Cards[i]=="K" or Computer_Cards[i]=="Q" or Computer_Cards[i]=="J":
                Sum+=10
            elif Computer_Cards[i] in [2,3,4,5,6,7,8,9,10]:
                Sum+=Computer_Cards[i]
            else:
                continue
        for i in range(0,len(Computer_Cards)):
            if Computer_Cards[i]=="A":
                if Sum+11<=21:
                    Sum+=11
                else:
                    Sum+=1
        return Sum
    print("Your cards are: "+str(Player_Cards)+" and your Score is: "+str(Sum_Player()))
    print("Computers first Card is: "+str(Computer_Cards[0]))
    Cont="yes"
    while Cont=="yes":
        Action=input("Type 'hit' if you want another card, or type 'stand' to pass: \n").lower()
        if Action=="hit":
            hit()
            print("Your new cards are: "+ str(Player_Cards)+" and your new Score is: "+str(Sum_Player()))
            if Sum_Player()>21:
                print("You busted! Computer wins with: "+str(Computer_Cards)+" and Computer's Score was: "+str(Sum()))
                break
        elif Action=="stand":
            goog="yes"
            while goog=="yes":
                if Sum()<=16:
                    Comp_hit()
                else:
                    goog="no"
            if Sum()>21:
                print("YOU WIN! Computer Busted! Its cards were: "+str(Computer_Cards)+" and Computer's Score was: "+ str(Sum()))
                break
            if Sum_Player()>Sum():
                print("YOU WIN! Computer had the following cards: "+ str(Computer_Cards)+ " and Computer's Score was: "+str(Sum()))
                break
            elif Sum_Player()<Sum():
                print("You LOST! Computer had the following cards: "+ str(Computer_Cards)+ " and Computer's Score was: "+str(Sum()))
                break
            else:
                print("Its a draw! The Computer had the following cards: "+ str(Computer_Cards)+" and Computer's Score was: "+str(Sum()))
                break
    again=input("Do you wish to play again?:(y/n) \n")
print("Thank you for playing!")