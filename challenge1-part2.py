with open("input.txt") as f:
    list = [int(l) for l in f.readlines()]
count = 0

windows = [a + b + c for a, b, c in zip(list, list[1:], list[2:])]
for (a, b) in zip(windows, windows[1:]):
    if b > a:
        count += 1
        print (f"{a} (increased).")
    elif a == b :
        print (f"{a} is equal to {b}.")
    elif a > b:
        print (f"{a} (decreased).")
print(f"The number of times a depth measurement increased was {count}.")


