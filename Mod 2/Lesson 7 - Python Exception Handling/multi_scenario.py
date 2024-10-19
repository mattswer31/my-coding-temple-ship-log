age = input("How old are you?")
while True:
    try:
        age = int(age)
    except ValueError:
        print("That is not a valid age.")
        break
    try:
        if age < 0 or age > 120:
            raise ValueError
        else:
            print(f"you are {age} years old.")
            break
    except ValueError:
        print("You cannot be < 0 years old or > 120 years old.")
        break