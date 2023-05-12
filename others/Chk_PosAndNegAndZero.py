# check number positive or not
while True:
    num = float(input("enter a number: "))
    if num == 0:
        print("number is Zero")
    elif num >0:
        print("number is Positive")
    else:
        print("number is Negative")

    con=input("continue loop(y/n): ")
    if con == 'n':
        break

