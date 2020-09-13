# -*- coding: utf-8 -*-
# @ModuleName: twoSum
# @Author: Liqian
# @Time: 2020/9/9 20:31
# @Software: PyCharm


"""
给定一个整数数组nums和一个目标值target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
"""


def two_sum(nums, target):
    # 暴力求解 时间复杂度O(n²)
    # for i, num1 in enumerate(nums[:-1]):
    #     for j in range(i+1, len(nums)):
    #         if num1 + nums[j] == target:
    #             return [i, j]

    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_hash(nums, target):
    # 通过字典模拟哈希查询  时间复杂度O(n)
    hashmap = {}
    for index, num in enumerate(nums):
        hashmap[num] = index
    for i, num1 in enumerate(nums):
        j = hashmap.get(target - num1)
        if j is not None and i != j:
            return [i, j]


if __name__ == '__main__':
    nums_test = [2, 7, 11, 15]
    target_test = 26
    # result = two_sum(nums_test, target_test)
    result = two_sum_hash(nums_test, target_test)
    print(result)
