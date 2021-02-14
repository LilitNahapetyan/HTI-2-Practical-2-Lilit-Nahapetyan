print("Think of a number between 1 and 999. Input 0 once you’re ready to play: ")

def guesser():
    i = 1
    start = 1
    end = 999
    num = (start + end) // 2
    x = int(input())
    print(f"My guess number {i}: {num}")

    while i < 10:
        i += 1
        x = int(input())
        if x == 0:
            print(f"I guessed in {i - 1} steps!")
            break

        if x == 1:
            start = num + 1
            num = (start + end) // 2
            print(f"My guess number {i}: {num}")

        if x == -1:
            end = num
            num = (start + num) // 2
            print(f"My guess number {i}: {num}")

    x = int(input())
    if x == 0:
        print("I guessed in 10 steps!")
    else:
        print("I couldn’t guess in 10 steps! This means you cheated!")

guesser()
