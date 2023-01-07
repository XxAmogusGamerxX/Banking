from bank import Bank as B
from clearconsole import cls
  

inventoryStarting = [["Box","30","4"],["Cards","15","2"]]
bank = B(inventoryStarting,3000)
cls()
bank.viewItems()