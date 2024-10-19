fruits = ["apple", "strawberry", "banana", "mango"]
while True:
    try:
        fav = input("What is your favorite fruit?")
        if fav not in fruits:
            raise ValueError
        else:
            print(f"{fav} is a valid choice. good job")
            break
    except ValueError:
        print("Pick a different favorite buddy")