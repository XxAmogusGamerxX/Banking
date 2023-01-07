from bankingStuff.functions import cls; from bankingStuff.storing.saving import save; from bankingStuff.storing.loading import instantiateBank as instB

# Instantiate bank, the starting inventory (can be changed in itemManager\items.py) and starting money (can also be changed in itemManager/items.py)
bank = instB()

cls()
bank.viewItems()
input("Press Enter to Continue\n")
cls()
bank.buyItem("Cards","2")
input("Press Enter to Continue\n")
cls()
bank.viewItems()
input("Press Enter to Continue\n")
cls()

# Save the bank
save(bank)