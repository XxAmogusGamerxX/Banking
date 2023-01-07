from itemManager.items import items
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

    # Loop through inventory to get the current item name
    for i in range(len(self.inventory)):
      itemName = self.inventory[i][0]
      # Loop through all items 
      for i2 in range(len(self.items)):
        if(self.items[i2][0] == itemName):
          # If the item that is currently looped has the same name as the current one in the inventory, set the item price to the 
          itemPrice = int(self.items[i2][1])
      itemCount = int(self.inventory[i][1])
      finalPrint += f"\n  - Name: {itemName}\n    - Price Per Item: ${itemPrice}\n    - Amount: {itemCount}\n    - Value: ${itemPrice * itemCount}\n"
      finalPrice = itemPrice * itemCount
    finalPrint += f"\n\n  - Total Value in Items: ${finalPrice}"
    print(finalPrint)

  def buyItem(self,itemName,amount):
    itemPrice = ""
    finalPrice = ""
    found = False
    for i in range(len(self.items)):
        if(self.items[i][0] == itemName):
          itemPrice = int(self.items[i][1])
    finalPrice = itemPrice * int(amount)
    if(self.money >= finalPrice):
      # Check if there is already 1+ of the item in inventory
      for i3 in range(len(self.inventory)):
        if(self.inventory[i3][0] == itemName):
          found = True
          self.inventory[i3][1] = int(self.inventory[i3][1])
          self.inventory[i3][1] += 1
      if(found == False): 
        self.inventory.append([str(itemName),int(amount)])
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
      for i in range(len(self.inventory)):
        if(self.inventory[i][1] == 0 or "0"):
          del self.inventory[i]

      print(f"You sold {amount} {itemName}(s) for ${int(sellPrice) * int(amount)}.\n  - You now have ${self.money}")
    else:
      print(f"You don't have enough {itemName}s to sell {amount} {itemName}(s).\n  - You only have {self.inventory[int(itemIndex)][1]} {itemName}(s).")

  def saveAll(self):
    data = []
    data.append(self.inventory)
    data.append(self.money)
    return data