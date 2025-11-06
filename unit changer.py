e = input("what do you prefer meter to kilometer or kilometer to meter : ")
def z(r):
    if e == "meter to kilometer":
        print(r/1000)

    elif e == "kilometer to meter":
        print(r*1000)
    else:
        print("envalid")
z(int(input("enter your number")))

  
    
   