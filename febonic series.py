def fibonacci_generator(limit):
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Loop to generate Fibonacci numbers until the limit
    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence

# Example usage:
limit = 100000
fib_numbers = fibonacci_generator(limit)
print(f"Fibonacci numbers up to {limit}: {fib_numbers}")
