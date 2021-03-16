import re
import csv
class Laptop:
    def __init__(self,manufacturer,model_name,category,screen_size,screen,cpu,ram,storage,gpu,
    operation_system,weight,price,operating_system_version=None):
        self.manufacturer=manufacturer
        self.model_name=model_name
        self.category=category
        self._screen_size=None
        self.screen_size=screen_size
        self.screen=screen
        self.cpu=cpu
        self._ram=None
        self.ram=ram
        self.storage=storage
        self.gpu=gpu
        self.operation_system=operation_system
        self.weight=weight
        self._price=None
        self.price=price
        self.operating_system_version=operating_system_version
    @property
    def screen_size(self):
        return self._screen_size
    @screen_size.setter
    def screen_size(self, value):
        if value[-1]=='"':
            value=value[:-1]
        else:
            raise ValueError('Screen size must be int or float!')
        value=float(value)
        self._screen_size = value
    @property
    def ram(self):
        return self._ram
    @ram.setter
    def ram(self, value):
        if re.fullmatch("^[1-9]\d*$", value):
            self._ram=f"{value}GB"
        elif re.fullmatch("^[1-9]\d*\w\w$", value):
            self._ram=value.upper()
        else:
            raise ValueError("Not allowed value passed.")
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        try:
            if "," in value:
                value=value.replace(",",".")
            value=float(value)
        except ValueError:
            print("Price must be integer or float!")
        self._price=value
    def __repr__(self):
        return (f"Manufacturer: {self.manufacturer}\nModel name: {self.model_name}\nCategory: {self.category}\nScreen size: {self.screen_size}"
            f"\nScreen: {self.screen}\nCPU: {self.cpu}\nRam: {self.ram}\nStorage: {self.storage}\nOperation System: {self.operation_system}\n"
            f"Operetion system version: {self.operating_system_version}\nGPU: {self.gpu}\nWeight: {self.weight}\nPrice: {self.price}")
def laptops():
    with open("C:/Users/Admin/Desktop/laptops.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield Laptop(
                manufacturer=row["Manufacturer"],
                model_name=row["Model Name"],
                category=row["Category"],
                screen_size=row["Screen Size"],
                screen=row["Screen"],
                cpu=row["CPU"],
                ram=row["RAM"],
                storage=row["Storage"],
                gpu=row["GPU"],
                operation_system=row["Operating System"],
                weight=row["Weight"],
                price=row["Price (Euros)"]
           )


list_=[0]
i_laptops = laptops()
the_most_expencive_laptops = next(i_laptops)
for laptop in laptops():
    if the_most_expencive_laptops.price < laptop.price:
        the_most_expencive_laptops = laptop
list_[0] = the_most_expencive_laptops.price
i=0

the_most_expencive = next(i_laptops)

for i in range(5):
    for laptop in laptops():
        if the_most_expencive.price < list_[i] and the_most_expencive.price < laptop.price:
            the_most_expencive = laptop
        break

    list_.append(the_most_expencive.price)


print(list_)