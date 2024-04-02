num = int(input("Enter any positive number: "))

if( num % 15 == 0):
    print("Number is divisible by 15")
else:
    if(num % 3 == 0 or num % 5 == 0):
        print("divisible by 3 or 5")
    else:
        print("not divisible by 3 or 5")
    