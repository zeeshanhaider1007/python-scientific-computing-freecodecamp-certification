
class Category:
  def __init__ (self, category):  
    self.ledger = []
    self.category = category
    self.net_balance = 0

  def deposit(self, amount, description=""):
    self.net_balance += amount
    self.ledger.append({"amount": amount, "description": description})
  
  def withdraw(self, amount, description=""):
    if not self.check_funds(amount):
      return False
    else:
      self.net_balance-=amount
      self.ledger.append({"amount": amount*-1, "description": description})
      return True
      
  def get_balance(self):
    return self.net_balance
    
  def check_funds(self, amount):
    if amount > self.net_balance:
      return False
    else:
      return True
      
  def transfer(self, amount, category):
    if self.check_funds(amount):
      category.deposit(amount, f"Transfer from {self.category}")
      self.withdraw(amount,f"Transfer to {category.category}")
      return True
    else:
      return False
  def __str__(self):
    x = self.category.center(30, "*")
    for ledge in self.ledger:
      message = "{:.2f}".format(float(str(ledge["amount"])[:7]))
      align = ">"
      fill = " "
      width = 7 + (23-len(ledge["description"][:23]))
      stri  = f'{message:{fill}{align}{width}}'
      stri = ledge["description"][:23]+stri
      x =  x + "\n" + stri
    x = x +"\n"+ f"Total: {self.net_balance}"
    return x

def find_nearest(array, value):
    array1 = [abs(val - value) for val in array]
    return array[array1.index(min(array1))]
def create_spend_chart(categories):
  array = list(range(0,110,10))
  withdrawls = dict()
  for category in categories:
    withdrawls[category.category] = 0.
    for ledge in category.ledger:
      if ledge["amount"] < 0:
        withdrawls[category.category] += ledge["amount"]*-1

  percentages = dict()
  for key in withdrawls:
    percentages[key] = withdrawls[key]/sum(list(withdrawls.values())) * 100
    
    percentages[key] = find_nearest(array,percentages[key])
  graph = "Percentage spent by category\n"
  # print(percentages)
  for i in array[::-1]:
    fill = ""
    for j  in percentages:
      
      if percentages[j] >= i:
        fill += "o  "
      else:
        fill += "   "
    vertical = f'{i:>3}'
    graph += f"{vertical}| {fill}"
    graph+="\n"
  n = len(f"{vertical}| {fill}")
  graph+=f'{"-"*(n-4):>{n}}'
  graph+="\n"
  counter = max(list(map(len,list(percentages.keys()))))
  for count in range(counter):
    fill = ""
    for key in list(percentages.keys()):
      if len(key)-1 < count:
        fill += " " * 3
      else:
        fill += f'{key[count]:<3}'
    if count==counter-1:
      graph+=f'{fill:>{n}}'
    else:
      graph+=f'{fill:>{n}}'+"\n"
  return graph