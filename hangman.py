import random

class Hangman:
    def __init__(self):
        self.word = "none"
        self.closedword = []
        self.trysnumber = 7
        self.letterleft = -1
        self.tryedletters = []

    def newgame(self):
        f = open("data.txt", "r")
        objfile = f.readlines()

        summa = 0
        for line in objfile:
            summa += 1

        x = random.randint(0, summa)
        i = 0
        for line in objfile:
            if i == x:
                print(line)
                self.word = line
            i += 1

    def show_word(self):
        length = len(self.word)
        warr=[]
        for i in range(0, length-1):
            warr.append("*")
        self.closedword = warr

    def check_letter(self, arg):
        ar = []
        letter = ""
        ishere = False
        if arg in self.tryedletters:
            print("You've already used this letter, choose another one")
        else:
            self.tryedletters.append(arg)
            for key, i in enumerate(self.word):
                if i == arg:
                    ar.append(key)
                    letter = arg
                    ishere = True
                    tup = (letter, ar)
            if ishere == True:
                self.showletter(tup)
            else:
                print("here is no such letter")
                self.trysnumber = self.trysnumber - 1
                print("You have {tries} tries".format(tries=self.trysnumber))


    def showletter(self, lettersInfo):
        for i in lettersInfo[1]:
            self.closedword[i] = lettersInfo[0]
        count = 0
        for i in self.closedword:
            if i == "*":
                count += 1
        self.letterleft = count

        return self.closedword



def print_menu():
    cons = input("""  
    1. New game
    2. Exit""")


while True:
    print_menu()
    resp = int(input())
    if resp == 1:
        print("Enjoy your game")
        hangman = Hangman()
        hangman.newgame()
        print(hangman.show_word())
        print(hangman.closedword)
        while hangman.trysnumber > 0:
            inpLetter = str(input("Guess a letter"))
            if not inpLetter.isalpha():
                print("That is not a letter, try again")
            elif len(inpLetter) > 1:
                print("Print only one symbol please, try again")
            else:
                print(hangman.check_letter(inpLetter))
                print(hangman.closedword)
                if hangman.letterleft == 0:
                    print("You are won!")
                    break
                if hangman.trysnumber == 0 and hangman.letterleft > 0:
                    print("Sorry! Game is over")
                    print("The word was '{w}'".format(w=hangman.word))
                    break

    elif resp == 2:
        print("Hope see you soon back")
        break

    else:
        print("Thank for using app")
        break



