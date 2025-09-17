import math
def textbook_discounts():
    text_books=int(input("how many textbooks bro "))
    loyalty_scheme=input("are you in the loyalty scheme (input Y/N)")
    if text_books>9 and text_books<20:
        if loyalty_scheme=="Y":
            text_books=(text_books*15) /1.05
        else:
            text_books=(text_books*15) /1.05 +5
    elif text_books>20:
        if loyalty_scheme=="Y":
            text_books=(text_books*15) /1.1
        else:
            text_books=(text_books*15) /1.1 +5  
    print(f"the total cost is {round(text_books, 2)}")      
textbook_discounts()