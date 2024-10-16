# promp for quantity to order
# validate for positive int
# confirm if valid
# if invalid display error
# try/except to catch non numeric

class NegativeValue(Exception):
    pass

while True:
    try:
        quantity = int(input("How many books do you wanna order?"))
        if quantity < 0:
            raise NegativeValue()
        print(f"You succesfully ordered {quantity} books.")
        break
    except ValueError:
        print("Thats not a valid quantity.")
    except NegativeValue:
        print("You cannot order a negative number of books.")