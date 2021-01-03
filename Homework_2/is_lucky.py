number = input("Print number which contains an even number of characters: ")

num = [int(i) for i in list(number[0:int(len(number))])]

half_sum = 0
sum = 0
for i in range(0, int(len(number)//2)):
    half_sum = half_sum + num[i]
for i in range(0, int(len(number))):
    sum = sum + num[i]
if half_sum == sum/2:
    print("Yes")
else:
    print("No")
