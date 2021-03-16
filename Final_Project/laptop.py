import csv
import pandas as pd

class laptops:
    def __init__(self,brand, model_name, category, screen_size,screen, cpu, ram, storage,
                 gpu, operating_system, operating_system_version, weight, price):
        self.brand = brand
        self.model_name = model_name
        self.category = category
        self.screen_size = screen_size
        self.screen = screen
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu
        self.operating_system = operating_system
        self.operating_system_version = operating_system_version
        self.weight = weight
        self.price = price


    @property
    def get_brand(self):
        return self.brand

    @property
    def get_model_name(self):
        return self.model_name

    @property
    def get_category(self):
        return category

    @property
    def get_screen_size(self):
        return self.screen_size

    @property
    def get_cpu(self):
        return self.cpu

    @property
    def get_ram(self):
        return self.ram

    @property
    def get_storage(self):
        return self.storage

    @property
    def get_gpu(self):
        return self.gpu

    @property
    def get_operating_system(self):
        return self.operating_system

    @property
    def get_operating_system_version(self):
        return self.operating_system_version

    @property
    def get_weight(self):
        return self.weight

    @property
    def get_price(self):
        return float(self.price)


def laptop():
    with open('C:/Users/Admin/Desktop/laptops.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            yield laptops(
                brand=row['Manufacturer'],
                model_name=row['Model Name'],
                category=row['Category'],
                screen_size=row['Screen Size'],
                screen=row['Screen'],
                cpu=row['CPU'],
                ram=row['RAM'],
                storage=row['Storage'],
                gpu=row['GPU'],
                operating_system=row['Operating System'],
                operating_system_version = row['Operating System Version'],
                weight=row['Weight'],
                price = row['Price (Euros)'],
            )

#բոլոր օպերացիոն համակարգերը և իրենց laptop-երի քանակը
systems = {}
for comp in laptop():
    if comp.operating_system in systems.keys():
        systems[comp.operating_system] += 1
    else:
        systems[comp.operating_system] = 1
print(systems)



#բոլոր չափի RAM-երը և իրենց մոդելների քանակը
rams =  {}
for comp in laptop():
    if comp.ram in rams.keys():
        rams[comp.ram] += 1
    else:
        rams[comp.ram] = 1
print(rams)

#էկրանի չափսերը և իրենց մոդելների քանակը
a, b, c, d = 0,0,0,0

for comp in laptop():
    if float(comp.screen_size[:-1]) < 10:
        a += 1
    if float(comp.screen_size[:-1]) >= 10 and float(comp.screen_size[:-1]) < 13:
        b += 1
    if float(comp.screen_size[:-1]) >= 13 and float(comp.screen_size[:-1]) < 15:
        c += 1
    if float(comp.screen_size[:-1]) >= 15:
        d += 1
print(f"(until 10”:{a}, 10”-13”:{b}, 13”-15”: {c},15” or more {d}) ")

#բոլոր brand-երը և իրենց մոդելների քանակը
brands = {}
for comp in laptop():
    if comp.brand in brands.keys():
        brands[comp.brand] += 1
    else:
        brands[comp.brand] = 1
print(brands)



#5 ամենահզոր RAM ունեցող laptop-ները
def n_powerfull_ram_laptop(count):
    laptop_ = laptop()
    comp_ = next(laptop_)
    i = 0
    list_ = []
    list_n = []
    for comp in laptop_:
        for i in range(count):
            if len(list_) < count:
                list_.append(float(comp.ram[:-2]))
                list_n.append(f"{comp.brand},{comp.model_name},{comp.ram}")
            elif list_[i] < float(comp.ram[:-2]):
                list_[i] = float(comp.ram[:-2])
                list_n[i] = f"{comp.brand},{comp.model_name},{comp.ram}"
                break
    print(f"{count} powerfull laptops")
    for j in list_n:
        print(j)

n_powerfull_ram_laptop(5)

#5 ամենաթանկ laptop-ները
def n_expensive_laptop(count):
    laptop_exp = laptop()
    comp_ = next(laptop_exp)
    i = 0
    list_ = []
    list_n = []
    for comp in laptop_exp:
        for i in range(count):
            if len(list_) < count:
                list_.append(float(comp.price.replace(",", ".")))
                list_n.append(f"{comp.brand},{comp.model_name},{comp.price}")
            elif list_[i] < float(comp.price.replace(",", ".")):
                list_[i] = float(comp.price.replace(",", "."))
                list_n[i] = f"{comp.brand}, {comp.model_name}, {comp.price} Euro"
                break
    print(f"{count} expensive laptops")
    for j in list_n:
        print(j)


