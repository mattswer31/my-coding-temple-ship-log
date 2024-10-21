class AlreadyExists(Exception):
    pass
class DoesNotExist(Exception):
    pass

def add_category(category):
    try:
        if category in menu:
            raise AlreadyExists
        else:
            menu[category] = []
    except AlreadyExists:
        print(f"{category} already exists.")

def remove_category(category):
    try:
        menu.pop(category)
    except KeyError:
        print(f"{category} does not exist.")

def add_item(category, item):
    try:
        if item in menu[category]:
            raise AlreadyExists
        else:
            menu[category].append(item)
    except AlreadyExists:
        print(f"{item} already exists in {category}.")
    except KeyError:
        print(f"{category} does not exist. {item} could not be added.")


def remove_item(category, item):
    try:
        if item in menu[category]:
            menu[category].remove(item)
        else:
            raise DoesNotExist
    except DoesNotExist:
        print(f"{item} does not exist in {category}.")
    except KeyError:
        print(f"{category} does not exist. {item} could not be removed.")

def take_order(*orders):
    order_list.append([])
    for items in menu.values():
        for item in items:
            for order in orders:
                if order == item:
                    order_list[-1].append(order)
    for order in orders:
        if order not in order_list[-1]:
            print(f"{order} could not be ordered, it is not in the menu.")
    




def display():
    for category, item in menu.items():
        print(f"{category}: {item}")

menu = {
    "apps" : ["wings", "calimari"],
    "entrees" : ["chicken parm", "spaghetti"]
}
order_list = []

take_order("wings", "calimari", "chicken parm", "nachos")
take_order("wings", "calimari", "spaghetti")
print(order_list)


display()