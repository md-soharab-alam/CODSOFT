first = int(input("enter your first number : "))
operator = input("enter your operator(+,_,*,/) : ")
second = int(input("enter your second second number :"))

if operator == "+":
    print("result=",first + second)

elif operator == "-":
    print("Result=",first - second)

elif operator == "*":
    print("Result=",first * second)

elif operator == "//":
    print("Result=",first // second)

elif operator == "%":
    print("Result=",first%second)    

else:
    print("invalide operation")


