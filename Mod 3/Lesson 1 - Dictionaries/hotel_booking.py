hotel_rooms = {201: True,
               202: False,
               203: True,
               204: False}

def add_room(room):
    room = int(room)
    if room in hotel_rooms:
        print(f"{room} is already in the system.")
    else:
        hotel_rooms[room] = False

def check_vacancy(room):
    room = int(room)
    try:
        if hotel_rooms[room] == True:
            print(f"{room} is booked.")
        else:
            print(f"{room} is vacant.")
    except KeyError:
        return (f"{room} not found")

def book_room(room):
    room = int(room)
    try:
        hotel_rooms[room] = not hotel_rooms[room]
    except KeyError:
        print(f"{room} cannot be booked, it's not in the system.")

def display_rooms():
    for room, vacancy in hotel_rooms.items():
        if vacancy == True:
            print(f"{room} is booked.")
        else:
            print(f"{room} is vacant.")

print("Welcome to Delfino Hotel!")
while True:
    action = input("[A]dd a room, [C]heck vacancy, [B]ook a room, [D]isplay rooms, or [Q]uit?")
    if action.upper() == 'A':
        new_room = input("Number of room?")
        add_room(new_room)
    elif action.upper() == 'C':
        room = input("Check vacancy of which room?")
        check_vacancy(room)
    elif action.upper() == 'B':
        room = input("Book which room?")
        book_room(room)
    elif action.upper() == 'D':
        display_rooms()
    elif action.upper() == 'Q':
        print("Thanks for using this booking system!")
        break
    else:
        print(f"{action} is not a valid option.")