while True:
    try:
        inp = int(input("Enter a positive int(or neg number to exit): "))
        if inp < 0:
            raise ValueError("negative number entered. Exited.")

        square = inp ** 2
        print(f"The square of {inp} is: {square}")

    except ValueError as ve:
        print(ve)
        break