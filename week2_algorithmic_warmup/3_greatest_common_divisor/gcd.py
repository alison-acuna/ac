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

def gcd_naive(e, f):
    print("12")
    a = max(e, f)
    b = min(e, f)
    c = a%b

    i = 0

    placeholder_gcd = 1

    if c == 0:
        current_gcd = b
    elif b%6==0 and c%6==0:
        print("24")
        while b%6==0 and c%6==0:
            b = b//6
            c = c//6
            i = i+1
        j = 6*i
        current_gcd = gcd_loop(c, b)*j
    elif b%5==0 and c%5==0:
        while b%5==0 and c%5==0:
            b = b//5
            c = c//5
            i = i+1
        j = 5*i
        current_gcd = gcd_loop(c, b)*j
    elif b%3==0 and c%3==0:
        print("39")
        while b%3==0 and c%3==0:
            b = b//3
            c = c//3
            i = i+1
        j = 3*i
        current_gcd = gcd_loop(c, b)*j
    elif b%2==0 and c%2==0:
        while b%2==0 and c%2==0:
            print("Loop 48")
            b = b//2
            print("b")
            print(b)
            c = c//2
            print("c")
            print(c)
            i = i+1
        first_gcd = gcd_loop(c, b)
        j = 2*i
        current_gcd = int(first_gcd)*j
    elif b%2==0 and c%2==1:
        b = b//2
        current_gcd = gcd_loop(c, b)
    elif b%2==1 and c%2==0:
        c = c//2
        current_gcd = gcd_loop(c, b)
    else:
        u = max(b, c)
        v = min(b, c)
        x = (u-v)//2
        current_gcd = gcd_loop(x, v)

    return current_gcd

if __name__ == "__main__":
    e, f = [int(x) for x in input().split()]
    print(gcd_naive(e, f))
