# -*- coding: utf-8 -*-
# @ModuleName: fibonacci
# @Author: Liqian
# @Time: 2020/9/6 22:54
# @Software: PyCharm


# 0, 1, 1, 2, 3, 5, ...
# F(n) = F(n-1) + F(n-2), n > 2

# 递归解决
def fib_rec(n):
    if n < 3:
        return n - 1
    return fib(n-1) + fib(n-2)


# 非递归解决
def fib(n):
    first = 0
    second = 1
    for i in range(n-1):
        next = first + second
        first, second = second, next
    return first


if __name__ == '__main__':
    result = fib(99)
    print(result)
