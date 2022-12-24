'''
Example maze:
10
7
1100000000000111111101100000000100011000010101001100010000001111111111
'''
length = int(input("Enter world length: ")) + 2
breadth = int(input("Enter world breadth: ")) + 2
world = []
lengthElem = [" "]*length
print("Enter maze code of "+str((length-2)*(breadth-2))+" characters (1 is block and 0 is empty): ")
mazeCode = input().replace("1","█").replace("0"," ")[:(length*breadth)]
slices = []
currentSlice = []
for k in range(breadth-2):
    for i in range(length-2):
        currentSlice.append(mazeCode[i])
    mazeCode = mazeCode[length-2:]
    slices.append(currentSlice)
    currentSlice = []
world.append(lengthElem[:])
for i in range(breadth-2):
    world.append([" "]+slices[i]+[" "])
world.append(lengthElem[:])
def printWorld():
    for row in world:
        print(''.join(row))
for block in range(length):
    world[0][block]="█"
for block in range(length):
    world[-1][block]="█"
for block in range(1, breadth):
    world[block][0]="█"
    world[block][-1]="█"
playerX, playerY = (length)//2, breadth-2
world[playerY][playerX] = "^"
world[0][playerX] = " "
printWorld()
play = True
while play:
    print("Input Q to quit")
    action = input("W/A/S/D:").upper()
    if action == "W" and world[playerY-1][playerX]==" ":
        world[playerY][playerX]=" "
        playerY-=1
        world[playerY][playerX]="^"
    elif action == "S" and world[playerY+1][playerX]==" ":
        world[playerY][playerX]=" "
        playerY+=1
        world[playerY][playerX]="v"
    elif action == "A" and world[playerY][playerX-1]==" ":
        world[playerY][playerX]=" "
        playerX-=1
        world[playerY][playerX]="<"
    elif action == "D" and world[playerY][playerX+1]==" ":
        world[playerY][playerX]=" "
        playerX+=1
        world[playerY][playerX]=">"
    elif action == "Q":
        quit()
    printWorld()
    if world[0][length//2]=="^":
        print("You win!")
        quit()