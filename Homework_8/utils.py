import sys

def generator_odd(start,stop):
    while start < stop:
        if start % 2 == 0:
            start += 1
        else:
            i = start
            while i != 0:
                i //= 10
                if i < 10 and i % 2 == 1:
                    yield start
                if i % 2 == 0:
                    break
            start += 2


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[0] == "utils.py":
        try:
            start = int(sys.argv[1])
            stop = int(sys.argv[2])
            for i in generator_odd(start,stop):
                print(i, end=" ")
        except ValueError:
            print("Oops! ValueError ocured")
    else:
        print("Please input 2 positive integer")
