class Bank():
  def __init__(self, inventory, money):
    self.money = money
    self.inventory = inventory

  def viewMoney(self):
    print(f"You have ${self.money}.")

  def viewItems(self):
    finalPrice = 0
    finalPrint = ""
    finalPrint += "Inventory:"
    for i in range(len(self.inventory)):
      finalPrint += f"\n  - Name: {self.inventory[i][0]}\n    - Price Per Item: ${self.inventory[i][1]}\n    - Amount: {self.inventory[i][2]}\n    - Price: ${int(self.inventory[i][1]) * int(self.inventory[i][2])}\n"
      finalPrice += int(self.inventory[i][1]) * int(self.inventory[i][2])
    finalPrint += f"\n\n  - Final Value in Items: ${finalPrice}"
    print(finalPrint)