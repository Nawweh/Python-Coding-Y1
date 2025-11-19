def valid(column,row):

    if column==int(column) and column <= 3 or column > 0:
        
        if row==int(row) and row <= 3 or row > 0:
            
            if board[row][column]=="X" or board[row][column]=="O":
                
                print("This is invalid, please try again")
                valid="False"
                return valid
                
            else:
                valid="True"
                return valid
    else: 
        print("This is invalid, please try again")
        valid="False"
        return valid

def win():
    count=0
    count2=0
    for i in range (0,3):
        for j in range (0,3):
            if board[i][j]=="X":
                count+=1
                if count==3:
                    game="won"
                    print(game)
                    return game
            else: 
                count=0

            if board[j][i]=="X":
                count2+=1
                if count2==3:
                    game="won"
                    print(game)
                    return game
            else:
                count2=0

    game="going"
    print(game)
    return game



game="going"
count=0
board=[["-","-","-"],["-","-","-"],["-","-","-"]]
valid_check="False"


while game=="going":
    count+=1
    for i in range (0,3):
        print("\n")
        for j in range (0,3):
            print(board[i][j], end="\t")
    valid_check="False"
    
    

    while valid_check=="False":
        column=int(input("\nwhat column would you like to move in: "))
        row=int(input("what row would you like to move in: " ))

        valid_check=valid(column,row)

    if count%2==0:
        board[row][column]="O"
    else:
        board[row][column]="X"
    
    game=win()

print("hi")



            