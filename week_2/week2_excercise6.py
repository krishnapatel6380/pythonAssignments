import random

# Generate a 3-digit code where each number is between 0 and 9
digit1 = random.randint(0, 9)
digit2 = random.randint(0, 9)
digit3 = random.randint(0, 9)
code_3_digit = str(digit1) + str(digit2) + str(digit3)

# Generate a 4-digit code where each number is between 1 and 6
digit4 = random.randint(1, 6)
digit5 = random.randint(1, 6)
digit6 = random.randint(1, 6)
digit7 = random.randint(1, 6)
code_4_digit = str(digit4) + str(digit5) + str(digit6) + str(digit7)

# Output the results
print("3-digit combination lock code:", code_3_digit)
print("4-digit combination lock code:", code_4_digit)
