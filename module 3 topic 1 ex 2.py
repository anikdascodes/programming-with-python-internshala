Year=int(input("Enter the year: "))
if (Year %100==0) and (Year%400==0):
    print("Year" "is leap year")
elif(Year%4==0) and (Year%100!=0):
    print("Year is leap year")
else:
    print("Year is not leap ")