inventory = {"mouse" : 23, "keyboard" : 33, "gpus" : 8}

def update_quantity(product, quantity):
    try:
        inventory.update({product : quantity})
    except KeyError:
        print(f"{product} is not in the inventory.")

def remove_product(product):
    try:
        inventory.pop(product)
    except KeyError:
        print(f"{product} is not in the inventory.")

def display_inventory():
    print(inventory)

update_quantity("mouse", 25)
remove_product("keyboard")
display_inventory()