try:
    filename = input("Enter the filename: ")

    with open(filename, 'r') as file:
        content = file.read()
        print(f"File content:\n{content}")

except FileNotFoundError:
    # Handle the case where the file is not found
    print(f"File '{filename}' not found. Creating the file...")

    with open(filename, 'w') as file:
        file.write("File is opened in write mode")

    print("File created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
