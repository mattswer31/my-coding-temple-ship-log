def safe_addition():
    try:
        num1 = float(input("First number?"))
        num2 = float(input("Second number?"))
        sum = num1 + num2
        print(f"{num1} + {num2} = {sum}")
    except ValueError:
        print("That is not a valid number.")

while True:
    action = input("[A]dd two numbers or [Q]uit?")
    if action == 'A':
        safe_addition()
    elif action == 'Q':
        break
    else:
        print("Not a valid option.")