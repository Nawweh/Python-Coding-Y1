word=str.lower(input("give a word for player 2 to guess: "))
word_2=str.lower(input("player 2, guess the word: "))

if word==word_2:
    print("correct")
else:
    print("incorrect")