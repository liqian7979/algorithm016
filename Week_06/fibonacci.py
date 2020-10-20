# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-10-20 下午4:55
# @File     : fibonacci.py
# @Software : PyCharm


# 递归
def fib_rec(n):
    if n < 2:
        return n
    return fib_rec(n-1) + fib_rec(n-2)


# 递归 + 记忆化搜索
# memo = [0] * (n+1)
def fib_rec_search(n, memo):
    if n < 2:
        return n
    if memo[n] == 0:
        memo[n] = fib_rec_search(n-1, memo) + fib_rec_search(n-2, memo)
    return memo[n]


# for循环  自底向上
def fib_for(n):
    a = [0 for _ in range(n+1)]
    a[0], a[1] = 0, 1
    for i in range(2, n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n]


if __name__ == '__main__':
    n = 6
    # res = fib_rec(n)

    # memo = [0] * (n+1)
    # res = fib_rec_search(n, memo)

    res = fib_for(n)
    print(res)
