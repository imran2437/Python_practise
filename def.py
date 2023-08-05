def func(ab: list) -> None:
    ab[0] = 99
    print((ab))

if __name__ == "__main__":
    li = [1, 2, 3]
    print(id(li))
    print(id(li.copy()))
    func(li.copy()) #pass by value
    print(li)
    func(li) #pass by reference original list is modified
    print(li)