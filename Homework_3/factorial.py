def my_factorial(n):
    if n < 0:
        print("The factorials of negative integers have no defined meaning.")
    #0! = 1
    elif n >= 0:
        fact = 1
        while n > 0:
            fact *= n
            n -= 1
        return fact
num = int(input("Enter number: "))
print(my_factorial(num))
