def is_prime(num):
    if num < 2:
        return False
    else:
        x, sum = 2, 0
        while x <= num // 2:
            if num % x == 0:
                return False
            x += 1
        return True

def goldbach(n):
    i = 2
    while i < n:
        if is_prime(i) and is_prime(n - i):
            return i , n - i
        i += 1

num = int(input("Enter even number greater than 2: "))
if 2 < num and num % 2 == 0:
    print(goldbach(num))
else:
    print("This number is Odd or Is greater than 2")
