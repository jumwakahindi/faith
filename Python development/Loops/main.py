#a program to print the mathematical table of a number entered by user
num=int(input("Enter a number to print its mathematical table:"))
for i in range(1,11):
  print(f"{num}x{i}={num*i}")