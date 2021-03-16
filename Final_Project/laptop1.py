import csv
import pandas as pd
import re

laptop = pd.read_csv('C:/Users/Admin/Desktop/laptops.CSV',decimal = ',' )

laptop.columns = ['brand', 'model', 'category', 'screen_size', 'screen', 'cpu', 'ram',
                 'storage', 'gpu', 'op_system', 'op_system_version', 'weight', 'price']

def expensive_laptop(n):
    return laptop.nlargest(n, 'price')[['brand','model','price']]

n = int(input("Input count:"))
print(f'The most expensive {n} laptops.')
print(expensive_laptop(n))

#5 ամենամատչելի laptop-ները f’{brand} {model} {price}’ այս ֆորմատով

def smallest_laptop(n):
    return laptop.nsmallest(num, 'price')[['brand','model','price']]

num = int(input("Input count:"))
print(f'The cheapest {n} laptops.')
print(smallest_laptop(n))

#բոլոր օպերացիոն համակարգերը և իրենց laptop-երի քանակը(օրինակ՝ windows: 456, macOS:46, Linux: 876...)
count_laptop_op_system = laptop['op_system'].value_counts()
print(count_laptop_op_system)


def heavy_laptop(n):
    laptop.weight = laptop.weight.apply(lambda w: float(w.strip('kg').strip('kgs')))
    return laptop.nlargest(n, 'weight')[['brand','model','weight']]


print(heavy_laptop(n))

def powerfull_ram(n):
    laptop.ram = laptop.ram.apply(lambda r: int(r[:-2]))
    return laptop.nlargest(n, 'ram')[['brand','model','ram']]

n = int(input("Input count:"))
print(powerfull_ram(n))

count_laptop_ram = laptop['ram'].value_counts()
print(count_laptop_ram)

size = laptop['screen_size'].apply(lambda size:float(size[:-1]))

a,b,c,d = 0,0,0,0

for i in range(len(laptop.index)):
    current_size = size[i]
    if current_size < 10:
        a += 1
    if current_size >= 10 and current_size < 13:
        b += 1
    if current_size >= 13 and current_size < 15:
        c += 1
    else:
        d += 1
print(
    f'''until 10”: {a},
10”-13”: {b},
13”-15”: {c},
15” or more  {d} '''
)

count_laptop_brand = laptop['brand'].value_counts()
print(count_laptop_brand)