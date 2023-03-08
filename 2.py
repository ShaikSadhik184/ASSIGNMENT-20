def is_prime(num):
    # Check if the number is less than 2, which is not a prime number
    if num < 2:
        return False
    
    # Loop through each integer from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        # Check if the number is divisible by any integer in this range
        if num % i == 0:
            return False
    
    # If the number is not divisible by any integer in the range, it is prime
    return True
# Check if the number 7 is prime
is_prime_7 = is_prime(7)
print(is_prime_7)  # Output: True

# Check if the number 12 is prime
is_prime_12 = is_prime(12)
print(is_prime_12)  # Output: False
