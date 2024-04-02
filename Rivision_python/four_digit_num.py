num = int(input("Enter the number: "))
count = 0
while(num>0):
    rev = num % 10
    num //=10
    count = count + 1
if(count == 4):
    print("Yes, given number is of four digit")
else:
    print("NO, given number is not four digit")
