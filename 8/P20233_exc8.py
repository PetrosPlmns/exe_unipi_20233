import random


#point for white and black
PW = 0
PB = 0

PWRO1 = 0
PBRO1 = 0
PWRO2 = 0
PBRO2 = 0
PWRO3 = 0
PBRO3 = 0


for RO in range(3):
    PW = 0
    PB = 0
    for j in range(100):

        #I dont have to change the size of the board as long as I dont place any piece in the extra squares and do not display them, everything should be fine
        board = [    ["-","-","-","-","-","-","-","-",], ["-","-","-","-","-","-","-","-",], ["-","-","-","-","-","-","-","-",], ["-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-",], ["-","-","-","-","-","-","-","-",], ["-","-","-","-","-","-","-","-",], ["-","-","-","-","-","-","-","-",] ]


        if (RO == 0):
            #gives random location to x and y coordinates for pieces
            XR = random.randint(0, 7)
            XB = random.randint(0, 7)
            YR = random.randint(0, 7)
            YB = random.randint(0, 7)
            while ( (XR == XB) and (YR == YB) ) or ( (XR == XB) and (YR == YB) ) :
                XR = random.randint(0, 7)
                YR = random.randint(0, 7)

      #Changes the location where the pieces are placed
        if (RO == 1):
            XR = random.randint(0, 6)
            XB = random.randint(0, 6)
            YR = random.randint(0, 6)
            YB = random.randint(0, 6)
            while ( (XR == XB) and (YR == YB) ) or ( (XR == XB) and (YR == YB) ) :
                XR = random.randint(0, 6)
                YR = random.randint(0, 6)
#Coordinates for 7*8
        if (RO == 2):
            XR = random.randint(0, 7)
            XB = random.randint(0, 7)
            YR = random.randint(0, 6)
            YB = random.randint(0, 6)
            while ( (XR == XB) and (YR == YB) ) or ( (XR == XB) and (YR == YB) ) :
                XR = random.randint(0, 7)
                YR = random.randint(0, 6)









        board[XR][YR] = "R"
        board[XB][YB] = "B"










        if(RO == 0):
            for i in range(0, 8):
                    print(board[i][0], board[i][1], board[i][2], board[i][3], board[i][4], board[i][5], board[i][6], board[i][7])


        if(RO == 1):
            for i in range(0, 7):
                    print(board[i][0], board[i][1], board[i][2], board[i][3], board[i][4], board[i][5], board[i][6])

        if(RO == 2):
            for i in range(0, 8):
                    print(board[i][0], board[i][1], board[i][2], board[i][3], board[i][4], board[i][5], board[i][6],)

















        print("                    ")

        #checks if there is line of sight

        checkx = XB
        checky = YB
        #Checks if bishop has line of sight to rook
        LOS = False
        for x in range(8):
                if ( (checkx + x >= 0) and (checkx + x <= 7)and (checky + x >= 0) and (checky + x <= 7) ):
                    #checks that coordinates are within the chees board
                    if (board[checkx + x][checky + x] == "R"):
                        LOS = True
                        #if Rook is found LOS becomes true



        for x in range(8):
                if ( (checkx - x >= 0) and (checkx - x <= 7)and (checky - x >= 0) and (checky - x <= 7) ):
                    if (board[checkx - x][checky - x] == "R"):
                        LOS = True

        for x in range(8):
                if ( (checkx + x >= 0) and (checkx + x <= 7)and (checky - x >= 0) and (checky - x <= 7) ):
                    if (board[checkx + x][checky - x] == "R"):
                        LOS = True

        for x in range(8):
                if ( (checkx - x >= 0) and (checkx - x <= 7)and (checky + x >= 0) and (checky + x <= 7) ):
                    if (board[checkx - x][checky + x] == "R"):
                        LOS = True


        if (LOS == True):
            #print("Bishop success")
            PB += 1








        checkx = XR
        checky = YR
        #Checks if Rook has line of sight to bishop
        LOS = False
        for x in range(8):
                if ( (checkx + x >= 0) and (checkx + x <= 7)):
                    #checks that coordinates are within the chees board
                    if (board[checkx + x][checky] == "B"):
                        LOS = True
                        #if bishop is found LOS becomes true



        for x in range(8):
                if ( (checkx - x >= 0) and (checkx - x <= 7)):
                    if (board[checkx - x][checky] == "B"):
                        LOS = True

        for x in range(8):
                if ( (checky - x >= 0) and (checky - x <= 7) ):
                    if (board[checkx][checky - x] == "B"):
                        LOS = True

        for x in range(8):
                if ( (checky + x >= 0) and (checky + x <= 7) ):
                    if (board[checkx][checky + x] == "B"):
                        LOS = True


        if (LOS == True):
            #print("Rook success")
            PW += 1

    if (RO == 0):
        PWRO1 = PW
        PBRO1 = PB
    if (RO == 1):
        PWRO2 = PW
        PBRO2 = PB
    if (RO == 2):
        PWRO3 = PW
        PBRO3 = PB




#checks who won
print("for the first round")
print("Blacks points are :", PBRO1)
print("Whites points are :", PWRO1)
if (PBRO1 > PWRO1):
    print("Black wins")
elif (PWRO1 > PBRO1):
    print("White wins")
else:
    print("Draw")


print("for the 7*7 round")
print("Blacks points are :", PBRO2)
print("Whites points are :", PWRO2)
if (PBRO2 > PWRO2):
    print("Black wins")
elif (PWRO2 > PBRO2):
    print("White wins")
else:
    print("Draw")


print("for the 7*8 round")
print("Blacks points are :", PBRO3)
print("Whites points are :", PWRO3)
if (PBRO3 > PWRO3):
    print("Black wins")
elif (PWRO3 > PBRO3):
    print("White wins")
else:
    print("Draw")
