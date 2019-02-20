# Uses python3
import sys

def gcd_naive(e, f):
    # current_gcd = 2
    a = max(e, f)
    # print("a")
    # print(a)
    b = min(e, f)
    # print(b)
    # print("b")
    c = a%b
    # print("c")
    # print(c)
    # subing c for a speeds things up
    if c == 0:
        # print("Return B")
        return b
    else:
        for d in range(c, 2, - 1):
            # print(d)
            if c % d == 0 and b % d == 0:
                # print("Return D")
                return d
                break
        # print("Return 1")
        return 1

if __name__ == "__main__":
    # input = sys.stdin.read()
    # e, f = map(int, input.split())
    e, f = [int(x) for x in input().split()]
    print(gcd_naive(e, f))
