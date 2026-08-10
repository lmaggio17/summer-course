##Problem 1:
print("Case sensitive. Please enter your choice exactly as shown.")
choice = input(
    'Would you like to enter "Miles above Mars" or "Kilometers above Mars"? '
)

if choice == "Miles above Mars":
    miles = float(input("Enter the number of miles: "))

    yards = miles * 1760
    feet = miles * 5280
    inches = miles * 63360

    print(f"Yards: {yards}")
    print(f"Feet: {feet}")
    print(f"Inches: {inches}")

elif choice == "Kilometers above Mars":
    kilometers = float(input("Enter the number of kilometers: "))

    meters = kilometers * 1000
    centimeters = kilometers * 100000
    millimeters = kilometers * 1000000

    print(f"Meters: {meters}")
    print(f"Centimeters: {centimeters}")
    print(f"Millimeters: {millimeters}")

else:
    print("Invalid choice.")


##Problem 2:
# #The first Automatron produces 2 circular pizzas (15 inch diameter) that require 20 units of dough.
# The second Automatron makes a larger, equilateral triangle pizza, side length 20, that also requires 20 units of dough.
# The third Automatron creates a square pizza with side length 18, that only requires 18 units of dough.

# As the Chief Engineer, you decide to write a Python Script to figure out
# which Automatron is most efficient.  Once we avert total disaster and save all 1000 lives on
# board of the incoming shuttle,
# we will want to welcome them with some warm, Martian pizza after all.

import math

# Automatron 1 - two circular pizzas
radius = 15 / 2
circle_area = math.pi * radius**2
automatron1_area = circle_area * 2
automatron1_efficiency = automatron1_area / 20

# Automatron 2 - equilateral triangle
automatron2_area = (math.sqrt(3) / 4) * 20**2
automatron2_efficiency = automatron2_area / 20

# Automatron 3 - square
automatron3_area = 18**2
automatron3_efficiency = automatron3_area / 18

print(f"Automatron 1 efficiency: {automatron1_efficiency:.2f}")
print(f"Automatron 2 efficiency: {automatron2_efficiency:.2f}")
print(f"Automatron 3 efficiency: {automatron3_efficiency:.2f}")

if (
    automatron1_efficiency >= automatron2_efficiency
    and automatron1_efficiency >= automatron3_efficiency
):
    print("The most efficient Automatron is: Automatron 1")
elif (
    automatron2_efficiency >= automatron1_efficiency
    and automatron2_efficiency >= automatron3_efficiency
):
    print("The most efficient Automatron is: Automatron 2")
else:
    print("The most efficient Automatron is: Automatron 3")


##Problem 3:
import math

total_fuel = 0

with open(
    "C:\\Users\\Maggio\\Desktop\\testing\\summer-course\\Z - Final Project\\input.txt",
    "r",
) as file:
    for line in file:
        mass = int(line.strip())
        fuel = math.floor(mass / 3) - 2
        total_fuel += fuel

print(f"Total fuel required: {total_fuel}")
