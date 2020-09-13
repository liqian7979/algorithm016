# -*- coding: utf-8 -*-
# @ModuleName: plusOne
# @Author: Liqian
# @Time: 2020/9/8 22:02
# @Software: PyCharm

"""
加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一；
最高位数字存放在数组的首位，数组中每个元素只存储单个数字；
你可以假设除了整数0之外，这个整数不会以零开头；
示例：输入：[1, 2, 3]  输出：[1, 2, 4]
"""


def plus_one(digits):
    num = 0
    length = len(digits)
    # 将数组中的单个数字转化为整数，进行加一运算后再转换为数组
    for i in range(length):
        num += digits[i] * 10 ** (length-1-i)
    num_plus_one = num + 1
    result = [int(j) for j in str(num_plus_one)]
    return result


def plus_one2(digits):
    # 数组遍历，末位加一，判断是否有进位
    for i in range(len(digits)-1, -1, -1):
        num = digits[i] + 1
        # 无进位，当前位直接加1，返回
        if num % 10 != 0:
            digits[i] += 1
            return digits
        # 有进位，当前位为0，向前一位加1
        digits[i] = 0
    # 首位也有进位  [9, 9, 9]的情况，首位添加一位，值位1
    return [1, ] + digits


if __name__ == '__main__':
    digits_test = [9, 9, 9, 9]
    # res = plus_one(digits_test)
    # print(res)

    res2 = plus_one2(digits_test)
    print(res2)
