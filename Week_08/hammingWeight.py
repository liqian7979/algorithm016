# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-11-19 上午9:24
# @File     : hammingWeight.py
# @Software : PyCharm
"""
191. 位1的个数
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为'1'的个数（也被称为汉明重量）。
示例1:
    输入: 00000000000000000000000000001011
    输出: 3
    解释: 输入的二进制串00000000000000000000000000001011中，共有三位为'1'。
示例2:
    输入: 00000000000000000000000010000000
    输出: 1
    解释: 输入的二进制串00000000000000000000000010000000中，共有一位为'1'。
示例3:
    输入: 11111111111111111111111111111101
    输出: 31
    解释: 输入的二进制串11111111111111111111111111111101中，共有31位为'1'。
"""


class Solution(object):
    def hamming_weight(self, n):
        """
        调用函数bin().count()
        :param n: int
        :return: count
        """
        # bin(): 返回一个整数 int 或者长整数 long int 的二进制表示.
        return bin(n).count('1')

    def hamming_weight1(self, n):
        """
        for循环计算1的个数(0-->32)
        :param n: int
        :return: count
        """
        n = bin(n)
        count = 0
        for c in n:
            if c == '1':
                count += 1
        return count

    def hamming_weight2(self, n):
        """
        利用十进制转二进制的方法。每次对2取余判断是否是1，是的话 count += 1.
        :param n: int
        :return: count
        """
        count = 0
        while n:
            res = n % 2
            if res == 1:
                count += 1
            n //= 2
        return count

    def hamming_weight3(self, n):
        """
        位运算法1: n & 1 得到n的最低位数字，再将n右移一位，循环此步骤，直到n等于0.
        :param n: int
        :return: count
        """
        count = 0
        while n:
            count += (n & 1)
            n >>= 1
        return count

    def hamming_weight4(self, n):
        """
        位运算法2: 在二进制表示中，数字n中最低位的1总是对应n-1中的0.
                  n & (n-1): 将n中最低位的1变成0，并保持其他位不变.
                  利用此方法，不断将n中最低位的1进行反转，count+=1，直到n=0.
        :param n:
        :return:
        """
        count = 0
        while n:
            count += 1
            n &= (n-1)
        return count


if __name__ == '__main__':
    n = 128
    sol = Solution()
    res = sol.hamming_weight(n)
    res1 = sol.hamming_weight1(n)
    res2 = sol.hamming_weight2(n)
    res3 = sol.hamming_weight3(n)
    res4 = sol.hamming_weight4(n)
    print(res, res1, res2, res3, res4)
