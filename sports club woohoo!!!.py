def sport_club_membership():
    user_age=int(input("give me your age pls :) "))
    member_years=int(input("give me how many years you've been a member "))
    if user_age<18:
        if member_years<2:
            print("you pay £60")
        else:
            print("you pay £40")
    elif user_age>18 and user_age<50:
        if member_years>10:
            print("pay £90")
        else:
            print("print £120")
    elif user_age>50:
        if member_years>10:
            print("pay £50")
        else:
            print("print £80")
sport_club_membership()

