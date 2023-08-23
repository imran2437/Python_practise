def sum_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n - 1)

result = sum_of_numbers(5)
print(result)  # Prints 15
