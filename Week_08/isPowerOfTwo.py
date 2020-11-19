# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-11-19 下午4:46
# @File     : isPowerOfTwo.py
# @Software : PyCharm
"""
231. 2的幂
给定一个整数，编写一个函数来判断它是否是2的幂次方。
示例1:
    输入: 1
    输出: true
    解释: 2^0 = 1
示例2:
    输入: 16
    输出: true
    解释: 2^4 = 16
示例1:
    输入: 218
    输出: false
"""


class Solution(object):
    def is_power_of_two(self, n):
        """2的幂次方整数的二进制表示形式里面有且仅有一位二进制位是1"""
        return n != 0 and (n & (n-1)) == 0


if __name__ == '__main__':
    n = 218
    sol = Solution()
    res = sol.is_power_of_two(n)
    print(res)