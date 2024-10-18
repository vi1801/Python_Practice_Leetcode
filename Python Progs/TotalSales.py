def main():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sales = []

    for day in days:
        sales_in = float(input(f"Enter sales for {day}: "))
        sales.append(sales_in)

    total_sales = sum(sales)

    print(f"Total sales for the week: {total_sales}")

if __name__ == "__main__":
    main()