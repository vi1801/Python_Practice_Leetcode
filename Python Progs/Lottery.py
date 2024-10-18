import random
def generate_lottery_number():
    lottery_number = []
    for _ in range(7):
        lottery_number.append(random.randint(0, 9))
    return lottery_number

def main():
    lottery_numbers = generate_lottery_number()

    print("Generated Lottery Number:")
    for digit in lottery_numbers:
        print(digit)

if __name__ == "__main__":
    main()
