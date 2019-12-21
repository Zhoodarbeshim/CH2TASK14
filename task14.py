# for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     print(i * 2)
nums = input("enter a number: ").split(' ')
for x in nums:
    if int(x) % 2 == 0:
        print(x)
    else:
        continue