input_str = input("Enter a String: ")

output_str = ''.join(['!' if char.lower() in 'aeiou' else char for char in input_str])

print("Modified: ", output_str)