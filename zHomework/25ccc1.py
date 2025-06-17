# Roller Coaster Ride

N = int(input("Enter Place in Line: "))
C = int(input("Enter Number of Cars of Train: "))
P = int(input("Enter Number of People in Single Car: "))

capacity = C * P

if N <= capacity:
    print("yes")
else:
    print("no")

