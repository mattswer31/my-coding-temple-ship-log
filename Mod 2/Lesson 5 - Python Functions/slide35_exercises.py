import math

#1. username validator
def username_validator(user):
    length = len(user)
    if length >= 8 and not length > 16:
        return True
    else:
        return False 
    
#2. precise price tagger
def price_tagger(price):
    return round(price,2)

#3. global temp translator
def temp_translator(temp):
    cels = (temp-32)*5/9
    print(f"{temp}F is equivalent to {cels:.0f}C")

#4. goldilocks room selector
def goldilocks(rooms):
    pass

#5. ecommerce cart
def ecommerce_cart(cart):
    items = []
    prices = []
    for i in cart:
        if type(i) == str:
            items.append(i)
        else:
            prices.append(i)
    for i in range(len(items)):
        print(f"The price of {items[i]} is {prices[i]}")

# 6. interactive story chooser

# 7. customized list printer

# 8. dynamic type quiz game

# 9. type inspection challenge
def inspect(list):
    for i in range(len(list)):
        print(f"{list[i]} is a {type(list[i])}")

# 10. math function marathon



sample_cart = ["apples", 2.02, "oranges", 3.03, "bread", 2.57, "steak", 7.52]
inspect(sample_cart)
