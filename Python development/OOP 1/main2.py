class Robot:
    def __init__ (self, name, model, purpose):
       self.name=name
       self.model=model
       self.purpose=purpose 
    #method to intoduce the robot
    def introduce(self):
        print("Hello world")  
        print(f"My name is {self.name}.") 
        print(f"I am a model {self.model}.")
        print(f"My purpose is to {self.purpose}.")
#creating an object
my_robot = Robot("AquaBot", "AB-2026", "assist in marine engineering tasks") 
#calling
my_robot.introduce()  