# Uses python3
import sys

# Once I figure out gcp, LCM should work

def lcm_naive(a, b):
    current_gcd = 1
    c = a%b
    if c == 0:
        current_gcd = min(a, b)
    else:
        for d in range(min(c, b), 2, - 1):
            if c % d == 0 and b % d == 0:
                current_gcd = d
                break


    e = a/current_gcd
    f = int(e*b)

    return f

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

# 28851538
# 1183019
# 17657
#
# 10
# 10
# 10
#
# 2000000000
# 1
# 1
#
# 226553150
# 1023473145
# 5





# Uses python3
# import sys
#
# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l
#
#     return a*b
#
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     a, b = map(int, input.split())
#     print(lcm_naive(a, b))
