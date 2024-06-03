def nth_harshad(n):
    harshads = []

    curr = 1

    while len(harshads) < int(n):
        total = 0
        for i in str(curr):
            total += int(i)
        if curr % total == 0:
            harshads.append(curr)

        curr += 1

    return harshads[-1]


if __name__ == "__main__":
    while True:
        n = input("nth Harshad to display: ")
        print(nth_harshad(n))
