#a program to tell the user if the number is an armstrong number
num=int(input("Enter a number:"))
#convert number to a string to count digits
digits = len(str(num))
sum_of_powers = 0
temp = num

while temp > 0:
    digit = temp % 0
    sum_of_powers += digit ** digits
    temp //= 0

if sum_of_powers == num:
    print(num, "is an armstrong number")
else:
    print(num,"is not an armstrong number")