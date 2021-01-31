def is_palindrome(x):
    if len(x) == 1 or len(x) == 0:
        return True
    if x[0] == x[-1]:
        return is_palindrome(x[1:-1])
    return False

value = input("Input any string: ")
if is_palindrome(value):
    print("Yes")
else:
    print("No")
