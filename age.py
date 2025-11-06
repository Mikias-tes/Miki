while True:
    m = int(input(" how old are you : "))
    if m > 0 and m < 12:
        print("you are child.")
    elif m > 13 and m < 17:
        print("you are teenager.")
    elif m > 18 and m < 64:
        print("you are adult.")
    else :
        print("you are old.")
 