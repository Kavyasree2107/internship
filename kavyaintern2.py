n1=float(input(" first number:"))
n2=float(input(" second number:"))
opr=input("insert a opertion to be performed (+,-,*,/):")
add=(n1)+(n2)
sub=(n1)-(n2)
mul=(n1)*(n2)
div=(n1)/(n2)
if opr == "+":
    print(add)
elif opr == "-":
    print(sub)
elif opr == "*":
    print(mul)
elif opr == "/":
    print(div)
else:
    print("Invalid operation")
