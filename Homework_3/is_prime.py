def is_prime(num):
    x, sum = 1, 0
    while x <= num:
        if num % x == 0:
            sum += 1
        x += 1
    if sum == 2:
        print("Yes")
    else:
        print("No")
num = int(input("Num: "))
is_prime(num)
