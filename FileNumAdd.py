try:
    with open("number_list.txt", "r") as file:
        numbers = file.read()

        numbers_list = [int(num) for num in numbers.split()]

        total = sum(numbers_list)

        print("Numbers from number_list.txt:")
        print(numbers)
        print(f"Total: {total}")

except FileNotFoundError:
    # Handle the case where the file is not found
    print("File 'number_list.txt' not found.")

except Exception as e:
    # Handle other exceptions
    print(f"An error occurred: {e}")
