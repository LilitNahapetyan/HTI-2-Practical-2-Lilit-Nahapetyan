def sum_of_digit(num):
    sum = 0
    while num > 0 or sum > 9:
        if num == 0:
            num = sum
            sum = 0
        else:
            sum += num % 10
            num //= 10
    return sum

num = int(input("Number: "))
print(sum_of_digit(num))