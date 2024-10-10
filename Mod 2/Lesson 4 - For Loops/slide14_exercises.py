# 1. festival planner
events = ["food", "games", "show", "drinks"]
times =  ["12:00", "2:00", "4:00", "6:00"]
items =  ["chicken", "water guns", "guitars", "mixers"]

for i in range(4):
    print(events[i] + " will be at " + times[i] + " with " + items[i])

# 2. classroom seat aassignment
students = ["alice", "bob", "charlie", "david", "edward"]
seats = ["front left", "front middle", "front right", "middle", "back"]
for i in range(5):
    print(students[i] + " will be sitting in the " + seats[i] + " seat.")
    
# 3. shopping cart calculator
groceries = ["apples", "bread", "peanut butter", "jelly", "bananas"]
costs = [1.00, 3.50, 5.50, 4.50, 1.50]
total = 0
for i in range(5):
    total += costs[i]
print(total)

# 4. multiplication table
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = 12
table = []
for i in range(10):
    table.append(x[i]*y)
print(table)

# 5. inventory management
stock = ["monitors", "desktops", "laptops", "mice", "keyboards"]
quantity = [43, 25, 46, 85, 67]
for i in range(5):
    print("There are " + str(quantity[i]) + " " + stock[i] + " in stock.")

# 6. treasure hunt
treasures = ["doubloons", "goblets", "chalices", "silver coins", "gold rings"]
for i in range(5):
    print(treasures[i])
    if treasures[i] == "chalices":
        print("found the chalices!")
        break

# 7. email cleanup
emails = ["spam", "promotion", "work", "personal", "spam", "promotion", "shopping"]
for i in range(7):
    if emails[i] == "spam" or emails[i] == "promotion":
        pass
    else:
        print(emails[i])