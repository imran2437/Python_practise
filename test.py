def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        print(n)
        
        # return n * factorial(n - 1)  # recursion
        result=n * factorial(n - 1)
        print("\n")
        print(result)
        return result

num = int(input("write a number to calculate factorial "))  # Change this to the number for which you want to calculate the factorial
result = factorial(num)
print(f"The factorial of {num} is {result}")