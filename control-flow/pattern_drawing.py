# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using a while loop
row = 0
while row < size:
    for col in range(size):
        print("*", end="")  # Print asterisk without a new line
    print()  # Move to the next line after finishing a row
    row += 1  # Increment the row counter