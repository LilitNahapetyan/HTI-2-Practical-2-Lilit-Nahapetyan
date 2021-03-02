def zip_generator(list1, list2):
    l_1 = len(list1)
    l_2 = len(list2)
    if l_1 <= l_2:
        l = l_1
    else:
        l = l_2
    i = 0
    while l > 0:
        x = (list1[i], list2[i])
        l -= 1
        i += 1
        yield x

list1 = [1,2,3,4]
list2 = [4,7,6,7,8,]

for couple in zip_generator(list1, list2):
    print(couple)

print(list(zip(list1,list2)))