import getpass
import random
target="y"
while target=="y":
    print("Welcome to Hangman!!")
    Word=""
    L2=[]
    L1=[]
    Letters=[]
    target="y"
    def Mistake_0():
        print('''      _______
        |/      |
        |      
        |      
        |       
        |      
        |
    jgs_|___''')
    def Mistake_1():
        print('''      _______
        |/      |
        |      (_)
        |      
        |       
        |      
        |
    jgs_|___''')
    def Mistake_2():
        print('''      _______
        |/      |
        |      (_)
        |       |
        |       |
        |      
        |
    jgs_|___''')
    def Mistake_3():
        print('''      _______
        |/      |
        |      (_)
        |      \|
        |       |
        |      
        |
    jgs_|___''')
    def Mistake_4():
        print('''      _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      
        |
    jgs_|___''')
    def Mistake_5():
        print('''      _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      /
        |
    jgs_|___''')
    def Mistake_6():
        print('''      _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      / \\
        |
    jgs_|___''')
    def Hangman():
            if Mistakes==0:
                Mistake_0()
            elif Mistakes==1:
                Mistake_1()
            elif Mistakes==2:
                Mistake_2()
            elif Mistakes==3:
                Mistake_3()
            elif Mistakes==4:
                Mistake_4()
            elif Mistakes==5:
                Mistake_5()
            elif Mistakes==6:
                Mistake_6()
                print("YOU LOST! The word was: "+Word)
    Choice=input("Do you want to enter the word or let computer choose a random word?(y or n): ")
    if Choice=="y":
        Word=getpass.getpass("Enter the word you want to be guessed:\n")
    else:
        Rando=["canary","postgraduate","anadromous","heehaw","subsolar","scenography","clinch", "sortie", "nursemaid","inceptive","consecrate","apterygial"]
        E=random.randint(0,12)
        Word=Rando[E]
    for i in Word.lower():
        L1.append(i)
    Length=len(Word)
    for i in Word:
        L2.append("_")
    def print_string():
        string=""
        for i in L2:
            string+=i
        print(string+"\n")
    Guessed=False
    Mistakes=0
    goog=""
    print_string()
    Mistake_0()
    while Guessed==False:
        guess=input("Which Letter do you want to guess:\n").lower()
        goog=""
        if guess in Letters:
            print("This letter has already been used!")
            print_string()
            Hangman()
            continue
        Letters.append(guess)
        k=0
        found=0
        while k<Length:
            for i in L1:
                if i == guess:
                    L2[k]=i
                    print_string()
                    Hangman()
                    found+=1
                    k+=1
                    print("The letter \""+i+"\" is there in the word!")
                else:
                    k+=1
        if found==0:
            Mistakes+=1
            print_string()
            Hangman()
            print("You letter \""+guess+"\" is not there in the word!")
        for j in Letters:
                    goog+=j
        print("Letters used are: "+goog)
        if L1==L2:
            print("YOU WIN!!")
            Guessed=True
            target=input("Do you wish to play the game again?(y/n): \n")
        if Mistakes==6:
            Guessed=True
            target=input("Do you wish to play the game again?(y/n): \n")
print("THANK YOU FOR PLAYING!!")