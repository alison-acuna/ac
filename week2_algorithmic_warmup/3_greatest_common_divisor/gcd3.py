# from multiprocessing import Pool

# Uses python3
import sys
from threading import Thread

# breadcrumbs

# 2 add pool of works
# terminate at halway mark, when either finds it,

def gcd_loop(c, b):
    print("gcd loop")
    print(c)
    print(b)
    for d in range(c, 2, - 1):
        # print(d)
        if c % d == 0 and b % d == 0:
            # print("Return D")
            print(d)
            return d
            break
    # print("Return 1")
    return 1

def dcg_loop(c, b):
    print("dcg loop")
    print(c)
    print(b)
    for d in range(2, c, 1):
        # print(d)
        if c % d == 0 and b % d == 0:
            # print("Return D")
            print(d)
            return d
            break
    # print("Return 1")
    return 1

def gcd_naive(e, f):
    while e > 100:
        if e % 2 == 0:
            e = e//2
            print(e)
        if e % 5 == 0:
            e = e//5
            print(e)
    print("final number")
    print(e)

if __name__ == "__main__":
    # input = sys.stdin.read()
    # e, f = map(int, input.split())

    e, f = [int(x) for x in input().split()]
    print(gcd_naive(e, f))



# from multiprocessing import Pool
#
# def f(x):
#     return x*x
#
# if __name__ == '__main__':
#     p = Pool(5)
#     print(p.map(f, [1, 2, 3]))
