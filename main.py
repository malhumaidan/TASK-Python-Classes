class Wallet:
    
    def __init__(self, money=0):
        self.money = money
        

    def credit(self, amount):
        self.money = self.money + amount
        print(f"Your credit balance is {self.money}")
        

    def debit(self, amount):
        self.money = self.money - amount
        print(f"Your debit balance is {self.money}")



class Person:
    # Implement the code here
    def __init__(self, name, location, money):
        self.name = name
        self.location = location
        self.wallet = Wallet(money)


    def moveTo(self, point):
        self.location = point

        print(f"your updated location is {self.location}")



person = Person("Moh", 5, 50)


class Vendor(Person):
    # implement Vendor!
    def __init__(self, name, location, money):
        super().__init__(name, location, money)
        self.range = 5
        self.price = 1

    def sellTo(self, customer, number_of_icecreams):
        self.moveTo(customer.location)
        self.wallet.credit(number_of_icecreams*self.price)
        customer.wallet.debit(number_of_icecreams*self.price)
        print(f"{number_of_icecreams} Icecreams were sold")


vendor = Vendor("Abdallah", 3, 6)


class Customer(Person):
    # implement Customer!
    def __init__(self, name, location, money):
        super().__init__(name, location, money)

    def _is_in_range(self, vendor):
        distance = abs(vendor.location - self.location)
        if distance <= vendor.range:
            print("customer is in range")
            return True
        else:
            print("customer is not in range")
            return False

    def _have_enough_money(self, vendor, number_of_icecreams):
        if self.wallet.money >= number_of_icecreams*vendor.price:
            print("You have enough money")
            return True
        else:
            print("You don't have enough money")
            return False


    def request_icecream(self, vendor, number_of_icecreams):
        if self._is_in_range(vendor) and self._have_enough_money(vendor, number_of_icecreams):
            vendor.sellTo(self, number_of_icecreams)
            print("a request has been made.")
        else:
            print("a request can't be made.")


customer = Customer("Abdallah", 3, 6)

customer.request_icecream(vendor, 6)

