import random

def valid(column,row):


    if column <= 2 and column >= 0: #checks if column/row is within 0, 1 and 2, and if there is already an X or O in the spot, if not it will return "False"
        
        if row <= 2 and row >= 0:
            
            if board[row][column]=="X" or board[row][column]=="O":
                
                print("This is invalid, please try again")
                return "False"
                
            else:
                return "True"
            
        else: 
            print("This is invalid, please try again")
            return "False"
    
    else: 
        print("This is invalid, please try again")
        return "False"
    


def print_board():
    for i in range (0,3):
                print("\n")
                for j in range (0,3):
                    print(board[i][j], end="\t") #cycles through each item in the board and prints it out to display the board

    

def advanced_ai_move():


    for i in range (0,3): #if the ai has more than 2 in a row, it will attack
        count=0
        for j in range (0,3):
            if board[i][j]=="O":
                count+=1
                
            else:
                pos=j
        if count==2:

            for x in range (0,3):
                
                if board[i][x]=="-":
                        
                    board[i][pos]="O"
                    return
                
    for i in range (0,3): #if the ai has more than 2 in a column, it will attack
        count=0
        for j in range (0,3):
            if board[j][i]=="O":
                count+=1
                
            else:
                pos=j   
        if count==2:
 
            for x in range (0,3):
                
                if board[x][i]=="-":

                    board[pos][i]="O"
                    return

    count=0                               
    for i in range (0,3): #if the ai has more than 2 in a diagonal, it will attack
        if board[i][i]=="O":
            count+=1
        
        if count==2:

            for x in range (0,3):
                
                if board[x][x]=="-":

                    board[x][x]="O"
                    return
                
    count=0                       
    for i in range (0,3): #if the ai has more than 2 in an inverse diagonal, it will attack
        if board[i][2-i]=="O":
            count+=1
        
        if count==2:
            for x in range (0,3):
                
                if board[x][2-x]=="-":

                    board[x][2-x]="O"
                    return
                


    for i in range (0,3): #if the player has more than 2 in a row, it will block
        count=0
        for j in range (0,3):
            if board[i][j]=="X":
                count+=1
                
            else:
                pos=j
        if count==2:

            for x in range (0,3):
                
                if board[i][x]=="-":
                        
                    board[i][pos]="O"
                    return
                
    for i in range (0,3): #if the player has more than 2 in a column, it will block
        count=0
        for j in range (0,3):
            if board[j][i]=="X":
                count+=1
                
            else:
                pos=j   
        if count==2:
 
            for x in range (0,3):
                
                if board[x][i]=="-":

                    board[pos][i]="O"
                    return

    count=0                               
    for i in range (0,3): #if the player has more than 2 in a diagonal, it will block
        if board[i][i]=="X":
            count+=1
        
        if count==2:

            for x in range (0,3):
                
                if board[x][x]=="-":

                    board[x][x]="O"
                    return
                
    count=0                       
    for i in range (0,3): #if the player has more than 2 in an inverse diagonal, it will block
        if board[i][2-i]=="X":
            count+=1
        
        if count==2:
            for x in range (0,3):
                
                if board[x][2-x]=="-":

                    board[x][2-x]="O"
                    return
                
    valid_check="False"            
                    
    while valid_check=="False": #if it cannot block/attack, it will place in a random spot
        column=random.randint(0,2)
        row=random.randint(0,2)
                    
        valid_check=valid(column,row)
    board[row][column]="O"

                    

def win():
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
    


def board_reset():
    for i in range (0,3):
            for j in range (0,3):
                board[i][j]="-"



def game_ai_basic(): #same as the normal game except there is an ai instead of a player

    game="going"
    count=0


    while game=="going": 
        count+=1

        if count%2==0: #checks if its the players or ai's turn
            
            valid_check="False"
        
            while valid_check=="False": #after the inputs are ran (in this case the basic ai's random move), it will use the "valid" function to check if its a valid move, if not it will set valid_check to False and repeat again
                column=random.randint(0,2)
                row=random.randint(0,2)
                
                valid_check=valid(column,row)
            
            board[row][column]="O"

        else: #if its not the ai's turn, it will let the player have their turn
            print_board()

            valid_check="False"
            
            
            while valid_check=="False": #after the inputs are ran, it will use the "valid" function to check if its a valid move, if not it will set valid_check to False and repeat again
                count2=0

                try:
                    column=int(input("\nwhat column would you like to move in (1,2,3): "))-1
                    row=int(input("what row would you like to move in (1,2,3): " ))-1
                    
                except:
                    print("This is invalid, please try again") #checks if input is an integer, if not it will return "False"
                    count2=1
                    valid_check="False"

                if count2==0:
                    valid_check=valid(column,row)

            board[row][column]="X"

        if count==9: #checks if its a draw
                print("It's a draw!")
                return

        
        game=win()
        if game=="game end": #if the game is won it will check who was last playing when they won and then declare them as the winner, and then run menu again
            print_board()

            if count%2==0:
                print("O wins")
                return
            else:
                print("X wins")
                return
            


def advanced_ai_game():
    game="going"
    count=0


    while game=="going": 
        count+=1

        if count%2==0: #checks if its the players or ai's turn
                       
                advanced_ai_move()

        else: #if its not the ai's turn, it will let the player have their turn
            print_board()

            valid_check="False"
            
            
            while valid_check=="False": #after the inputs are ran, it will use the "valid" function to check if its a valid move, if not it will set valid_check to False and repeat again
                count2=0

                try:
                    column=int(input("\nwhat column would you like to move in (1,2,3): "))-1
                    row=int(input("what row would you like to move in (1,2,3): " ))-1
                    
                except:
                    print("This is invalid, please try again") #checks if input is an integer, if not it will return "False"
                    count2=1
                    valid_check="False"

                if count2==0:
                    valid_check=valid(column,row)

            board[row][column]="X"

        if count==9: #checks if its a draw
                print_board()
                print("It's a draw!")
                return

        
        game=win()
        if game=="game end": #if the game is won it will check who was last playing when they won and then declare them as the winner, and then run menu again
            print_board()

            if count%2==0:
                print("O wins")
                return
            else:
                print("X wins")
                return


    
def game_2P():

    game="going"
    count=0


    while game=="going": 
        count+=1
        print_board()

        valid_check="False"
        
        
        while valid_check=="False": #after the inputs are ran, it will use the "valid" function to check if its a valid move, if not it will set valid_check to False and repeat again
            count2=0

            try:
                column=int(input("\nwhat column would you like to move in (1,2,3): "))-1
                row=int(input("what row would you like to move in (1,2,3): " ))-1
                
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
                print_board()
                print("It's a draw!")
                return

        
        game=win()
        if game=="game end": #if the game is won it will check who was last playing when they won and then declare them as the winner, and then run menu again
            print_board()
            print("\n")
            if count%2==0:
                print("O wins")
                return
            else:
                print("X wins")
                return


#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#
board=[["-","-","-"],["-","-","-"],["-","-","-"]] #defines the board as a global variable
#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//#//# 


def menu(): #options menu for if the user would like to play or not
    end=False
    play=False
    while end==False:

        try:
            option=input("would you like to play? (Y/N): ")
            match option:

                case "Y": #if the user wants to play they select what gamemode they want
                    play=True
                    while play==True:

                        try:
                            option2=input("type '1' for 2 player\ntype '2' for the Basic AI\ntype '3' for the Advanced AI\n: ")
                            match option2:

                                case "1":
                                    play=False
                                    print("Running 2P game")
                                    board_reset()
                                    game_2P()

                                case "2":
                                    play=False
                                    print("Running Basic AI")
                                    board_reset()
                                    game_ai_basic()
                                
                                case "3":
                                    play=False
                                    print("Running Advanced AI")
                                    board_reset()
                                    advanced_ai_game()
                                
                                case "bob":
                                    count3=1
                                    while True:
                                        count3+=1
                                        print("bob",count3)


                                case _:
                                    print("invalid input, try again")
                        except:
                            print("invalid input, try again")


                case "N":
                    print("Okay, ending the menu")
                    end=True
                    pass

                case _:
                    print("invalid input, try again1")

        except:
            print("invalid input, try again2")
            pass

menu()