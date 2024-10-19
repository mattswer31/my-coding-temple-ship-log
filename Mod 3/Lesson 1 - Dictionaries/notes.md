dictionaries
    dict["yoga"] = "7:30 AM"
items()
    returns a view object that displays list of dicts kv tuple pairs
keys()
    returns a view object that displays list of all keys in dict
values()
    returns a view object that displays list of all values in dict
get()
    location_of_toaster = kitchen.get("Toaster", "not found")
    returns value of key, "not found" is default if not key is found
setdefault()
    returns value of specified key, if key not found, inserts key with specified default value
update()
    merges another dict or an iterable of kv pairs
pop(key, [default])
    removes item with specified key and returns its value, if not it returns default, otherwise KeyError
popitem()
    removes and returns last inserted kv pair as tuple
    before py3.7 it removes random item because dicts were unordered
del dict[key]
    rmoves item with key, otherwise raises KeyError
clear()
    empties entire dict, leaving it empty
sorted(dict.keys or values)
    sorts keys or values by alph, or numeric order

keys and values
keys are unique, values dont have to be
kitchen = {"Spoons" : "top drawer",
           "plates" : "middle shelf"}
prints {'Spoons': 'top drawer', 'plates': 'middle shelf'}
location_spoon = kitchen["Spoons"]
prints top drawer

shallow copy
    copied = original.copy()
    outer dict is duplicated but contents still ref the same objects
    copy can be modified without affecting original unless using compound objects (list,class instances)
    dict is a new object
    faster and cheaper to create

deep copy
    copied = copy.deepcopy(original)
    changing copy does not affect original, it is completely new object including parts of lists
    longer and more expesive to create
    

assignment
    seconddict = firstdict
    change seconddict changes firstdict
    seconddict is pointing to firstdict

get and setdefault for safe access and assignment
leverage dict comprehensions for efficiency
iterate with items keys and values
avoid redundant key lookups
be mindful of mem usage with large dicts