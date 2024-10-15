def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def count_primes_in_range(start, end):
    prime_count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            prime_count += 1
    return prime_count


if __name__ == "__main__":
    print(is_prime(326))
    print(is_prime(303))
    print(is_prime(313))
    print(is_prime(351))
    print(count_primes_in_range(100, 151))

