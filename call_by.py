def modify_value(x):
    x = 20  # Changes made to the formal parameter won't affect the original argument
    print("Inside function:", x)
    return x

num = 10

print("Before function call:", num)
modify_value(num)
print("After function call:", num)
#this is call by value method in python where the value of the variable is passed to the function and the changes made to the formal parameter won't affect the original argument as seen in the above example where the value of num is not changed even after the function call is made. 
#........................#

#now let's see call by reference method in python
def modify_reference(x):
    x[0] = 20  # Changes made to the formal parameter affect the original argument

num_list = [10]

print("Before function call:", num_list[0])
modify_reference(num_list)
print("After function call:", num_list[0])
#this is call by reference method in python where the reference of the variable is passed to the function and the changes made to the formal parameter affect the original argument as seen in the above example where the value of num_list is changed even after the function call is made. 


# Difference between C and Python in this Scenario:

# The primary difference in this scenario between C and Python is related to the type of data used for call by reference:

#     In C, call by reference is achieved using pointers. We pass the memory address of a variable to the function using a pointer. C allows direct manipulation of pointers, which means we can modify the value at the memory address pointed by the pointer.

#     In Python, the concept of call by reference is achieved using references to objects. In the example, we used a list as the argument to simulate call by reference. Python does not have pointers like C, but almost everything in Python is an object and behaves like a reference. However, Python does not allow direct manipulation of references like C does with pointers. To achieve call by reference behavior, we can use mutable objects (e.g., lists or dictionaries) as arguments since their reference can be modified inside the function.

# It's important to note that Python does not have true call by reference as in C. Instead, it follows the call by object reference model, which allows for similar behavior when using mutable objects. For non-mutable objects (e.g., integers, strings, tuples), Python behaves more like call by value. Understanding this distinction is crucial for correctly handling mutable and immutable objects when passing arguments to functions in Python.