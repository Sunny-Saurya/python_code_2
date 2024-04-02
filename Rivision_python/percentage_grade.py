per = float(input("Enter your percentage: "))
if(per>= 80 and per <=100):
    print("Very Good")
elif(per >60 and per<80):
    print("GOod")
elif(per>40 and per<=60):
    print("Average")
else:
    print("Sorry, you are fail")