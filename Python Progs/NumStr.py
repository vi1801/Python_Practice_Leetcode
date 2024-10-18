input_string = input("Enter a series of single-digit numbers: ")

total = 0

for char in input_string:
    if char.isdigit():
        total += int(char)

print(total)