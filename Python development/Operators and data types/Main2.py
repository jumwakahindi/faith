#Asking the user to enter numbers
num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))
#Asking the user to swap the numbers(using pythonic way)
a=10
b=20
a,b= b,a
print(a,b)
#Asking the user to swap numbers(using a temporary variable)
a=5
b=6
temp=a
a=b
b=temp
print(a, b)
#Asking the user to swap numbers(using arithmetic)
a=9
b=8
a=a+b
b=a-b
a=a-b
print(a,b)