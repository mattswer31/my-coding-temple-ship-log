import datetime
import math

# # 1. morning routine
# unread = 100
# def morning_routine():
#     global unread
#     print("good morning")
#     today = datetime.datetime.today().weekday()
#     weathers = ["rainy", "sunny", "rainy", "cloudy", "snowing", "sweltering", "sunny"]
#     events = ["work", "bootcamp", "work", "work", "dayoff", "bootcamp", "park"]

#     if weathers[today] == "rainy":
#         print("It's raining today, take an umbrella.")
#     else:
#         print(f"It is {weathers[today]} today.")
#     print(f"Today you have {events[today]} scheduled.")
#     print(f"You currently have {unread} unread emails in your inbox")
# morning_routine()

# # 2. coffee maker
# def make_coffe(coffee_type = "espresso"):
#     options = ["espresso", "americano", "latte", "cappuccino"]
#     if coffee_type == "cappuccino":
#         print("Now making a cappuccino, my favorite!")
#     elif coffee_type in options:
#         print(f"Now making a/an {coffee_type}")
#     else:
#         print(f"{coffee_type} is not available here, sorry!")
# make_coffe()

# 3. dynamic playlist
# def playlist(song_list):
#     for i in song_list:
#         print(f"Now playing {i}")

# custom = ["pyramids", "laura", "i looked away", "from the start"]
# done = False
# while done != True:
#     song = input("Add a song! Input 'done' when you are satisfied")
#     if song == "done":
#         done = True
#         break
#     custom.append(song)
# playlist(custom)

# 4.  group expense tracker
# def track_expenses(*expenses):
#     total = sum(expenses)
#     print(f"The total expenses are: {total}")
#     highest = max(expenses)
#     highest_person = expenses.index(highest)+1
#     print(f"The higest spender was Person {highest_person} with an expense of ${highest}")
# group_expenses = []
# while True:
#     cost = input("Enter an expense or 'done' to finish.")
#     if cost == 'done':
#         break
#     else:
#         group_expenses.append(float(cost))
# track_expenses(*group_expenses)

# 5. product inventory manager
# inventory = ["mouse", "keyboard", "monitor", "headset"]
# def manage_inventory():
#     global inventory
#     while True:
#         choice = input("Would you like to 'add', 'remove', or 'display' the inventory?")
#         if choice == "display":
#             for i in inventory:
#                 print(i)
#         elif choice == "add":
#             new_item = input("Name of item to add?")
#             inventory.append(new_item)
#         elif choice == "remove":
#             removed_item = input("Name of item to remove?")
#             if removed_item in inventory:
#                 inventory.remove(removed_item)
#             else:
#                 print(f"{removed_item} is not in the inventory")
#         elif choice == "done":
#             break
#         else:
#             print("That is not a valid option")
# manage_inventory()

# # 6. payment splitter

# def split_payment(expenses, friends):
#     total = sum(expenses)
#     share = total/friends
#     return total, share

# expenses = []
# number_of_friends = int(input("how many friends are splitting?"))
# while True:
#     expense = input("How much was this expense?")
#     if expense == "done":
#         break
#     expenses.append(float(expense))
# total, share = split_payment(expenses, number_of_friends)
# print(f"The total cost is {total}")
# print(f"The {number_of_friends} friends each owe {share}")

# # 7. phonebook manager
# phonebook_names = []
# phonebook_numbers = []
# def add_contact(name,number):
#     global phonebook_names
#     global phonebook_numbers
#     phonebook_names.append(name)
#     phonebook_numbers.append(number)
# def display_contacts():
#     global phonebook_names
#     global phonebook_numbers
#     for i in range(len(phonebook_names)):
#         print(f"{phonebook_names[i]}'s number is {phonebook_numbers[i]}.")

# while True:
#     action = input("[A]dd a contact, [D]isplay all contacts, or [Q]uit?")
#     if action == 'A':
#         name = input("Name?")
#         number = input("Number?")
#         add_contact(name,number)
#     elif action == 'D':
#         display_contacts()
#     elif action == 'Q':
#         break
#     else:
#         print("Not a valid option")

# 8. HR Assistant
employees = []
def add_employee(name,age,department):
    global employees
    employee = [name,int(age),department]
    employees.append(employee)
def calculate_average_age():
    global employees
    sum = 0
    for i in range(len(employees)):
        sum += employees[i][1]
    sum /= len(employees)
    return sum
def display_employees():
    global employees
    for i in range(len(employees)):
        print(f"{employees[i][0]} is {employees[i][1]} years old and works in the {employees[i][2]} department.")

while True:
    action = input("[A]dd and employee, [D]isplay them, [C]alculate average age, or [Q]uit?")
    if action == 'A':
        name = input("Name?")
        age = input("Age?")
        department = input("Department?")
        add_employee(name,age,department)
    elif action == 'D':
        display_employees()
    elif action == 'C':
        print(calculate_average_age())
    elif action == 'Q':
        break
    else:
        print("That is not a valid option.")