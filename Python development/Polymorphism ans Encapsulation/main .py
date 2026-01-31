class Payment:
    #constructor
    def __init__(self,amount,method):
        self.amount= amount
        self.method= method
    #method to process payment
    def process_paymrnt(self):
        print("Process the payment of ", self.amount, "using", self.method)  
#paypal payment
class paypal(Payment):
    def __init__(self, amount, method):
        super().__init__(amount, method)
    def process_payment(self):
        print("Processing paypal payment of ", self.amount)            
#object to execute the methods
payment1=paypal(1000, "Paypal method")
payment1.process_payment()