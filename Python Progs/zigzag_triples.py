# check if triples of consecutive elements in an array form a zigzag pattern, and return the result as an array
def zigzag_triples(numbers):
    # Initialize the result array of length len(numbers) - 2
    result = [0] * (len(numbers) - 2)

    # Iterate over the numbers array and check triples
    for i in range(len(numbers) - 2):
        a, b, c = numbers[i], numbers[i + 1], numbers[i + 2]

        # Check if the triple (a, b, c) forms a zigzag pattern
        if (a < b > c) or (a > b < c):
            result[i] = 1
        else:
            result[i] = 0

    return result


# Example usage:
numbers = [1, 3, 2, 4, 6, 5, 7]
print(zigzag_triples(numbers))  # Output: [1, 1, 0, 1, 1]
