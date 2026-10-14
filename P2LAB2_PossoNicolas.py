# Nicolas Posso
# October 14, 2026
# P2LAB2
# Using a dictionary

vehicles = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

keys = vehicles.keys()
print(keys)

vehicle = input("\nEnter a vehicle to see it's mpg: ")

print(f"\nThe {vehicle} gets {vehicles[vehicle]} mpg.")

miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))

gallons = miles / vehicles[vehicle]

print(f"\n{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")
