weight=float(input("Enter your weight in kg:"))
height=float(input("Enter your height in m:"))
#calculate the BMI
BMI=weight/(height**2)
if BMI<=18.4:
    print("you are under weight")
elif BMI<=24.9:
    print("you are healthy")
elif BMI<=29.9:
    print("you are over weight")
else:
    print("you are obese")