def valid(column,row):


    if column <= 3 or column < 0: #checks if column/row is within 0, 1 and 2, and if there is already an X or O in the spot, if not it will return "False"
        
        if row <= 3 or row < 0:
            
            if board[row][column]=="X" or board[row][column]=="O":
                
                print("This is invalid, please try again")
                return "False"
                
            else:
                return "True"
    else: 
        print("This is invalid, please try again")
        return "False"
    

    
def win_test():
    if board[0][0] =="X" and board[0][1] =="X" and board[0][2] =="X": #checks if the rows have win condition
        return "game end"
    elif board[0][0] =="O" and board[0][1] =="O" and board[0][2] =="O":
        return "game end"
    if board[1][0] =="X" and board[1][1] =="X" and board[1][2] =="X":
        return "game end"
    elif board[1][0] =="O" and board[1][1] =="O" and board[1][2] =="O":
        return "game end"
    if board[2][0] =="X" and board[2][1] =="X" and board[2][2] =="X":
        return "game end"
    elif board[2][0] =="O" and board[2][1] =="O" and board[2][2] =="O":
        return "game end"
    

    if board[0][0] =="X" and board[1][0] =="X" and board[2][0] =="X": #checks if all the columns have win condition
        return "game end"
    elif board[0][0] =="O" and board[1][0] =="O" and board[2][0] =="O":
        return "game end"
    if board[0][1] =="X" and board[1][1] =="X" and board[2][1] =="X":
        return "game end"
    elif board[0][1] =="O" and board[1][1] =="O" and board[2][1] =="O":
        return "game end"
    if board[0][2] =="X" and board[1][2] =="X" and board[2][2] =="X":
        return "game end"
    elif board[0][2] =="O" and board[1][2] =="O" and board[2][2] =="O":
        return "game end"
    
    
    if board[0][0] =="X" and board[1][1] =="X" and board[2][2] =="X": #checks both diagonals to see if win condition
        return "game end"
    elif board[0][0] =="O" and board[1][1] =="O" and board[2][2] =="O":
        return "game end"
    if board[2][0] =="X" and board[1][1] =="X" and board[0][2] =="X":
        return "game end"
    elif board[2][0] =="O" and board[1][1] =="O" and board[0][2] =="O":
        return "game end"
    
    return "going" #if a win is not found, return going
    

def win(): #old system that works but is unoptimised, here for testing :)
    if board[0][0] =="X" and board[0][1] =="X" and board[0][2] =="X": #checks if the rows have win condition
        print ("X wins")
        return "game end"
    elif board[0][0] =="O" and board[0][1] =="O" and board[0][2] =="O":
        print ("O wins")
        return "game end"
    if board[1][0] =="X" and board[1][1] =="X" and board[1][2] =="X":
        print ("X wins")
        return "game end"
    elif board[1][0] =="O" and board[1][1] =="O" and board[1][2] =="O":
        print ("O wins")
        return "game end"
    if board[2][0] =="X" and board[2][1] =="X" and board[2][2] =="X":
        print ("X wins")
        return "game end"
    elif board[2][0] =="O" and board[2][1] =="O" and board[2][2] =="O":
        print ("O wins")
        return "game end"
    

    if board[0][0] =="X" and board[1][0] =="X" and board[2][0] =="X": #checks if all the columns have win condition
        print ("X wins")
        return "game end"
    elif board[0][0] =="O" and board[1][0] =="O" and board[2][0] =="O":
        print ("O wins")
        return "game end"
    if board[0][1] =="X" and board[1][1] =="X" and board[2][1] =="X":
        print ("X wins")
        return "game end"
    elif board[0][1] =="O" and board[1][1] =="O" and board[2][1] =="O":
        print ("O wins")
        return "game end"
    if board[0][2] =="X" and board[1][2] =="X" and board[2][2] =="X":
        print ("X wins")
        return "game end"
    elif board[0][2] =="O" and board[1][2] =="O" and board[2][2] =="O":
        print ("O wins")
        return "game end"
    
    
    if board[0][0] =="X" and board[1][1] =="X" and board[2][2] =="X": #checks both diagonals to see if win condition
        print ("X wins")
        return "game end"
    elif board[0][0] =="O" and board[1][1] =="O" and board[2][2] =="O":
        print ("O wins")
        return "game end"
    if board[2][0] =="X" and board[1][1] =="X" and board[0][2] =="X":
        print ("X wins")
        return "game end"
    elif board[2][0] =="O" and board[1][1] =="O" and board[0][2] =="O":
        print ("O wins")
        return "game end"
    
    return "going" #if a win is not found, return going
    



def game_start():

    game="going"
    count=0
    valid_check="False"


    while game=="going": 
        count+=1
        for i in range (0,3):
            print("\n")
            for j in range (0,3):
                print(board[i][j], end="\t") #cycles through each item in the board and prints it out to display the board
        valid_check="False"
        
        

        while valid_check=="False": #after the inputs are ran, it will use the "valid" function to check if its a valid move, if not it will set valid_check to False and repeat again
            count2=0
            column=input("\nwhat column would you like to move in (0,1,2): ") 
            row=input("what row would you like to move in (0,1,2): " )

            try:
                column=int(column)
                row=int(row)
            except:
                print("This is invalid, please try again") #checks if input is an integer, if not it will return "False"
                count2=1
                valid_check="False"

            if count2==0:
                valid_check=valid(column,row)


        if count%2==0: #checks whos turn it is and sets that position on the board to their letter
            board[row][column]="O"
        else:
            board[row][column]="X"

        if count==9: #checks if its a draw
                print("It's a draw!")
                menu()
        
        game=win_test()
        if game=="game end": #if the game is won it will check who was last playing when they won and then declare them as the winner, and then run menu again
            for i in range (0,3):
                print("\n")
                for j in range (0,3):
                    print(board[i][j], end="\t")
            print("\n")
            if count%2==0:
                print("O wins")
                menu()
            else:
                print("X wins")
                menu()




board=[["-","-","-"],["-","-","-"],["-","-","-"]] #defines the board as a global variable




def menu(): #options menu for if the user would like to play or not
    end=False
    while end==False:
        option=input("would you like to play? (Y/N): ")
        match option:
            case "Y":
                board=[["-","-","-"],["-","-","-"],["-","-","-"]]
                game_start()
            case "N":
                print("Okay, ending the menu")
                end=True
            case _:
                print("invalid input, try again")
    



menu()