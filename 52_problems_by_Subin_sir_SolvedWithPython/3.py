# for num in sorted(range(1000, 0, -1), reverse=True):
#     print(num)
count = 0

for i in range(1, 1001):#list e 1001 ta items ase, print kora suru korce 1 theke o bad diye
    print(i, end='\t')
    count += 1
    if count == 5:
        print()  # Move to the next line
        count = 0



