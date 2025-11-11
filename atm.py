def atm_withdrawal():
    x = 1000.00
    print("your balance : 1000.00")
    m = float(input("with drawal amount"))
    if m < x:
        print("withdrawl successful:")
    elif m > x:
        print("insufficeint fund:")   
    elif m == x:
        print("balance will be 0")
        print(x-m)
atm_withdrawal()
             
    
    