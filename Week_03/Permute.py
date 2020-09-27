# -*- coding: utf-8 -*-
# @ModuleName: Permute
# @Author: Liqian
# @Time: 2020/9/27 22:34
# @Software: PyCharm
"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:
    输入: [1,2,3]
    输出:
        [
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,1,2],
        [3,2,1]
        ]
"""
# 这个问题可以看作有n个排列成一行的空格，从左往右依此填入给定的n个数，每个数只能使用一次


class Solution(object):
    def permute(self, nums):
        def back(first=0):
            # 空格已填满
            if first == n:
                result.append(nums[:])
                return None
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                back(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        result = []
        back(first=0)
        return result


if __name__ == '__main__':
    nums_test = [1, 2, 3]
    sol = Solution()
    res = sol.permute(nums_test)
    print(res)
