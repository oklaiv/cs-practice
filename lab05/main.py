k = int(input())
for d in range(k-1, 0, -1):
    if k % d == 0:
        print(d)
        break