def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

my_list = [64, 34, 25, 12, 22, 11, 90]
result = linear_search(my_list, 22)
print(result)  # Prints 4
