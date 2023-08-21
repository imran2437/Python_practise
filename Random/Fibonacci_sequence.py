# def fibonacci_recursive(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# num_terms = 10  # Change this to the number of Fibonacci terms you want
# fibonacci_sequence = [fibonacci_recursive(i) for i in range(num_terms)]
# print(f"Fibonacci sequence with {num_terms} terms:", fibonacci_sequence)


# without recursive
def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    return fib_sequence

num_terms = 10  # Change this to the number of Fibonacci terms you want
fibonacci_sequence = fibonacci_iterative(num_terms)
print(f"Fibonacci sequence with {num_terms} terms:", fibonacci_sequence)
