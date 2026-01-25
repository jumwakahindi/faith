from abc import ABC,abstractmethod
#abstract class-used to hide detaiils
class Animal(ABC):
    #abstract method
    @abstractmethod
    def sound(self):
        pass
class Lion(Animal):
     #inherit the sound method
     def sound(self):
         print("A lion roars")
#object to execute the class
p=Lion() 
#print the sound
p.sound()          