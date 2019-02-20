# Uses python3
import sys

# Compute the remainder of the n-th Fibonacci divided by m.
# I don't understand the association of the patterns well enough yet

def get_fibonacci_huge_naive(n, m):
    l = [0, 1]
    if n <= 1:
        return n

    c  = 1

    for _ in range(n - 1):
        c = l[-1] + l[-2]
        l.append(c)

    return l[-1] % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))


# 115
# 1000
# 885
#
# 2816213588
# 239
# 151

# https://www.youtube.com/watch?v=Nu-lW-Ifyec

# 1) The Fibonacci sequence mod m is periodic, with period less than m^2;
#
# 2) Each Pisano period starts with 01 and then does not have 01 repeated (you can rely on the fact that when you see next 01, it means the next period has started.)
#
# 3) The fact from the instructions: Fn mod m = Fr mod m, where r = n % pisanoPeriodLength; (Ex.: F2015 mod 3 = F7 mod 3 = 1)
#
# So the algorithm:
#
# Step 1: Find pisanoPeriodLength by iterating from 0 to m^2-1 and calculating Fi % m without calculating the Fi itself ( F(i+2) mod m = F(i) mod m + F(i+1) mod m );
#
# As soon as you get F(i) mod m = 0 and F(i+1) mod m = 1, exit the loop (you've started the new Pisano Period).
#
# Step 2: You know the pisanoPeriodLength now so you can use the fact 3) from above to calculate Fn mod m.


# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % m
#
# if __name__ == '__main__':
#     input = sys.stdin.read();
#     n, m = map(int, input.split())
#     print(get_fibonacci_huge_naive(n, m))
