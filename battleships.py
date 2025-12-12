alphabet=["A","B","C","D","E","F","G","H","I","J"]

board=[]
for i in range (10):
    board.append(["-","-","-","-","-","-","-","-","-","-"])


def board_reset():
    for i in range (0,7):
        for j in range (0,7):
            board[i][j]="-"



def print_board():
    for x in range (0,10): #prints the numbers at the top

        if x==9:
            print("    ", x+1, end=" ")
        else:  
            print("     ", x+1, end=" ")

    print()
    for i in range (0,10):
        print("  ---------------------------------------------------------------------------------")
        for j in range (0,10):
            if j==0:
                print(alphabet[i], end=" |   ") #adds the vertical lines inbetween each time a new line happens
            print(board[i][j], end="   |   ")
        print("")

level=3

def game_setup(level): #prebuilt boards for testing 
    if level==1:
        for i in range (2,6):
            board[i][1]="B"
        for i in range (3,8):
            board[3][i]="A"
        for i in range (7,10):
            board[6][i]="C"
        for i in range (7,10):
            board[i][5]="D"
    elif level==2:
        for i in range (2,6):
            board[8][i]="B"
        for i in range (5,10):
            board[i][0]="A"
        for i in range (1,4):
            board[i][9]="C"
        for i in range (3,6):
            board[7][i]="D"
    elif level==3:
        for i in range (4,8):
            board[i][3]="B"
        for i in range (2,7):
            board[i][8]="A"
        for i in range (3,6):
            board[i][4]="C"
        for i in range (5,8):
            board[4][i]="D"
        
    print_board()



def valid_check(column,row):

    if column <= 9 and column >= 0: #checks if column/row is within 0, 1 and 2, and if there is already an X or O in the spot, if not it will return "False"

            if row <= 9 and row >= 0:
                
                if board[row][column]=="*":
                    
                    print("you have already hit here, please try again")
                    return False
                    
                else:
                    return True
                
            else: 
                print("This is invalid, please try again")
                return False

    else: 
        print("This is invalid, please try again")
        return False



def player_turn():
    valid=False
    while valid==False:
        count=0
        count2=0
    
        try:
            column=int(input("\nwhat column would you like to move in (1-10): "))-1
            row=input("what row would you like to move in (A-J): " )

            for i in alphabet:
                if row==i:
                    row=count
                    print(row)
                else:
                    count+=1
                    
        except:
            print("This is invalid, please try again") #checks if input is an integer, if not it will return "False"
            count2=1
        
        if count2==0: #if it can pass through the try except correctly, it will check if the inputs are valid
            valid=valid_check(column,row)

    print("DGFDGFJNGGDFJN")

player_turn()
