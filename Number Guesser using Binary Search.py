import random

maxNum = 10000
print("Think of a number from 1 to", maxNum, "and I will guess it B)")
minRange = 1
maxRange = maxNum
guessed = False
tries = 1
while not guessed:
    mean = random.randint(minRange, maxRange)
    print("Attempt", tries, "\nMy guess is", mean)
    print("""Is your number higher, lower or did I get it right?
[1] Higher
[2] Lower
[3] You guessed it!""")
    a = int(input("Enter: "))
    if a == 3:
        guessed = True
    elif a == 1:
        minRange = mean + 1
    elif a == 2:
        maxRange = mean - 1
    tries += 1
print("L bozo, I guessed that your number is", mean, "in only", tries, "tries.")
