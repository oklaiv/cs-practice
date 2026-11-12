from sympy import Symbol, Sum, oo, factorial
x = float(input())
y = x
i = 1
s = 0
eps = 1e-4
while abs(y) >= eps:
    s += y
    i += 1
    y = -x * x * y / (2 * i - 2) / (2 * i - 1)
print('%6.4f' % s)

i = Symbol('i')
s_s = Sum((-1)**(i - 1) * x**(2 * i - 1) / factorial(2 * i - 1), (i, 1, oo))
print(s_s.evalf(4))
