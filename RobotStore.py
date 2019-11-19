#CMPT 120 Intro to Programming
#Lab 8 – Working with Objects
#Author: Tyler Vultaggio
#Date: 11/12/2019

# JA: Always remember to add comments to your code

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def isInStock(self,count):
        return self.quantity >= count

    def totalCost(self,count):
        return self.price * count

    def newStock(self,count):
        return self.quantity - count

products = [Product("Ultrasonic range finder", 2.50 ,4),
            Product("Servo motor", 14.99, 10),
            Product("Servo controller", 44.95, 5),
            Product("Microcontroller Board", 34.95, 7),
            Product("Laser range finder", 149.99, 2),
            Product("Lithium polymer battery", 8.99, 8)]

def printStock():
    print()
    print("Available Products")
    print("------------------")
    i = 0
    for product in products:
        if product.isInStock(1):
            print(str(i) +")",product.name, "$", product.price)
            i = i + 1
    print()
     
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        
        if vals[0] == "quit": break
        
        prodId = int(vals[0])
        count = int(vals[1])
        
        if products[prodId].isInStock(count):
            if cash >= products[prodId].price:
                products[prodId].newStock(count)
                cash -= products[prodId].totalCost(count)
                print("You purchased", count, products[prodId].name +".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", products[prodId].name)
main()
