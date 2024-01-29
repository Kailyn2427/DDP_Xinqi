list1 = [1, 2, 3, 4, 5]
list2 = [6,7,'8']
print(len(list1), len(list2))
print(list1+list2)
print(list1*2)
print(1 in list1)
print(1 not in list1)
del list1[0]
print(list1)
print(1 in list1)
print(1 not in list1)
for i in list1:
    print(i)
for i in list1:
    print(i, end='   ')
for i in list1:
    print(i, end='')