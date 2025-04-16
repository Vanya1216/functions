def fact(a):
    if a<=1:
        return 1
    else:
        return a * fact(a-1)

a=int(input("enter a number"))
print("The factorial of a is",fact(a))