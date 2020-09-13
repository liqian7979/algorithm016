# -*- coding: utf-8 -*-
# @ModuleName: climbStairs
# @Author: Liqian
# @Time: 2020/9/13 12:31
# @Software: PyCharm
"""
爬楼梯
假设你正在爬楼梯，需要n阶你才能到达楼顶。
每次你可以爬1或2个台阶，你有多少种不同的方法可以爬到楼顶呢？
注意：给定n是一个正整数。
示例1：
    输入：2
    输出：2
    解释：有两种方法可以爬到楼顶。
    1. 1 + 1
    2. 2
示例2：
    输入：3
    输出：3
    解释：有三种方法可以爬到楼顶。
    1. 1 + 1 + 1
    2. 1 + 2
    3. 2 + 1
"""
# f(1) = 1, f(2) = 2
# f(n) = f(n-1) + f(n-2)


class Solution(object):
    """
    爬到n阶的方法数为爬到第n-1阶和爬到第n-2阶的方法数之和
    当爬到第n-1阶时，只要一步上1阶就到达n阶
    当爬到第n-2阶时，只要一步上2阶就到达n阶
    f(1) = 1, f(2) = 2
    f(n) = f(n-1) + f(n-2), n>2
    """
    def climb_stairs(self, n):
        # 递归实现
        if n < 3:
            return n
        return self.climb_stairs(n - 1) + self.climb_stairs(n - 2)

    def climb_stairs2(self, n):
        # 非递归实现，迭代
        # # 爬 1 阶台阶的方法
        # first = 1
        # # 爬 2 阶台阶的方法
        # second = 2
        # while n > 1:
        #     first, second = second, first + second
        #     n -= 1
        # return first

        if n < 3:
            return n
        fir, sec = 1, 2
        for i in range(3, n+1):
            fir, sec = sec, fir + sec
        return sec


if __name__ == '__main__':
    n_test = 5
    sol = Solution()
    result = sol.climb_stairs2(n_test)
    print(result)