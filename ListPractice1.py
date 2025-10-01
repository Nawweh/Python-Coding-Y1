def main():
    confirm="True"
    my_array=["Tim","Nigel","Steve","Maggie"]
    
    while confirm=="True":
          new_person=input("input another person ")
          my_array.append(new_person)
          confirm=input("do you want to add another (True/False)")

    for i in my_array:
        print(i)
main()
