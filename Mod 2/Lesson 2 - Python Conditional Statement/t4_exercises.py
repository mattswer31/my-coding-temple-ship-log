#1. traffic lights
light_color = input("Is the traffic light red, yellow, or green?")
if light_color == "red":
    print("Stop the car!")
elif light_color == "yellow":
    print("Slow down!")
elif light_color == "red":
    print("Drive on through!")
else:
    print("If the traffic light is broken, proceed with caution")

#2. movie age restrictions
rating = "R"
age = 15
if rating == "R" and age < 17:
    print("Not old enough to watch, sorry.")
elif rating == "PG-13" and age < 13:
    print("Not old enough to watch, sorry.")
elif rating == "PG" and age < 10:
    print("Not old enough to watch, sorry.")
else:
    print("go ahead and enjoy")

#3. weather suggestion use elif instead
temp = 67
if temp >= 75:
    print("sunglasses and shorts kinda day")
elif temp >= 60 & temp < 75:
    print("perfect day for a light windbreaker")
elif temp >= 45 & temp < 60:
    print("a little chilly, get snug")
else:
    print("its very cold, bundle up")

# #4. grading use elif instead
# grade = input("whats ur number grade")
# if grade >= 90:
#     print("you got an A")
# if grade >= 80 & grade < 90:
#     print("B")
# if grade >= 70 & grade < 80:
#     print("C")
# if grade > 65 & grade < 70:
#     print("D")
# if grade <= 65:
#     print("F")

#7. library book return
overdue = int(input("How many days is your book overdue?"))
if overdue <= 5:
    fine = overdue*1
    print("you owe $" + str(fine))
elif overdue > 5 & overdue <= 10:
    fine = overdue*2
    print("you owe $" + str(fine))
else:
    fine = overdue*5
    print("you owe $" + str(fine))