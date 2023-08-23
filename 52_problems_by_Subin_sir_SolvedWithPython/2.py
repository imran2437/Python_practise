t=int(input("Loop  "))
for _ in range(t):
    k=input("Enter a number")
    last=int(k[-1])
    if last%2==0:
        print("even")
    else:
        print("odd")