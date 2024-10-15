try:
    filename = input("Enter the filename: ")

    with open(filename, 'r') as file:
        content = file.read()
        print(f"File content:\n{content}")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
