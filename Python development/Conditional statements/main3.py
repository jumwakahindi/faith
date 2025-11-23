attendance = float(input("Enter attendance percentage: "))
if attendance >= 75:
  print("Eligible for exam:")
elif attendance <75:
 print("Not eligible for exam:")
reason = input("provide medical reason: ")
if reason.strip() !="":
    print("Medical reason submitted:", reason)
else:
    print("No medical reason submitted:")