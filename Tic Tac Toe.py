c1=c2=c3=c4=c5=c6=c7=c8=c9=' '
tiles, player, start=[c1,c2,c3,c4,c5,c6,c7,c8,c9], True, ["O","X"]
while True:
    print("Tic Tac Toe\n1, 2, 3\n4, 5, 6\n7, 8, 9\nRefer to the numbers to play a move\n"+"|".join(tiles[0:3])+"\n"+"-"*6+"\n"+"|".join(tiles[3:6])+"\n"+"-"*6+"\n"+"|".join(tiles[6:])+"\n"+"You are X") if player else print("Tic Tac Toe\n1, 2, 3\n4, 5, 6\n7, 8, 9\nRefer to the numbers to play a move\n"+"|".join(tiles[0:3])+"\n"+"-"*6+"\n"+"|".join(tiles[3:6])+"\n"+"-"*6+"\n"+"|".join(tiles[6:])+"\n"+"You are O")
    tile, player = input("Enter tile to place in: "), not player
    tiles[int(tile)-1]=start[int(not player)]
    if (tiles[0]==tiles[1]==tiles[2] and tiles[0]!=" ")or(tiles[3]==tiles[4]==tiles[5] and tiles[3]!=" ")or(tiles[6]==tiles[7]==tiles[8] and tiles[6]!=" ")or(tiles[0]==tiles[4]==tiles[8] and tiles[0]!=" ")or(tiles[2]==tiles[4]==tiles[6] and tiles[2]!=" ")or(tiles[0]==tiles[3]==tiles[6] and tiles[0]!=" ")or(tiles[1]==tiles[4]==tiles[7] and tiles[1]!=" ")or(tiles[2]==tiles[5]==tiles[8] and tiles[2]!=" "):
        print(start[int(not player)], "wins!\n"+"|".join(tiles[0:3]) + "\n" + "-" * 6 + "\n" + "|".join(tiles[3:6]) + "\n" + "-" * 6 + "\n" + "|".join(tiles[6:]) + "\n")
        break


