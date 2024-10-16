def safe_divide(a,b):
    try:
        product = float(a)/float(b)
        print(f"{a} / {b} = {product}")
    except(ZeroDivisionError):
        print("Cannot divide by 0.")
    except(ValueError):
        print("One of these is not a valid number")

a, b = input("Enter two values.").split()
safe_divide(a,b)