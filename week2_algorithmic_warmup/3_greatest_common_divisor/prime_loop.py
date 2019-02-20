# Uses python3
import sys

def prime_loop(c, b):
    a = max(e, f)
    print(a)
    b = min(e, f)
    print(b)
    c = a%b
    print(c)
    g = 157

    for d in range(2, c):
        print(d)
        if c % d == 0:
            # if b%c == 0:
            #     return b/c
            # else:
            #     return d
            return d
    return 0
    # commit first
    # put some logic - if 0 run the other loop, if greater than 0, set current_gcd to result
    # attempt in one section of code

if __name__ == "__main__":
    e, f = [int(x) for x in input().split()]
    print(prime_loop(e, f))
