# -*- coding: utf-8 -*-
# @ModuleName: moveZeroes
# @Author: Liqian
# @Time: 2020/9/12 14:50
# @Software: PyCharm
"""
移动零
给定一个数组nums，编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序。
示例：
    输入：[0, 1, 0, 3, 12]
    输出：[1, 3, 12, 0, 0]
说明：
    1.必须在原数组上操作，不能拷贝额外的数组。
    2.尽量减少操作次数。
"""


class Solution(object):
    def move_zeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        @param nums: list(int)
        @return:
        """
        # 记录数组中0的个数
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
        # 删除数组中的所有0
        # remove()方法只会删除列表中第一个和指定值相同的元素，而且必须保证该元素是存在的，否则会引发ValueError错误
        for _ in range(zero_count):
            nums.remove(0)
        # 在数组末尾添加同等数量的0
        nums += [0] * zero_count
        print(nums)

    def move_zeroes2(self, nums):
        # 双指针方法
        j = 0  # 记录当前数组中第一个0的位置
        for i in range(len(nums)):
            if nums[i] != 0:
                # 将非零元素与零元素进行交换
                nums[j], nums[i] = nums[i], nums[j]
                # 零元素指针后移
                j += 1
        print(nums)


if __name__ == '__main__':
    nums_test = [0, 0, 1, 0, 3, 0, 12]
    sol = Solution()
    sol.move_zeroes2(nums_test)
