a=int(input("Enter number: "))
b=int(input("Enter numbdr: "))
print(f"Before Swap a={a},b={b}")
a=a+b
b=a-b
a=a-b
print(f"After Swap a={a},b={b}")