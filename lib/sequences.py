#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])  # Empty list for non-positive length
        return

    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < length:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)

    print(fibonacci_sequence[:length])  # Ensure the list is exactly the given length
print_fibonacci(100)