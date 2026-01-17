#create the class
class student:
    #assign varibles inside the class
    grade=12
    print("Hello I am in grade ",grade)
    name="Monicah"
    #create a method-print a welcome message
    def welcome(self):
        print("Welcome to my website")
    #metod-print student details
    def details(self): 
        print(f"My name is {self.name} and I am in grade {self.grade}") 
#create an object to execute the class
ob=student() 
#execute all the metods usimg the object
ob.welcome()
ob.details()
  