import random

#ranloc brings back a random int between 0 and 7
def ranloc():
    j = random.randint(1, 8) - 1
    return(j)




#Points white and points black
PW = 0
PB = 0



for j in range(100):



    #There is probably a better way to do this but I dont care
    board = [    ["-","-","-","-","-","-","-","-",], ["-","-","-","-","-","-","-","-",], ["-","-","-","-","-","-","-","-",], ["-","-","-","-","-","-","-","-",],
    ["-","-","-","-","-","-","-","-",], ["-","-","-","-","-","-","-","-",], ["-","-","-","-","-","-","-","-",], ["-","-","-","-","-","-","-","-",]                       ]
    XR = ranloc()
    XB = ranloc()
    XQ = ranloc()
    YR = ranloc()
    YB = ranloc()
    YQ = ranloc()


    #makes sure pieces are not placed on the same location
    while ( (XR == XB) and (YR == YB) ) or ( (XR == XB) and (YR == YB) ) :
        XR = ranloc()
        YR = ranloc()

    while ( (XQ == XB) and (YQ == YB) ) or ( (XQ == XR) and (YQ == YR) ) :
        XQ = ranloc()
        YQ = ranloc()

















    board[XR][YR] = "R"
    board[XB][YB] = "B"
    board[XQ][YQ] = "Q"



    for i in range(0, 8):
            print(board[i][0], board[i][1], board[i][2], board[i][3], board[i][4], board[i][5], board[i][6], board[i][7])
    print("             ")
    #Since the queen can move like a rook and a bishop I only need to check if there is line of sight between that piece an the QUEEN
    # once since then both players will get a point
    # and later I only need to check if the queen hits the rook diagonaly or the bishop straight

    checkx = XB
    checky = YB
    #Checks if bishop has line of sight to queen
    LOSQ = False
    for x in range(8):
            if ( (checkx + x >= 0) and (checkx + x <= 7)and (checky + x >= 0) and (checky + x <= 7) ):
                #checks that coordinates are within the chees board
                if (board[checkx + x][checky + x] == "R"):
                    break
                    #checks if the rook breaks the line of sight
                if (board[checkx + x][checky + x] == "Q"):
                    LOSQ = True
                    #if queen is found LOSQ becomes true



    for x in range(8):
            if ( (checkx - x >= 0) and (checkx - x <= 7)and (checky - x >= 0) and (checky - x <= 7) ):
                if (board[checkx - x][checky - x] == "R"):
                    break
                if (board[checkx - x][checky - x] == "Q"):
                    LOSQ = True

    for x in range(8):
            if ( (checkx + x >= 0) and (checkx + x <= 7)and (checky - x >= 0) and (checky - x <= 7) ):
                if (board[checkx + x][checky - x] == "R"):
                    break
                if (board[checkx + x][checky - x] == "Q"):
                    LOSQ = True

    for x in range(8):
            if ( (checkx - x >= 0) and (checkx - x <= 7)and (checky + x >= 0) and (checky + x <= 7) ):
                if (board[checkx - x][checky + x] == "R"):
                    break
                if (board[checkx - x][checky + x] == "Q"):
                    LOSQ = True


    if (LOSQ == True):
        #print("Bishop success")
        PW += 1
        PB += 1
    # if true then both the queen and the bishop attack eachother





    checkx = XR
    checky = YR
    #Checks if Rook has line of sight to queen
    LOSQ = False
    for x in range(8):
            if ( (checkx + x >= 0) and (checkx + x <= 7)):
                #checks that coordinates are within the chees board
                if (board[checkx + x][checky] == "B"):
                    break
                    #checks if the Bishop breaks the line of sight
                if (board[checkx + x][checky] == "Q"):
                    LOSQ = True
                    #if queen is found LOSQ becomes true



    for x in range(8):
            if ( (checkx - x >= 0) and (checkx - x <= 7)):
                if (board[checkx - x][checky] == "B"):
                    break
                if (board[checkx - x][checky] == "Q"):
                    LOSQ = True

    for x in range(8):
            if ( (checky - x >= 0) and (checky - x <= 7) ):
                if (board[checkx][checky - x] == "B"):
                    break
                if (board[checkx][checky - x] == "Q"):
                    LOSQ = True

    for x in range(8):
            if ( (checky + x >= 0) and (checky + x <= 7) ):
                if (board[checkx][checky + x] == "B"):
                    break
                if (board[checkx][checky + x] == "Q"):
                    LOSQ = True


    if (LOSQ == True):
        #print("Rook success")
        PW += 1
        PB += 1

    #Queen checks



    checkx = XQ
    checky = YQ
    #Checks if QUEEEN has DIAGONAL line of sight to ROOK
    LOSQ = False
    for x in range(8):
            if ( (checkx + x >= 0) and (checkx + x <= 7)and (checky + x >= 0) and (checky + x <= 7) ):
                #checks that coordinates are within the chees board
                if (board[checkx + x][checky + x] == "B"):
                    break
                    #checks if the BISHOP breaks the line of sight
                if (board[checkx + x][checky + x] == "R"):
                    LOSQ = True
                    #if  is found LOSQ becomes true



    for x in range(8):
            if ( (checkx - x >= 0) and (checkx - x <= 7)and (checky - x >= 0) and (checky - x <= 7) ):
                if (board[checkx - x][checky - x] == "B"):
                    break
                if (board[checkx - x][checky - x] == "R"):
                    LOSQ = True

    for x in range(8):
            if ( (checkx + x >= 0) and (checkx + x <= 7)and (checky - x >= 0) and (checky - x <= 7) ):
                if (board[checkx + x][checky - x] == "B"):
                    break
                if (board[checkx + x][checky - x] == "R"):
                    LOSQ = True

    for x in range(8):
            if ( (checkx - x >= 0) and (checkx - x <= 7)and (checky + x >= 0) and (checky + x <= 7) ):
                if (board[checkx - x][checky + x] == "B"):
                    break
                if (board[checkx - x][checky + x] == "R"):
                    LOSQ = True


    if (LOSQ == True):
        #print("QUEN HIRS ROKM success")
        PB += 1






    checkx = XQ
    checky = YQ
    #Checks if q has line of sight to r
    LOSQ = False
    for x in range(8):
            if ( (checkx + x >= 0) and (checkx + x <= 7)):
                #checks that coordinates are within the chees board
                if (board[checkx + x][checky] == "R"):
                    break
                    #checks if the  breaks the line of sight
                if (board[checkx + x][checky] == "B"):
                    LOSQ = True
                    #if queen is found LOSQ becomes true



    for x in range(8):
            if ( (checkx - x >= 0) and (checkx - x <= 7)):
                if (board[checkx - x][checky] == "R"):
                    break
                if (board[checkx - x][checky] == "B"):
                    LOSQ = True

    for x in range(8):
            if ( (checky - x >= 0) and (checky - x <= 7) ):
                if (board[checkx][checky - x] == "R"):
                    break
                if (board[checkx][checky - x] == "B"):
                    LOSQ = True

    for x in range(8):
            if ( (checky + x >= 0) and (checky + x <= 7) ):
                if (board[checkx][checky + x] == "R"):
                    break
                if (board[checkx][checky + x] == "B"):
                    LOSQ = True


    if (LOSQ == True):
        #print("QUEEN HIT BISHAP success")
        PB += 1


#it is imbossible for white to win since whenever
#he gets a point black gets one too

print("Blacks points are :", PB)
print("Whites points are :", PW)
if (PB > PW):
    print("Black wins")
else:
    print("draw")
