import math


pairs = [(1,5),(2,20),(12,10)]
print(pairs)


cathetus = [math.sqrt((x * x) + (y * y)) for x,y in pairs]
print(cathetus)

combo = [ (x,y,math.sqrt((x * x) + (y * y))) for x,y in pairs]

try:
    print(combo)
except:
    print("There was no ordered pair")

infections = [("CA",3000),("NJ",500),("FL",250)]

