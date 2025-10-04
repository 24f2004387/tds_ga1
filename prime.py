def is_prime(num):
    """Checks if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_nth_prime(n):
    """Finds the nth prime number."""
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

if __name__ == "__main__":
    nth_prime = 10
    prime_number = find_nth_prime(nth_prime)
    print(f"The {nth_prime}th prime number is: {prime_number}")
