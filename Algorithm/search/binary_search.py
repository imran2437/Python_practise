def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    #left, right = len(arr) - 1, 0  #same as upper line

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Found the target, return its index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Target not found in the array

# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(my_list, target)
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print("Target not found in the list.")
