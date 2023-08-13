numbers = []
for i in range(3):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
print("You entered:", numbers , "\n")


numbers = [int(x) for x in input("Enter three numbers separated by spaces: ").split()]# list comprehension:
print("You entered:", numbers, "\n")

numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]# list comprehension:
print(squares)
print("\n")

city = input(f"Which city are you from? ")
print(f"Nice, I've heard good things about {city}." , "\n")

weight = float(input("Enter your weight in kilograms: "))
print("Your weight is:", weight, "kg", "\n")

values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
str = ["a","d","c"]
string=("sdfsfsdf").split()
print(string)

for i in values:
    print(i)
    
print("\n")
for i in str:
    print(i)
print("\n")   
for i in range(5):  # Loop from 0 to 4
    print(i)

print("\n")

data = "apple,banana,orange,grape"
fruits = data.split(",")  # Splitting the data using a comma as delimiter

print(fruits)

print("\n")


n=['10','3','3','3','3','3']
for i in n:
    print(n)

print("\n")

n=['10','3','3','3','3','3']
for i in n:
    print(i)
    
for i in range(4):
    print(i)

for i in range(n):
    print(i)

n=10
for i in range(2,n):#10 times loop-2 =8 times loop ghurbe
    print(i)