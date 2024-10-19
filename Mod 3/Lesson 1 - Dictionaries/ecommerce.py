# 3. error handling like adding prod to unlisted category
# 4. search is case-insensitive

# lower() or upper() for case-insensitive
# in serach check for products in every category, leverage try and except for KeyError

def add_category(category):
    catalog[category] = []

def add_product(category, product):
    try:
        catalog.get(category).append(product)
    except AttributeError:
        print(f"{category} category does not exist.")

def display():
    for category, product in catalog.items():
        print("{} ({})".format(category, product))

def search_product(search):
    found = False
    for category, products in catalog.items():
        for product in products:
            if product.lower() == search.lower():
                print(f"{search} is in {category}!")
                found = True
                break
    if found == False:
        print(f"{search} was not found.")

catalog = {"parts" : ["cpu", "gpu"],
           "periphs" : ["mouse", "keyboard"],
           "games" : ["deadlock", "overwatch"]}

add_category("books")
add_product("parts", "fan")
add_product("books", "grapes")
search_product("CPU")
search_product("power cable")
display()
