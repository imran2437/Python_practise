# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York',3:10}

# Accessing values
print(my_dict['name'])  # Prints 'Alice'
print(my_dict[3])
# Modifying values
my_dict['age'] = 31
print(my_dict)

# Iterating through a dictionary
for key, value in my_dict.items():
    print(key, value)
    print(key)
    print(value)
    
    
    
    
# Take input as a string
input_str = input("Enter a dictionary (e.g., {'name': 'Alice', 'age': 30}): ")

# Use eval() to convert the input string into a dictionary
try:
    user_dict = eval(input_str)

    # Now you can work with the user-provided dictionary
    print("User-provided dictionary:")
    for key, value in user_dict.items():
        print(key, value)
except SyntaxError:
    print("Invalid dictionary format. Please enter a valid dictionary.")


dict={'a':1,'b':2}
dict['c']=3
print(dict)
for key ,value in dict.items():
    print(value)

del dict ['c']
print(dict)