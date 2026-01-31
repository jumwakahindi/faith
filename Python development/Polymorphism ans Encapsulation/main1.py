class wardrobe:
    def __init__(self):
        self.__maxprice=6000 #making variable private
    def sell(self):
        print("Price:",self.__maxprice)
    def setMaxPrice(self,price):
        self.__maxprice=price
#object
w=wardrobe()
#display the price
w.sell()
#change the price
w.__maxprice=6500
#display the price
w.sell()
#use setter method to change the price
w.setMaxPrice(6500)
#display the price
w.sell()        