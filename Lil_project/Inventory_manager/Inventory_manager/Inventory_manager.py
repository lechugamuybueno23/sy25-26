Inventory = []
def on():
     name = input("\n Enter item name: ")
     num = int(input(f"How many {name}: "))
     Inventory = {}
     Inventory['item'] = name
     Inventory['amount'] = num
     Inventory.append(Inventory)
     print(f"Updated: {name} (total: {num}) \n")
def to():
    choice = input("Which would you like to delete?: ") # not done
    for i in Inventory:
        if choice == i:
            Inventory.remove(choice)
        else:
            return 0

def tre():
    print(" \n --- Current Inventory ---")
    for i in Inventory:
        print(f"- {Inventory}: {Inventory} \n")

print("--- Personal Invenotry Manager ---")

while True:
    print("Options: [1] Add [2] Remove [3] List [4] Exit")
    choice = input("Select an option (1-4): ")
    if choice == "1":
       on()
    elif choice == "2":
        to()
    elif choice == "3":
        tre()
    elif choice == "4":
        break
    else:
        print("please enter a valid input")