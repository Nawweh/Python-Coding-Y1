import random

class game:
    def Guess2p():
        NumberToGuess=int(input("Player A enter your chosen number "))

        while NumberToGuess<1 or NumberToGuess>10:
            NumberToGuess=int(input("Not a valid choice please choose another "))

        guess=0
        NumberOfGuesses=0

        while guess!= NumberToGuess and NumberOfGuesses<5:
             guess=int(input("Player B have a guess "))
             NumberOfGuesses+=1
        if guess==NumberToGuess:
            print("Player B wins")
        else:
            print("Player A wins")

    

    def Guess1p():
        NumberToGuess=random.randint(1,10)
        guess=0
        NumberOfGuesses=0

        while guess!= NumberToGuess and NumberOfGuesses<5:
                guess=int(input("Have a guess "))
                NumberOfGuesses+=1

        if guess==NumberToGuess:
            print("You win")
        else:
            print(f"You lose, the answer is {NumberToGuess}")

        

option=int(input("1 player guessing game or 2 player guessing game? (type 1 or 2) "))
while option!=1 or option!=2:
    if option==1:
            game.Guess1p()
    elif option==2:
            game.Guess2p()
    
    option=int(input("You have input a correct character, so 2 player guessing game or 1 player guessing game? (type 1 or 2) "))