num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2: "))

op = input("Enter any operator (+,-,*,/,%,//) :")

match op:
    case '+':
        print(num1+num2)
    case '-':
        print(num1-num2)
    case '*':
        print(num1*num2)
    case '/':
        print(num1/num2)
    case '%':
        print(num1%num2)
    case '//':
        print(num1//num2)
    