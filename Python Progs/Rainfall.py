# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    rainfall = []
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    for month in months:
        rainfall_input = float(input(f"Enter rainfall for {month}: "))
        rainfall.append(rainfall_input)

    # Calculate total rainfall
    total_rainfall = sum(rainfall)

    # average monthly rainfall
    average_rainfall = total_rainfall / len(rainfall)

    # Find month with the highest and lowest rainfall
    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)
    max_month = months[rainfall.index(max_rainfall)]
    min_month = months[rainfall.index(min_rainfall)]

    # Display results
    print(f"Total rainfall for the year: {total_rainfall} units")
    print(f"Average monthly rainfall: {average_rainfall} units")
    print(f"Month with the highest rainfall: {max_month} ({max_rainfall} units)")
    print(f"Month with the lowest rainfall: {min_month} ({min_rainfall} units)")


if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
