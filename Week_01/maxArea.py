# -*- coding: utf-8 -*-
# @ModuleName: maxArea
# @Author: Liqian
# @Time: 2020/9/13 10:21
# @Software: PyCharm
"""
盛最多水的容器
给你n个非负整数 a1, a2, ..., an, 每个数代表坐标中的一个点(i, ai)。
在坐标内画n条垂直线，垂直线i的两个端点分别为(i, ai)和(i, O)。
找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且n的值至少为2。
示例：
    输入：[1, 8, 6, 2, 5, 4, 8, 3, 7]
    输出：49
"""


class Solution(object):
    def max_area(self, height):
        area = 0
        # 枚举 时间复杂度O(n²)
        # for i in range(len(height) - 1):
        #     for j in range(i+1, len(height)):
        #         w = j - i
        #         h = min(height[i], height[j])
        #         area = max(area, w * h)
        # return area

        # 左右夹逼办法 左右指针i，j,向中间收敛, 时间复杂度O(n)
        # i, j = 0, len(height) - 1
        # while i < len(height):
        #     h = min(height[i], height[j])
        #     w = j - i
        #     area = max(area, w*h)
        #     if height[i] <= height[j]:
        #         i += 1
        #     elif j > i:
        #         j -= 1
        # return area

        i, j = 0, len(height) - 1
        while i < j:
            area_temp = (j - i) * min(height[i], height[j])
            area = max(area, area_temp)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return area


if __name__ == '__main__':
    h_test = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    sol = Solution()
    res = sol.max_area(h_test)
    print(res)
