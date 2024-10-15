while True:
    try:
        inp = int(input("input an integer: "))
        break
    except ValueError:
        print("Error: Enter a valid integer")
print("you entered: ", inp)