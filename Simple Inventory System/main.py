class Inventory:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_qty(self, quantity):
        self.quantity = quantity

def find_item_by_name(name):
    for item in inv:
        if item.name == name:
            return item
    return None

inv = []

req_active = True

#initial product list
inv.append(Inventory("Pizza", 10.99, 1))
inv.append(Inventory("Cheese", 4.99, 2))
inv.append(Inventory("Yogurt", 2.99, 3))
inv.append(Inventory("Milk", 5.99, 4))

while req_active:
    req = input("(A)dd product, (D)isplay product information, (U)pdate quantities, (T)otal inventory value, (E)xit: ").lower()
    if req == "a":
        print("**ADD PRODUCT**")
        while True:
            try:
                name = str(input("Name: "))
            except name == "":
                print("Sorry, I didn't understand that.")
                continue
            else:
                break
        while True:
            try:
                price = float(input("Price: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                break
        while True:
            try:
                quantity = int(input("Quantity: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                break
        inv.append(Inventory(name, price, quantity))
    elif req == "d":
        print("**DISPLAY PRODUCT INFORMATION**")
        for item in inv:
            print(f"Name: {item.name}, Price: $ {item.price}, Quantity: {item.quantity}")
    elif req == "u":
        print("**UPDATE QUANTITY**")
        item_name = str(input ("Item Name: "))
        item = find_item_by_name(item_name)
        if item:
            while True:
                try:
                    item_quantity = int(input ("Item Quantity:" ))
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    continue
                else:
                    break
            item.update_qty(item_quantity)
        else:
            print(f"Item with name '{item_name}' not found.")
    elif req == "t":
        print("**TOTAL INVENTORY VALUE**")
        inv_value = round(sum(item.price * item.quantity for item in inv),2)
        print("Total Inventory Value: $", inv_value)
    elif req == "e":
        print("**EXIT**")
        req_active = False
    else:
        print("Sorry, I didn't understand that.") 
        continue