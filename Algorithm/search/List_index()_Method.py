my_list = [1, 2, 3, 4, 5]
target = 3

try:
    index = my_list.index(target)
    print(f"Target {target} found at index {index}.")
except ValueError:
    print(f"Target {target} not found in the list.")
    
#The index() method of a list can be used to find the index of the first occurrence of an element.