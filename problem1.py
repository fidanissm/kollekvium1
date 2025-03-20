#Ask the user to input an operator (e.g., `+`, `-`, `*`, `/`) and two numbers. Use if-else logic to perform the appropriate operation and print the result (handling division by zero as needed).
a=input("choose +, -, /, *")
b=int(input("Pls write a number"))
c=int(input("pls write another number"))
if a == "+":
    print(b+c)
elif a== "-":
    print(b-c)
elif a=="*":
    print(b*c)
elif a=="/":
    print(b/c)
    
