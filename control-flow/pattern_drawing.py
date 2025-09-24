# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to go through rows
while row < size:
    # For loop to print stars in each row
    for col in range(size):
        print("*", end="")
    # Move to next line after finishing a row
    print()
    row += 1

