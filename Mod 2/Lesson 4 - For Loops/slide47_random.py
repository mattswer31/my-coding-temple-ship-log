import random

# 1. lucky draw
raffle = [200,140,22,45,203,14,99]
winner = random.choice(raffle)
print(str(winner))

#3. dice roll
dice = [1,2,3,4,5,6]
face = random.choice(dice)
print(str(face))

#4. randomized quiz
questions = ["water?", "gatorade?", "coffee?", "tea?", "beer?"]
new_list = []
while len(questions) > 0:
    q = random.choice(questions)
    new_list.append(q)
    questions.remove(q)
print(new_list)

# 5. password gen
chars = []
for c in (chr(i) for i in range(32, 127)):
    chars.append(c)
password = ""
for i in range(10):
    password += random.choice(chars)
print(password)

# 6. random color gen
colors = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
new_color = "#"
for i in range(6):
    new_color += random.choice(colors)
print(new_color)
