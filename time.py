while True:
    m = int(input("What time is now :"))
    if m<=5 and m < 11:
        print("Morning")
    elif 12<= m < 6:
        print("Afternoon")
    elif 17<= m < 20:
        print("Evening")
    else:
        print("Night")             