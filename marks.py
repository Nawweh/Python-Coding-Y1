def main():
    mark=int(input("Please enter your exam mark: "))

    if mark<0 or mark>100:
        print("invalid mark")
    elif mark>=80:
        print("distinction")
    elif mark>=60:
        print("merit")
    elif mark >= 40:
        print("pass")
    else:
        print("a mark of", mark, "is a fail")
if __name__ == "__main__":
    main()