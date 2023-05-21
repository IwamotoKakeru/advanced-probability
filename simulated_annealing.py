import random
import math


def f(x, y, z, w):
    return (x ** 2 + y ** 2 + z ** 2 + w ** 2)


T = 10

x = 1
y = 1
z = 1
w = 1

for m in range(50):
    for n in range(50):
        coin = random.randint(1, 4)
        if coin == 1:
            D = f(x, y, z, w) - f(1-x, y, z, w)
            if D > 0:
                x = 1-x
            else:
                p = random.random()
                if p <= math.exp(D/T):
                    x = 1-x
        elif coin == 2:
            D = f(x, y, z, w) - f(x, 1-y, z, w)
            if D > 0:
                y = 1-y
            else:
                p = random.random()
                if p <= math.exp(D/T):
                    y = 1-y
        elif coin == 3:
            D = f(x, y, z, w) - f(x, y, 1-z, w)
            if D > 0:
                z = 1-z
            else:
                p = random.random()
                if p <= math.exp(D/T):
                    z = 1-z
        else:
            D = f(x, y, z, w) - f(x, y, z, 1-w)
            if D > 0:
                w = 1-w
            else:
                p = random.random()
                if p <= math.exp(D/T):
                    w = 1-w
    print('m=', m+1, ' : ', x, y, z, w, ' : ', f(x, y, z, w), ' : T=', T)
    T *= 0.9
