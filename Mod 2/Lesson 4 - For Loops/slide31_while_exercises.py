#1. countdown timer
timer = 10
while timer > 0:
    print(str(timer) + " seconds left")
    timer -= 1

# 2. patient queue
people = 8
while people > 0:
    print(str(people) + " people ahead of you in line")
    people -= 1
if people == 0:
    print("time to order your sandwich")

# 3. battery charger
battery = 12
while battery < 80:
    print("Currently at " + str(battery) + "% battery level.")
    battery += 10
while battery >= 80 and battery < 100:
    print("Currently at " + str(battery) + "% battery level. Slow charging now.")
    battery += 5
if battery > 100:
    battery = 100
print("Fully charged!")

# 4. smart coffee machine
reservoir = 100
espresso = 10
latte = 20
americano = 30
while reservoir > 0:
    order = input("espresso, latte, or americano?")
    if order == "espresso":
        if reservoir >= 10:
            print("heres an espresso!")
            reservoir -= 10
            print("Reservoir is at " + str(reservoir) + "%")
        else:
            print("Reservoir at " + str(reservoir) + "%. It's not enough to make an espresso")
    elif order == "latte":
        if reservoir >= 20:
            print("heres a latte!")
            reservoir -= 20
            print("Reservoir is at " + str(reservoir) + "%")
        else:    
            print("Reservoir is at " + str(reservoir) + "%. It's not enough to make a latte")
    elif order == "americano":
        if reservoir >= 30:
            print("heres an espresso!")
            reservoir -= 30
            print("Reservoir is at " + str(reservoir) + "%")
        else:
            print("Reservoir is at " + str(reservoir) + "%. It's not enough to make an americano")
    else:
        print("We don't make those here sorry, order something else.")
        pass
if reservoir == 0:
    print("were out of water! fill er back up")

# 5. intelligent elevator system
stops = [6,3,4,5,2,3,6,3,5]
floor = 1
while len(stops) > 0:
    next = stops[0]
    for i in stops:
        if next == i:
            stops.remove(i)
            print(stops)
