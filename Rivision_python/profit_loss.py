cp = float(input("Enter the cost price: "))
sp = float(input("Enter the selling price: "))
profit = sp - cp
loss = cp-sp

if(sp>cp):
    print("Profit of",profit)
else:
    print("Loss of",loss)

