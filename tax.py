m = int(input("what's your income"))
while m >= 0:
    if 0 <= m <= 2000:
        print(f"your_tax_is:{m*0/100}")
    elif 2000< m <= 4000:
        print(m*0.15)
    elif 4000< m <=7000:
        print(m*0.20)
    elif 7000< m <= 10000:
        print(m*0.25)
    elif 10000< m <= 14000:
        print(m*0.30)
    elif m > 14000:
        print(m*0.35)                    
    else:
        print("invalid")    