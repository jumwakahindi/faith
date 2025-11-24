#a program to create a pattern
rows=int(input("Enter the number of rows:"))
#outer loop-print each row
for w in range(1,rows+1):
    #inner loop-print each star in a row
    for x in range(w):
        print("*",end=' ')
    #print a new row/line
    print()