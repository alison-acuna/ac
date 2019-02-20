# Uses python3
import sys

# I actually think this one might be done

def fibonacci_sum_naive(n):
    l = [0, 1]
    test_l = [0, 1]
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n-1):
        # previous, current = current, (previous + current) % 10
        current = (l[-1] + l[-2]) % 10
        l.append(current)
        # print(current)
        # sum += current
        # sum_One = sum % 10
        # print(sum_One)
    k = sum(l) % 10
    return k

if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(fibonacci_sum_naive(n))

# 15
# 6

# 100
# 5

# 832564823476

# ^ Failed at bc time limit exceeded

# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#     sum      = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current
#
#     return sum % 10
#
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     print(fibonacci_sum_naive(n))
