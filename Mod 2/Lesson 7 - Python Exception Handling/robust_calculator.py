def add(a,b):
    sum = a + b
    print(f"{a} + {b} = {sum}")

def sub(a,b):
    sum = a - b
    print(f"{a} - {b} = {sum}")

def div(a,b):
    try:
        prod = a/b
        print(f"{a} / {b} = {prod}")
    except ZeroDivisionError:
        print("Cannot divide by 0.")

def mult(a,b):
    prod = a*b
    print(f"{a} * {b} = {prod}")

a, b = input("Gimme two numbers.").split()
try:
    num1 = float(a)
    num2 = float(b)
    action = input("[A]dd, [S]ubtract, [D]ivide, or [M]ultiply?")
    if action == 'A':
        add(num1,num2)
    elif action == 'S':
        sub(num1,num2)
    elif action == 'D':
        div(num1,num2)
    elif action == 'M':
        mult(num1,num2)
    else:
        print("not a valid action.")
except ValueError:
    print("One of the inputs is not a valid number.")

