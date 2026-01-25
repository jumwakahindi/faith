#parent class
class person:
    #constructor
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    #metod -to display the personsl information
    def display(self):
        print("-----Personal Details-----")
        print(f"Name:{self.name}")
        print(f"Id Number:{self.idnumber}")
#child class
class Employee(person):
    #constructor
    def __init__(self,name,idnumber,salary,position):
        self.salary=salary
        self.position=position
        #call the name and idnumber from parent class
        person.__init__(self,name,idnumber)
name=input("Employee's name:")
idnumber=input("Employee's ID Number")
salary=input("Employee's salary")
position=input("Employee's position")
#object to execute the class
f=Employee(name,idnumber,salary,position)
#call the class method to display the personal details
f.display()
print("salary:",f.salary)
print("position:",f.position)