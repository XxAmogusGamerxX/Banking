from items import items
class Bank():
  def __init__(self, inventory, money):
    self.money = money
    self.inventory = inventory
    self.items = items
    

  def viewMoney(self):
    print(f"You have ${self.money}.")

  def viewItems(self):
    itemName = ""
    itemPrice = ""
    itemCount = ""
    finalPrice = 0
    finalPrint = ""
    finalPrint += "Inventory:"
    for i in range(len(self.inventory)):
      itemName = self.inventory[i][0]
      for i in range(len(self.items)):
        if(self.items[i][0] == itemName):
          itemPrice = int(self.items[i][1])
      itemCount = int(self.inventory[i][1])
      finalPrint += f"\n  - Name: {itemName}\n    - Price Per Item: ${itemPrice}\n    - Amount: {itemCount}\n    - Price: ${itemPrice * itemCount}\n"
      finalPrice = itemPrice * itemCount
    finalPrint += f"\n\n  - Final Value in Items: ${finalPrice}"
    print(finalPrint)

  def buyItem(self,itemName,amount):
    itemPrice = ""
    finalPrice = ""
    for i in range(len(self.items)):
        if(self.items[i][0] == itemName):
          itemPrice = int(self.items[i][1])
    finalPrice = itemPrice * int(amount)
    if(self.money >= finalPrice):
      self.inventory.append([str(itemName),str(amount)])
      self.money -= finalPrice
      print(f"You bought {amount} {itemName}(s) for ${finalPrice}.\n  - You now have ${self.money}")
    else:
      print(f"You are too poor to buy {amount} {itemName}(s)\n  - You only have ${self.money}")

  def sellItem(self,itemName,amount):
    # See if there are {amount} of item(s) that user wants to sell, remove those items, give player money, check if there are any of that item, and if not, remove that item entirely from their inventory
    
    itemIndex = ""
    sellPrice = ""

    # Get item's index in inventory
    for i in range(len(self.inventory)):
      if(self.inventory[i][0] == itemName):
        itemIndex = i

    # Get item price
    for i in range(int(len(self.items))):
      if(self.items[i][0] == itemName):
        sellPrice = self.items[i][2]

    # Sell Item

    if(int(self.inventory[int(itemIndex)][1]) >= int(amount)):
      self.inventory[int(itemIndex)][1] = int(self.inventory[int(itemIndex)][1])
      self.inventory[int(itemIndex)][1] -= int(amount)
      self.money += int(sellPrice) * int(amount)
      print(f"You sold {amount} {itemName}(s) for ${int(sellPrice) * int(amount)}.\n  - You now have ${self.money}")
    else:
      print(f"You don't have enough {itemName}s to sell {amount} {itemName}(s).\n  - You only have {self.inventory[int(itemIndex)][1]} {itemName}(s).")

    