import dieRollingFunctions as dr

print("You have 3 choices. Would you like to roll 6 sides die, many sided die, or build own die?")
print("1, 2, or 3?")
choice = input("")

if choice == "1":
    dr.sixSidesRoller()
if choice == "2":
    dr.numberOfTimes()
if choice == "3":
    dr.dieNoNumber()
