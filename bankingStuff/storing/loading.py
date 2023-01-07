from bankingStuff.bankClass import Bank as B
from bankingStuff.storing.saved import data
from bankingStuff.itemManager.startingStats import startingInventory as SI, startingMoney as SM

def instantiateBank():
    if(int(data[2]) >= 1):
        bank = B(data[0],data[1])
    else:
        bank = B(SI,SM)
    return bank