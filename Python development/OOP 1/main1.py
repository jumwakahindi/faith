#create a class
class cow:
    #class variable
    species="animal"
    #init method
    def __init__(self,name,age):
       #the variables are assigned to a class
       self.name=name
       self.age=age
 #objects to assign values
angus=cow("angus",20)
Boran=cow("boran",15)
print("angus is an {}".format(angus.species))
print("boran is an {}".format(Boran.species))  