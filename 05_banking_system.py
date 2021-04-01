# banking system using OOP
# Parent class: User
# Holds details about a user
# Has a function to show user details
# Child class: Bank
# Stores details about the account balance
# Stores details about amount
# Allows for deposits, withdraw, view balance

class User():

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details: ")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

class Bank(User):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Account balance has been updated: ", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("{} is withdrawn, Account balance now is {}".format(amount, self.balance))
        else:
            print("Insufficient balance")

    def view_balance(self):
        self.show_details()
        print("Account balance has been updated: ", self.balance)







if __name__ == '__main__':
    johan = Bank('Johan', 21, 'Male')
    johan.show_details()
    johan.deposit(50)
    johan.withdraw(30)
    johan.withdraw(50)
    johan.deposit(500)
    johan.view_balance()


