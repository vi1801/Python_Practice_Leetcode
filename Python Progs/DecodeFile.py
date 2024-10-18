def decode(message_file):
    # Read the contents of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Sort the lines based on the numbers
    lines.sort(key=lambda x: int(x.split()[0]))

    # Create a dictionary to store the words
    word_dict = {}

    # Populate the dictionary with words corresponding to each number
    for line in lines:
        num, word = line.split()
        word_dict[int(num)] = word

    # Initialize an empty list to store the decoded message
    decoded_message = []

    # Initialize the current number and line length
    current_num = 1
    line_length = 1

    # Iterate through the dictionary to construct the decoded message
    while current_num in word_dict:
        # Add the word corresponding to the current number to the decoded message
        decoded_message.append(word_dict[current_num])
        # Increment the current number
        current_num += line_length
        # Increment the line length
        line_length += 1

    # Return the decoded message as a string
    return ' '.join(decoded_message)


# Test the function with the provided data file
decoded_message = decode("coding_qual_input.txt")
print(decoded_message)
