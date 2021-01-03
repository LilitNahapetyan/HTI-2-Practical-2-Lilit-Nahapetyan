numbers = [int(num) for num in input("Enter a list element separated by space: ").split()]
#In this List will be the products of adjacent elements
adj_el = []
for i in range(len(numbers)-1):
    adj_el.append(numbers[i]*numbers[i+1])
print(max(adj_el))



