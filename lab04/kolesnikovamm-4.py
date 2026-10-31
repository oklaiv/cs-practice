n = int(input('n = '))

k = 2
flag = n > 1

while k * k <= n and flag:
    flag = n % k != 0
    k = k + 1

print(flag)