# Get user input for the full name
full_name = input("Enter your full name: ")

print("Initials:", full_name)

names = full_name.split()

# Extract the first letter of each name and capitalize it
initials = [name[0].upper() + '.' for name in names]

# Join the initials to form the output
initials_output = ' '.join(initials)

print(initials_output)
