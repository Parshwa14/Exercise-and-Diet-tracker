print("\t\t\tWelcome to Exercise and Diet Tracker")             
import datetime                  # importing the datetime module for printing date and time

def getdate():
    return datetime.datetime.now()          # a function to get the date and time at that moment


def take(s):           # here s is for person and take is to enter the information

    if s == 1:
        t = int(input("Enter 1 for Exercise and 2 for Diet"))
        if t == 1:                 # here t is for choosing diet or exercise
            exs = input("Type here: \n")
            with open("exarnold.txt", "a") as op:                          # here we are using "with" statement to open file 
                op.write(str([str(getdate())]) + ": " + exs + "\n")       # because of better sytnex and also it automatically closes the file
                print("SUCCESSFULLY WRITTEN")

        elif t == 2:
            exs = input("Type here: \n")
            with open("diarnold.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + exs + "\n")
                print("SUCCESSFULLY WRITTEN")

    elif s == 2:

        t = int(input("Enter 1 for Exercise and 2 for Diet"))
        if t == 1:
            exs = input("Type here: \n")
            with open("exphill.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + exs + "\n")
                print("SUCCESSFULLY WRITTEN")

        elif t == 2:
            exs = input("Type here: \n")
            with open("diphill.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + exs + "\n")
                print("SUCCESSFULLY WRITTEN")

    elif s == 3:

        t = int(input("Enter 1 for Exercise and 2 for Diet"))
        if t == 1:
            exs = input("Type here: \n")
            with open("exronnie.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + exs + "\n")
                print("SUCCESSFULLY WRITTEN")

        elif t == 2:
            exs = input("Type here: \n")
            with open("dironnie.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + exs + "\n")
                print("SUCCESSFULLY WRITTEN")


def retrieve(s):  # now here is a function for retrieving the data we have logged in

    if s == 1:
        t = int(input("Enter 1 for Exercise and 2 for Diet"))
        if t == 1:
            with open("exarnold.txt") as op:
                for i in op:
                    print(i, end="")
        elif t == 2:
            with open("diarnold.txt") as op:
                for i in op:
                    print(i, end="")
    elif s == 2:
        t = int(input("Enter 1 for Exercise and 2 for Diet"))
        if t == 1:
            with open("exphill.txt") as op:
                for i in op:
                    print(i, end="")
        elif t == 2:
            with open("diphill.txt") as op:
                for i in op:
                    print(i, end="")

    elif s == 3:
        t = int(input("Enter 1 for Exercise and 2 for Diet"))
        if t == 1:
            with open("exronnie.txt") as op:
                for i in op:
                    print(i, end="")
        elif t == 2:
            with open("dironnie.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please Enter Valid Input (arnold,phill,ronnie)")


a = int(input("Press 1 to Log and 2 to Retrieve"))
 # here a is for choosing to log or to retrieve 

if a == 1:  
    b = int(input("Press 1 for arnold 2 for phill 3 for ronnie"))
    take(b)
else:
    b = int(input("Press 1 for arnold 2 for phill 3 for ronnie"))
    retrieve(b)
