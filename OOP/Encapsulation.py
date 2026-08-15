class BankAccount:
  def __init__(self, balance):
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
  def withdraw(self, amount):
    self.balance -= amount
  def withdraw_percentage(self, percentage):
    amount = self.balance * (percentage / 100)
    self.balance -= amount
    return amount

account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
account.withdraw_percentage(10)
print(account.balance)
