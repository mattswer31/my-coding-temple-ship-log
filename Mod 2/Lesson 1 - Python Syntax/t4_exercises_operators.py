#1. bakers dilemma: one cake needs 250g of flour and i have 2.5kg of flour. how many cakes?
total_flour = 2500
flour_per_cake = 250
number_of_cakes = total_flour // flour_per_cake
print(number_of_cakes)

#2. claiming territories: use operator to claim variable kingdom with value of "Pythonland"
kingdom = "Pythonland"

#3. fashion contest: 2 shirts cost 45 and 80. comparison operator to check if 1 < 2
shirt1 = 45
shirt2 = 80
print(shirt1 <= shirt2)

#4. rainy day: operation to determine if i should take an umbrella if its going to rain/rain heavily
rain = False
rain_heavy = True
print(rain or rain_heavy)

#5. evaluate 3 + 8 * 2 - 3 = 16. exponent > mult/div > add/sub

#6. 10 pastries divided amonst 3 friends
pastries = 10
friends = 3
pastries_per_friend = pastries // friends
leftover_pastries = pastries % friends
print(pastries_per_friend)
print(leftover_pastries)

#7. use assignment to add is wonderful to kingdom
kingdom += " is wonderful!"
print(kingdom)

#8. are knight1 and knight2 equal?
knight1 = 45
knight2 = 80
print(knight1 == knight2)

#9. chef special
eggs = True
flour = False
pancakes = eggs & flour
print(pancakes)

#10. castle problem
castle_height = 100
moat_width = 50
castle_height *= 2
moat_width /= 2
print(castle_height)
print(moat_width)