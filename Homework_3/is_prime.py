def is_prime(num):
    if num < 2:
        print("No")
    else:
        x, sum = 2, 0
        while x <= num - 1:
            if num % x == 0:
                print("No")
                break
            x += 1
        else:
            print("Yes")
num = int(input("Num: "))
is_prime(num)
