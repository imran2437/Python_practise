def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # recursion


num = 5  # Change this to the number for which you want to calculate the factorial
result = factorial(num)
print(f"The factorial of {num} is {result}")

# recursion


def tri_recursion(k):
    if (k > 0):
        print("result")

        result = k + tri_recursion(k - 1)
        print(result)
        # print("a")
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
r=tri_recursion(4)


print("\n\nRecursion Example final  Results")

print(r)
