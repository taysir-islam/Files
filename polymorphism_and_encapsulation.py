#### Project1
class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = cat("Kittyo", 2.5)  
dog1 = dog("Doggyo", 3)       

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()

### Project2    

class computer:
    def __init__(self):
        self.__maxprice = 900

    def price(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price

c = computer()
c.price()

# change the price
c.__maxprice = 1000
c.price()

# using setter function
c.setMaxPrice(1000)
c.price()

### Project3
class bankaccount:
    def __init__(self,accountnumber,accountname,initial_balance=0):
        self.accountnumber = accountnumber
        self.accountname = accountname
        self.balance = initial_balance

    def get_accountnumber(self):
        return self.accountnumber

    def get_accountname(self):
        return self.accountname 

    def get_balance(self):
        return self.balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Your new balance is ${self.balance}.")
        else:
            print("Invalid deposit amount.must be positive") 

    def withdraw(self,amount):
        if amount > 0:
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. Your new balance is ${self.balance}.")
            else:
                print("Insufficient funds.")      
        else:
            print("Invalid withdraw amount.must be positive") 

    def display_account_info(self):
        print(f"Account number: {self.accountnumber}")
        print(f"Account name: {self.accountname}")
        print(f"Balance: ${self.balance}")   


account1 = bankaccount(123456789,"John Doe",1000)

print(account1.get_accountnumber())
print(account1.get_accountname())
print(account1.get_balance())

account1.deposit(500)
account1.withdraw(200)
account1.withdraw(200000000)

account1.deposit(-500)
account1.withdraw(-200)

account1.display_account_info()

class savingsaccount(bankaccount): # Inheritance
    def __init__(self, account_number, account_holder_name, initial_balance=0, interest_rate=0.05):
        super().__init__(account_number, account_holder_name, initial_balance) # Call parent class constructor
        self._interest_rate = interest_rate # Encapsulated attribute specific to SavingsAccount

    def get_interest_rate(self):
        return self._interest_rate

    def apply_interest(self):
        interest = self.balance * self._interest_rate
        self.balance += interest
        print(f"Interest of ${interest} applied. New balance: ${self.balance}")


savings = savingsaccount("9876543210", "Jane Smith", 5000, 0.02)
savings.display_account_info()
savings.apply_interest()
savings.display_account_info()