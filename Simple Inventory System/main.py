class Inventory:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def find_item_by_name(name):
    for name in inv:
        if inv.name == name:
            found_items.append(item)
        return found_items
    return None

inv = []

req_active = True

#initial product list
inv.append(Inventory("Pizza", 10.99, 1))
inv.append(Inventory("Cheese", 4.99, 2))
inv.append(Inventory("Yogurt", 2.99, 3))
inv.append(Inventory("Milk", 5.99, 4))

while req_active:
    req = input("(D)isplay product information, (U)pdate quantities, (C)alculate total inventory value, (E)xit: ").lower()
    if req == "d":
        for item in inv:
            print(f"Name: {item.name}, Price: {item.price}, Quantity: {item.quantity}")
    elif req == "u":
        pass
    elif req == "c":
        pass
    elif req == "e":
        print("Good bye.")
        req_active = False
    else:
        print("Sorry, I didn't understand that.") 
        continue