#inputs
#   What type of die
#   How many sides
#       if die with no number is chosen, input what values should be on each side
#   How many time of rolls
#  calculations

import random

def six_side():
    randomsixSides = random.randint(1,6)
    print(randomsixSides)
    return randomsixSides

def integer_side(number_of_sides = 6):
    randomsixSides = random.randint(1,number_of_sides)
    print(randomsixSides)
    return randomsixSides

def choice_of_sides():
    for counter in range(1,roll_times + 1):
        print(random.randint(1,number_of_sides))


def side_input():
    dieList = []
    while True:
            sideString = input("")

            if sideString == "":
                break
            else:
                dieList.append(sideString)
    for counter in range(roll_times + 1):
            chosenOne = random.randint(1, number_of_sides)
            print (dieList[chosenOne - 1]) 

def computer_game():
    computer_rolls = []
    user_rolls = []
    for counter in range(1,game_roll_times + 1):
        computer_rolls.append(six_side())
        user_rolls.append(six_side())
    print('Computer rolled: ', computer_rolls)
    print('Sum = ', sum(computer_rolls))

    print('You rolled: ', user_rolls)
    print('Sum = ', sum(user_rolls))

    if sum(computer_rolls) > sum(user_rolls):
        print('Computer won')
    if sum(computer_rolls) < sum(user_rolls):
        print('You won')
    if sum(computer_rolls) == sum(user_rolls):
        print('It was a tie.')
    



print("Would you like to roll 6 sided die, choose how many sides, make your own, or play against computer?")
choice = input("1, 2, 3, or 4?")

if choice == "1":
    six_side()
if choice == "2" or choice == "3":
    print('This runs')
    number_of_sides = int(input("How many sides would you like?"))
    roll_times = int(input("How many times do you want to roll?"))
    if choice == "2":
        choice_of_sides()
    if choice == "3":
        print("Please input what you would like written on one side and tap enter for next side.")
        print("Tap enter another time when done.")
        side_input()
if choice == "4":
    game_roll_times = int(input("How many times would you like to play against computer?"))
    computer_game()



            

