# Donut Shop

D = int(input("Initial Number of Donuts: "))
E = int(input("Number of Events: "))

donuts = D

for _ in range(E):
    operation = input("Sign for Donuts Baked/ Sold: ")
    Q = int(input("Donuts Per Event: "))

    if operation == '+':
        donuts +=Q
    elif operation == '-':
        donuts -=Q

print(donuts)
