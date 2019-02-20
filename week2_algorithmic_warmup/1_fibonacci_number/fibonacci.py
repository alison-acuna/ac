# Uses python3
def calc_fib(n):
    l = [0, 1]
    c = 1
    if (n <= 1):
        return n
    else:
        while len(l) <= n:
            c = l[-1] + l[-2]
            l.append(c)
            # print(l)
    return c

n = int(input())
print(calc_fib(n))
