# There are two approaches of programming!

# 1) POPs : procedural oriented programming system : function based programming!
# 2) OOPs : object oriented programming system : class based programming!

# OOPS : 

# 6 key points of oops :

# class
# object / instance

# pillars of oops
# inheritance
# encapsulation
# polymorphism
# abstraction


# you are creating a game like pubg, COD, free fire

# 100 enemies
# 1 player
# fire - 

# before the game begins : it will create/generate 100 players in a game

# 1) you create 100 players for each game
# 2) create 1 player and use it 100 times : 

# reusing the code, oop

# food delivery : zomato, swiggy (restaurant, customers, orders)

# PascalCase


# blue-print
class Restaurant:

    # properties of restaurant

    # dunder method to initialize object
    # magic method

    # we don't need to call this method to get output

    # init : initialization : 
    def __init__(self, name, city, cuisin):
        self.name = name
        self.city = city
        self.cuisin = cuisin

        print(f'{self.name} is a restaurant in {self.city} city with {self.cuisin} food')

    # methods of restaurant

    def displayInfo(self):
        return f'{self.name} is a restaurant in {self.city} city with {self.cuisin} food'
    
    def get_details(self):
        return f'The restaurant is {self.name}'


class Customer:

    def __init__(self, name):
        self.name = name
        self.__wallet_balance = 0 # __ private variable / private access modifier
    # I need to create a functionality to place order!

    def place_order(self, restaurant, food_item):
        print(f'{self.name} has ordered {food_item} from {restaurant.name}')

    def get_details(self):
        return f'The Customer is {self.name}'

    # add money, and make payment

    def add_money(self, amount):
        if amount > 0:
            self.__wallet_balance += amount
            print(f'{amount} is added to your walled!')
        else:
            print('invalid amount!')


    def make_payment(self, amount):
        if amount <= self.__wallet_balance:
            self.__wallet_balance -= amount
            print(f'payment of {amount} made!')
        else:
            print('insufficient balance!')
    
    def check_balance(self):
        return self.__wallet_balance



# inheritance : inherting properties of parent class to child class
# to get the property from your parent class, we use super keyword


class Order(Customer):
    def __init__(self, name, order_id, food_item):
        super().__init__(name)
        self.order_id = order_id
        self.food_item = food_item

    def order_summery(self):
        print(f'order no: {self.order_id} : {self.name} has ordered {self.food_item}')

    def get_details(self):
        return f'the order id is {self.order_id}'

class DeliveryPerson:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def get_details(self):
        return f'The delivery person is {self.name}'

# polymorphism : one function having multiple forms
# I will create one common function in each class, and it will produce different result for each class!


# 1) step : to create an instance of the class


# an object or an instance of the restaurant

# fouxy = Restaurant()

# fouxy.name = "Fouxy"
# fouxy.city = "Indore"


# print(fouxy.displayInfo())

# lapinoz = Restaurant()

# lapinoz.name = "Lapinoz"
# lapinoz.city = "Ahmedabad"

# print(lapinoz.displayInfo())


dominoz = Restaurant("Dominoz", "NYC", "pizza")


nikhil = Customer('Nikhil')
nikhil.add_money(1000)
nikhil.make_payment(500)
print(nikhil.check_balance())
first_order = Order(nikhil.name, 999, "Cold drink")

dp = DeliveryPerson("Harsh", "Washington")

# print(dominoz.get_details())
# print(nikhil.get_details())
# print(first_order.get_details())
# print(dp.get_details())
# nikhil.place_order(dominoz, "Garlic bread")
# first_order.order_summery()
# print(dominoz.displayInfo())


