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

