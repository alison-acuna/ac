# Uses python3
import sys

def gcd_loop(c, b):
    print("5")
    for d in range(c, 2, -1):
        print("7")
        if c % d == 0 and b % d == 0:
            return d
            break
    return 1


if __name__ == "__main__":
    c, b = [int(x) for x in input().split()]
    print(gcd_loop(c, b))
