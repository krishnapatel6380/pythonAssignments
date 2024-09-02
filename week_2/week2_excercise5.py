# Conversion factors
LOTS_TO_GRAMS = 13.3
POUNDS_TO_LOTS = 32
TALENTS_TO_POUNDS = 20

# Input from the user
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

# Convert talents to pounds, then to lots, and then to grams
total_lots = (talents * TALENTS_TO_POUNDS * POUNDS_TO_LOTS) + (pounds * POUNDS_TO_LOTS) + lots
total_grams = total_lots * LOTS_TO_GRAMS

# Convert grams to kilograms and remaining grams
kilograms = int(total_grams // 1000)
remaining_grams = total_grams % 1000

# Output the result
print("The weight in modern units:")
print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")
