import random

#Welcome message
print("\n---------- WELCOME TO CONNECT 4 ----------\n")

#Variables:
possible_letters = ["A","B","C","D","E","F","G"]
gameBoard = [["","","","","","",""], ["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
rows = 6
cols = 7

#gameBoard:
def printgameBoard():
  print("\n     A    B    C    D    E    F    G  ", end="")
  for x in range(rows):
    print("\n   +----+----+----+----+----+----+----+")
    print(x, " |", end="")
    for y in range(cols):
     if(gameBoard[x][y] == "🔵"):
      print("",gameBoard[x][y], end=" |")
     elif(gameBoard[x][y] == "🟠"):
      print("", gameBoard[x][y], end=" |")
     else:
      print(" ", gameBoard[x][y], end="  |")
  print("\n   +----+----+----+----+----+----+----+")

def modifyTurn(spacePicked, turn):
    gameBoard[spacePicked[0][spacePicked[1]]] = turn

def checkforwiner(token):
    #//Check the horizontal spaces
    for y in range(rows):
        for x in range(cols-3):
            if (gameBoard[x][y] == token and gameBoard[x+1][y]==token and gameBoard[x+2][y]==token and gameBoard[x+3][y]==token):
                print("\n Game Over!", token, "wins! Thank you for playing :)")
                return True

    #//Check the vertical spaces
    for y in range(rows):
        for x in range(cols-3):
            if (gameBoard[x][y] == token and gameBoard[x][y+1]==token and gameBoard[x][y+2]==token and gameBoard[x][y+3]==token):
                print("\n Game Over!", token, "wins! Thank you for playing :)")
                return True
    
     #//Check upper right to bottom left diagonal spaces
    for y in range(rows-3):
        for x in range(3 ,cols):
            if (gameBoard[x][y] == token and gameBoard[x+1][y-1]==token and gameBoard[x+2][y-2]==token and gameBoard[x+3][y-3]==token):
                print("\n Game Over!", token, "wins! Thank you for playing :)")
                return True

    # Check upper left to bottom right diagonal spaces
    for x in range(rows - 3):
        for y in range(cols - 3):
         if gameBoard[x][y] == chip and gameBoard[x+1][y+1] == chip and gameBoard[x+2][y+2] == chip and gameBoard[x+3][y+3] == chip:
          print("\nGame over", chip, "wins! Thank you for playing :)")
          return True
    

    return False

def coordinatePasser(inputString):
    coordinate = [None] *2
    if(inputString[0]=="A"):
        coordinate[1] = 0

    elif(inputString[0]=="B"):
        coordinate[1] = 1

    elif(inputString[0]=="C"):
        coordinate[1] = 2

    elif(inputString[0]=="D"):
        coordinate[1] = 3

    elif(inputString[0]=="E"):
        coordinate[1] = 4

    elif(inputString[0]=="F"):
        coordinate[1] = 5
    
    elif(inputString[0]=="G"):
        coordinate[1] = 6
    
    else:
        print("Invalid")
    coordinate[0] = int(inputString[1])
    return coordinate

def isSpaceAvailable(intendedCoordinate):
  if(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔴'):
    return False
  elif(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔵'):
    return False
  else:
    return True


