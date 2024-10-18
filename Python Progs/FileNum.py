try:
    with open("number_list.txt", "r") as file:
        # Read all numbers from the file
        numbers = file.read()

        print("Numbers from number_list.txt:")
        print(numbers)

except FileNotFoundError:
    # Handle the case where the file is not found
    print("File 'number_list.txt' not found.")

except Exception as e:
    print(f"An error occurred: {e}")
