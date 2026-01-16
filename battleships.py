import random
import time



#!  ________.____    ________ __________    _____  .____      ____   _________ __________.___   _____ __________.____     ___________ _________
#! /  _____/|    |   \_____  \\______   \  /  _  \ |    |     \   \ /   /  _  \\______   \   | /  _  \\______   \    |    \_   _____//   _____/
#!/   \  ___|    |    /   |   \|    |  _/ /  /_\  \|    |      \   Y   /  /_\  \|       _/   |/  /_\  \|    |  _/    |     |    __)_ \_____  \ 
#!\    \_\  \    |___/    |    \    |   \/    |    \    |___    \     /    |    \    |   \   /    |    \    |   \    |___  |        \/        \
#! \______  /_______ \_______  /______  /\____|__  /_______ \    \___/\____|__  /____|_  /___\____|__  /______  /_______ \/_______  /_______  /
#!        \/        \/       \/       \/         \/        \/                 \/       \/            \/       \/        \/        \/        \/ 


alphabet=["A","B","C","D","E","F","G","H","I","J"]
board=[]
board_player=[]
board_ai=[]
board_ai_game=[]
hits=0
hits_ai=0
turns=0
win=False
length=[5,4,3,3,2]


#!  ________.____    ________ __________    _____  .____      ____   _________ __________.___   _____ __________.____     ___________ _________
#! /  _____/|    |   \_____  \\______   \  /  _  \ |    |     \   \ /   /  _  \\______   \   | /  _  \\______   \    |    \_   _____//   _____/
#!/   \  ___|    |    /   |   \|    |  _/ /  /_\  \|    |      \   Y   /  /_\  \|       _/   |/  /_\  \|    |  _/    |     |    __)_ \_____  \ 
#!\    \_\  \    |___/    |    \    |   \/    |    \    |___    \     /    |    \    |   \   /    |    \    |   \    |___  |        \/        \
#! \______  /_______ \_______  /______  /\____|__  /_______ \    \___/\____|__  /____|_  /___\____|__  /______  /_______ \/_______  /_______  /
#!        \/        \/       \/       \/         \/        \/                 \/       \/            \/       \/        \/        \/        \/ 



for i in range (10):
    board.append(["-","-","-","-","-","-","-","-","-","-"])
    board_player.append(["-","-","-","-","-","-","-","-","-","-"])
    board_ai.append(["-","-","-","-","-","-","-","-","-","-"])



def board_reset():
    for i in range (0,10):
        for j in range (0,10):
            board[i][j]="-"



def board_player_reset():
    for i in range (0,10):
        for j in range (0,10):
            board_player[i][j]="-"



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



def print_player_board():
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
            print(board_player[i][j], end="   |   ")
        print("")



def print_ai_board():
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
            print(board_ai[i][j], end="   |   ")
        print("")



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

            if int(row) <= 9 and row >= 0:
                
                if board_player[row][column]=="X"or board_player[column][row]=="*":
                    
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



def valid_input_check(column,row):

    if column <= 9 and column > 0: #checks if column/row is within 0, 1 and 2, and if there is already an X or O in the spot, if not it will return "False"

            if row <= 9 and row > 0:
                for i in range (10):

                    if board[column][row-i]!="-":
                    
                        return False
                    
                   
                return True
                
            else: 
 
                return False

    else: 
        return False



def valid_input_check_y(column,row):

    if column <= 9 and column > 0: #checks if column/row is within 0, 1 and 2, and if there is already an X or O in the spot, if not it will return "False"

            if row <= 9 and row > 0:
                for i in range (10):

                    if board[column-i][row]!="-":
                    
                        return False
                    
                    
                return True
                
            else: 
 
                return False

    else: 
        return False
    


def valid_input_check_ai(column,row):

    if column <= 9 and column > 0: #checks if column/row is within 0, 1 and 2, and if there is already an X or O in the spot, if not it will return "False"

            if row <= 9 and row > 0:
                for i in range (10):

                    if board_ai[column][row-i]!="-":
                    
                        return False
                    
                   
                return True
                
            else: 
 
                return False

    else: 
        return False



def valid_input_check_y_ai(column,row):

    if column <= 9 and column > 0: #checks if column/row is within 0, 1 and 2, and if there is already an X or O in the spot, if not it will return "False"

            if row <= 9 and row > 0:
                for i in range (10):

                    if board_ai[column-i][row]!="-":
                    
                        return False
                    
                    
                return True
                
            else: 
 
                return False

    else: 
        return False
    


def has_win():
    if hits==17:
        print("you win yay")
        return True
    else:
        return False
    
def has_win_AI():
    if hits_ai==17:
        print("you lose :(")
        return True
    else:
        return False





def place_ship(ship_length, letter):

    valid=False

    rotation=random.randint(0,1)

    if rotation==0: #runs for horizontal
        while valid==False:

            x=random.randint(0,9)
            y=random.randint(0,9)

            y=y+ship_length
            for i in range (ship_length):

                valid=valid_input_check_ai(x,y) #checks if the space is valid for each spot
            
    
        if valid==True:
            for i in range (ship_length): #if the space is valid it will place it on the board

                board_ai[x][y]=letter
                y-=1


    else: #runs for vertical
        while valid==False:

            x=random.randint(0,9)
            y=random.randint(0,9)

            x=x+ship_length
            for i in range (ship_length):

                valid=valid_input_check_y_ai(x,y) #checks if the space is valid for each spot
    
        if valid==True:
            for i in range (ship_length): #if the space is valid it will place it on the board

                board_ai[x][y]=letter
                x-=1



def player_turn():

    global turns
    global hits
    global win

    

    valid=False
    game_over=False
    hit=False

    while valid==False:

        count=0
        count2=0
    
        try:
            column=int(input("\nwhat column would you like to move in (1-10): "))-1
            row=str.upper(input("what row would you like to move in (A-J): " ))

            for i in alphabet:

                if row==i:
                    row=count

                else:
                    count+=1
                    
        except:
            print("This is invalid, please try again") #checks if input is an integer, if not it will return "False"
            count2=1
        
        if count2==0: #if it can pass through the try except correctly, it will check if the inputs are valid
            valid=valid_check(column,row)

    

    if board_ai[row][column]=="-": #if the users input is a miss 
        board_player[row][column]="*"
        print("miss")

    elif board_ai[row][column]=="A" or board_ai[row][column]=="B" or board_ai[row][column]=="C" or board_ai[row][column]=="D" or board_ai[row][column]=="E":#if it hits it will say "hit" and turn that spot into an x then count "hits up by 1"
        board_player[row][column]="X"
        print("hit")
        hit=True
        hits+=1

    while hit==True:
        valid=False

        while valid==False:

            count=0
            count2=0
        
            try:
                column=int(input("\nwhat column would you like to move in (1-10): "))-1
                row=str.upper(input("what row would you like to move in (A-J): " ))

                for i in alphabet:

                    if row==i:
                        row=count

                    else:
                        count+=1
                        
            except:
                print("This is invalid, please try again") #checks if input is an integer, if not it will return "False"
                count2=1
            
            if count2==0: #if it can pass through the try except correctly, it will check if the inputs are valid
                valid=valid_check(column,row)


        if board_ai[row][column]=="-": #if the users input is a miss 
            board_player[row][column]="*"
            print("miss")

        elif board_ai[row][column]=="A" or board_ai[row][column]=="B" or board_ai[row][column]=="C" or board_ai[row][column]=="D" or board_ai[row][column]=="E":#if it hits it will say "hit" and turn that spot into an x then count "hits up by 1"
            board_player[row][column]="X"
            print("hit")
            hit=True
            hits+=1



def AI_turn():

    global hits_ai

    hit=False
    column=random.randint(0,9)
    row=random.randint(0,9)


    if board[row][column]=="-": #if the users input is a miss 
        board[row][column]="*"

    elif board[row][column]=="A" or board[row][column]=="B" or board[row][column]=="C" or board[row][column]=="D" or board[row][column]=="E":#if it hits it will say "hit" and turn that spot into an x then count "hits up by 1"
        board[row][column]="X"
        hits_ai+=1
        hit=True

    if hit==True:
        for i in range (1,6):
            print_board()
            time.sleep(1)
            search_path=random.randint(0,1)

            if search_path==0:
                if board[row][column-i]=="-": #if the users input is a miss 
                    board[row][column-i]="*"
                    hit=False
                    return

                elif board[row][column-i]=="A" or board[row][column-i]=="B" or board[row][column-i]=="C" or board[row][column-i]=="D" or board[row][column-i]=="E":#if it hits it will say "hit" and turn that spot into an x then count "hits up by 1"
                    board[row][column-i]="X"
                    hits_ai+=1
                    hit=True

            else:
                if board[row-i][column]=="-": #if the users input is a miss 
                    board[row-i][column]="*"
                    hit=False
                    return

                elif board[row-i][column]=="A" or board[row-i][column]=="B" or board[row-i][column]=="C" or board[row-i][column]=="D" or board[row-i][column]=="E":#if it hits it will say "hit" and turn that spot into an x then count "hits up by 1"
                    board[row-i][column]="X"
                    hits_ai+=1
                    hit=True

                
            


def place_ship_player(ship_length, letter):
    valid=False
    valid2=False
    count=0
    print_board()

    while valid2==False:

        rotation=int(input("would you like your ship to be horizontal (1) or vertical (2): "))-1
        if rotation>1 or rotation<0:
            print("this is invalid, please try again")
        else:
            valid2=True


    if rotation==0: #runs for horizontal
        while valid==False:

            try:
                y=int(input("\nwhat column would you like to place in (1-10): "))-2
                x=str.upper(input("what row would you like to place in (A-J): " ))

                for i in alphabet:

                    if x==i:
                        x=count

                    else:
                        count+=1
                    
            except:
                print("This is invalid, please try again") #checks if input is an integer, if not it will return "False"
                
            y=y+ship_length
            for i in range (ship_length):


                valid=valid_input_check(x,y) #checks if the space is valid for each spot
    
        if valid==True:
            for i in range (ship_length): #if the space is valid it will place it on the board

                board[x][y]=letter
                y-=1


    else: #runs for vertical
        while valid==False:
            
            try:
                y=int(input("\nwhat column would you like to place in (1-10): "))-1
                x=str.upper(input("what row would you like to place in (A-J): " ))

                for i in alphabet:

                    if x==i:
                        x=count

                    else:
                        count+=1
                    
            except:
                print("This is invalid, please try again") #checks if input is an integer, if not it will return "False"
                
            x=x+ship_length
            for i in range (ship_length):


                valid=valid_input_check_y(x,y) #checks if the space is valid for each spot
    
        if valid==True:
            for i in range (ship_length): #if the space is valid it will place it on the board

                board[x-1][y]=letter
                x-=1




def game():
    count=0
    win=False 


    place_ship_player(5,"A") #player ships
    # place_ship_player(4,"B")
    # place_ship_player(3,"C")
    # place_ship_player(3,"D")
    # place_ship_player(2,"E")
    print_board()

    place_ship(5,"A") #AI ships
    place_ship(4,"B")
    place_ship(3,"C")
    place_ship(3,"D")
    place_ship(2,"E")


    while win==False:
        if count%2==0:

            AI_turn()

            win_ai=has_win_AI()

            if win_ai==True:
                return

        else:
            print_ai_board()
            time.sleep(2)
            print("Your board\n")
            print_board()
            time.sleep(2)
            print("Guessing board\n")
            print_player_board()

            player_turn()

            win=has_win()

            if win==True:
                return
        
        count+=1



game()
