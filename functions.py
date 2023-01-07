import os

def cls():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def choice(bank):
    choice = input("1: Check Balance, 2: Check Inventory, 3: Buy Item, 4: Sell Item \n")
    cls()
    if(choice == "1"):
        bank.viewMoney()
    elif(choice == "2"):
        bank.viewItems()
    elif(choice == "3"):
        print("Buy Item")
    elif(choice == "4"):
        print("Sell Item")
    else:
        choice(bank)