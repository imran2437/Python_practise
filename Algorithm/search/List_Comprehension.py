my_list = [1, 2, 3, 4, 5]
target = 3

indices = [i for i, x in enumerate(my_list) if x == target]

if indices:
    print(f"Target {target} found at indices {indices}.")
else:
    print(f"Target {target} not found in the list.")
#You can use list comprehensions to filter elements that match a certain condition.