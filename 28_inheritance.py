class BankAccount:
  def __init__(self, accountNumber, balance):
    self.accountNumber = accountNumber
    self.balance = balance

  def deposit(self, amt):
    self.balance += amt
    print(f"You have successfully deposited ${amt}")

  def withdraw(self, amt):
    if self.balance > amt:
      self.balance -= amt
      print(f"You have successfully withdrawn ${amt}")
    else:
      print("Transaction failed. Insufficeint balance")

  def get_balance(self):
    print(f"The balance in your account is ${self.balance}")

# acc1 = BankAccount(1122334455, 10000)
# acc1.get_balance()
# acc1.deposit(1200)
# acc1.get_balance()
# acc1.withdraw(4200)
# acc1.get_balance()

class SavingsAccount(BankAccount):
  def __init__(self, accountNumber, balance, intRate):
    super().__init__(accountNumber, balance)
    self.intRate = intRate

  def calc_interest(self):
    return self.balance * self.intRate

class CurrentAccount(BankAccount):
  pass

s1 = SavingsAccount(44557788, 10000, 0.06)
c1 = CurrentAccount(99887766, 0)

s1.get_balance()
c1.get_balance()

c1.deposit(15000)
c1.get_balance()

s1.withdraw(5500)
s1.get_balance()
print(s1.calc_interest())


# Activtiy 1

class Vehicle:

  def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage

class Bus(Vehicle):
  pass

School_bus = Bus("School Volvo", 100, 12)
print("Vehicle Name: ", School_bus.name, "Speed: ", School_bus.max_speed, "Mileage: ", School_bus.mileage)


# Activity 2

class Person( object ):

  def __init__(self, name, idnumber):
    self.name = name
    self.idnumber = idnumber
  def display(self):
    print(self.name)
    print(self.idnumber)

class Employee( Person ):
  def __init__(self, name, idnumber, salary, post):
    self.salary = salary
    self.post = post

    Person.__init__(self, name, idnumber)

a = Employee("Rahul", 886012, 200000, "Intern")
a.display()


# Activity 3

class Bird:
  def __init__(self):
    print("Bird is ready")

  def whoisThis(self):
    print("Bird")

  def swim(self):
    print("Swim Faster")

class Penguin(Bird):
  def __init__(self):
    super().__init__()
    print("Penguin is ready")

  def whoisThis(self):
    print("Penguin")

  def run(self):
    print("Run Faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()