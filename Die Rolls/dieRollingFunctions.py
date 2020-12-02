import random

#Roller for die. 6 Sides
def sixSidesRoller():
    randomsixSides = random.randint(1,6)
    return randomsixSides

#Roll multiple times with input. 6 sides
def numberOfTimes():
    rollTimes = int(input("How many times do you want to roll?"))
    for counter in range(1, rollTimes + 1):
        print(sixSidesRoller())

#Roll multiple times with input. Input how many sides
def choiceOfSides():
    howManySides = int(input("How many sides would you like?"))
    newRollTimes = int(input("How many times do you want to roll?"))
    for counter in range(1,newRollTimes + 1):
        print(random.randint(1,howManySides))
        newCounter += 1


def dieNoNumber():
        dieList = []
        sides = int(input("How many sides would you like?"))
        print("Please input what you would like written on one side and tap enter for next side.")
        print("Tap enter another time when done.")
        while True:
            sideString = input("")

            if sideString == "":
                break
            else:
                dieList.append(sideString)
        rollTimes = int(input("How many times would you like to roll?"))
        for counter in range(rollTimes + 1):
            chosenOne = random.randint(1, sides)
            print (chosenOne) 
            print ("You rolled:" + dieList[chosenOne - 1])
        print (dieList)