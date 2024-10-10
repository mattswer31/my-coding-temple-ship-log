# 1. Movie Night
mood = input("How's your mood? happy, sad, etc")
weather = input("What's the weather today? sunny or something else?")
if mood == "happy":
    if weather == "sunny":
        print("time for a comedy")
    else:
        print("time for a romance")
elif mood == "sad":
    print("time for a drama")
else: 
    print("time for an adventure")

# 2. outfit suggestions
temp = int(input("Whats the temperature in Celsisus?"))
event = input("Formal or casual?")
if temp <= 15:
    if event == "casual":
        print("hoodie and sweats")
    else:
        print("suit and coat")
else:
    if event == "casual":
        print("tshirt and shorts")
    else:
        print("light cotton suit")

# 3. Student Discout Eligibility
grade = input("A, B, or C?")
sports = input("Sports team? yes/no")
drama = input("Drama club? yes/no")

if grade == "A":
    if sports == "yes":
        print("20% discount")
    else:
        print("10% discount")
elif grade == "B":
    if drama == "yes":
        print("15% discount")
    else:
        print("no discount")
else:
    print("no discount")

# 4. Quick Age Check
age = int(input("Age?"))
print ("you can drive") if age >= 18 else print("out out")

# 5. Nested Food Choice
veg = input("Vegetarian?")
sugar = input("Sugar?") 
if veg == "yes":
    if sugar == "yes":
        print("veg cake")
    else:
        print("fruit salad")
else:
    if sugar == "no":
        print("sugar-free ice cream")
    else:
        print("chocolate brownie")
