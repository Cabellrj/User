class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


ruben = User("Ruben")
kim = User("Kim")
rick = User("Rick")

ruben.make_deposit(100)
ruben.make_deposit(200)
ruben.make_deposit(50)
ruben.make_withdrawl(45)
ruben.display_user_balance()

kim.make_deposit(1000)
kim.make_deposit(1000)
kim.make_deposit(500)
kim.make_withdrawl(300)
kim.display_user_balance()

rick.make_deposit(1500)
rick.make_deposit(1000)
rick.make_deposit(5000)
rick.make_withdrawl(3000)
rick.display_user_balance()


kim.transfer_money(400, ruben)