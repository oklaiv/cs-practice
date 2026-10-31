from math import sqrt
y = int(input())
z = int(input())
if y * z == 0:
    print('деление на 0')
else:
    x = int(input())
    if 2 * x < z:
        print('корень не определен')
    else:
        if y < x:
            print('корень не определен')
        else:
            if 2 * x == z:
                f = -4 * ((y-x) ** 1/4)
            if y == x:
                f = 6 + sqrt(2 * x - 2) / y / z
            else:
                f = 6 + 6 + sqrt(2 * x - 2) / y / z - 4 * ((y-x) ** 1/4)
                print('%5.3f' %f)


