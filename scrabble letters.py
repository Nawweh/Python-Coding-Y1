import random


def find_letter_value(entered_letter):
    totPoint = 0
    points = [["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"],
              ["d", "g"],
              ["b", "c", "m", "p"],
              ["f", "h", "v", "w", "y"],
              "k",
              ["j", "x"],
              ["q", "z"]]
   
    for y in range(len(points)):
        for x in points[y]:
            if x == entered_letter:
                match(y+1):
                    case 1:
                        totPoint = 1
                        break
                    case 2:
                        totPoint = 2
                        break
                    case 3:
                        totPoint = 3
                        break
                    case 4:
                        totPoint = 4
                        break
                    case 5:
                        totPoint = 5
                        break
                    case 6:
                        totPoint = 8
                        break
                    case 7:
                        totPoint = 10
                        break
    return totPoint


def find_word_value(word):
    total_value=0

    for letter in (word):
        total_value+=find_letter_value(letter)

    return total_value


def get_random_letters():
    alphabet = ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t","d", "g","b", "c", "m", "p","f", "h", "v", "w", "y","k","j", "x","q", "z"]
    random_letters=[]

    for i in range (7):
        random_letter=alphabet[random.randint(0,26)]
        random_letters.append(random_letter)
    print(random_letters)
    

def game_scrabble():
    count=0

        



def main():
    option=0
    while option!=4:
        option=int(input("Enter 1 to get the value of a scrabble letter \nEnter 2 to get value of a scrabble word \nEnter 3 to play a game \nEnter 4 to quit \n"))

        if option==1:
            letter=input("input a letter: ")
            letter=str.lower(letter)         
            print(find_letter_value(letter))

        elif option==2:

            word=input("give word: ")
            print(find_word_value(word))
        
        elif option==3:
            game_scrabble()

            

get_random_letters()

