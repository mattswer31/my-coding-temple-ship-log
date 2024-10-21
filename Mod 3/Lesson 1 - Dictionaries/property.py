def add_property(id, location, price):
    if id not in master_list:
        master_list[id] = {"Location" : location, "Price" : price, "Status" : "Unsold", "Inquiries" : []}
        print(f"Property with ID: {id} added to master list.")
    else:
        print(f"Property with ID: {id} already exists.")

def update_property(property):
    if property in master_list:
        if master_list[property]["Status"] == "Unsold":
            master_list[property]["Status"] = "Sold"
        else:
            master_list[property]["Status"] = "Unsold"
    else:
        print(f"Property {property} does not exist.")

def add_inquriy(property, name, inquiry):
    if property in master_list:
        master_list[property]["Inquiries"].append({"Name" : name, "Inquiry" : inquiry})
    else:
        print(f"Property {property} does not exist")

def display_properties():
    for id in master_list:
        current = master_list[id]
        print(f"Property ID: {id}\nLocation: {current["Location"]}\nPrice: {current["Price"]}\nStatus: {current["Status"]}\nInquiries:")
        for inquiry in current["Inquiries"]:
            print(f"    Name:{inquiry["Name"]} {inquiry["Inquiry"]}")


master_list = {"ABC123" :
              {"Location" : "Allendale", "Price" : 750000, "Status" : "Unsold", "Inquiries" :
              [{"Name" : "Matt Song", "Inquiry" : "Asked about price."}]}}

print("\nReal Estate Management System")
print("1. Add Property\n2. Update Property Status\n3. Add Inquiry\n4. Display Properties\n5. Exit")
while True:
    choice = input("Enter choice: ")
    if choice == '1':
        print("Now Adding a property")
        id = input("ID of property?")
        location = input("Location of property?")
        price = (input("Price of property?"))
        try:
            price = int(price)
            add_property(id,location,price)
        except ValueError:
            print(f"{price} is not a valid price integer. Property could not be added")
    elif choice == '2':
        id = input("Which property status would you like to update?")
        update_property(id)
    elif choice == '3':
        property = input("Property to inquire about?")
        name = input("Name of inquirer?")
        inquiry = input("Inquiry?")
        add_inquriy(property, name, inquiry)
    elif choice == '4':
        display_properties()
    elif choice == '5':
        print(f"Thank you for using Real Estate Managment System.")
        break
    else:
        print(f"{choice} is not a valid choice. Try again.")