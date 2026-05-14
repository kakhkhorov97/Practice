'''Class Deep

(1) Encapsulation
(2) Inheritance
(3) Plimorphism
'''
print("===== Encapsulation ========")
# Encapsulation > Public __private _Protected


class Account():
    # state
    description = "The class that makes encapsulation"

    # Constractor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # Method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.amount -= amount

    @property
    def holder(self):
        return self.__owner


def change_ownership(self, new_owner):
    print("change_ownership:", new_owner)
    self.__owner = new_owner

    my_account = Account("Shawn", 1000)
    my_account.get_balance()

    print("---------")


my_account.deposit(8000)
my_account.withdraw(350)
my_account.get_balance()

print("---------")


try:
    result = my_account.amount
    print("result:", result)

except Exception as err:
    print("No amount:",  err)


account_owner = my_account.holder
print("account_owner:", account_owner)
