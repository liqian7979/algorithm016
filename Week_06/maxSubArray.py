# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-10-26 上午11:32
# @File     : maxSubArray.py
# @Software : PyCharm
"""
53. 最大子序列和
给定一个整数数组nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
    输入: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    输出: 6
    解释: 连续子数组 [4, -1, 2, 1] 的和最大，为6.
进阶:
    如果你已经实现复杂度为O(n)的解法，尝试使用更为精妙的分治法求解。
"""
"""
思路
# 1. 暴力求解: O(n^2)   （可优化: 以正数开头，以正数结尾）
# 2. DP:
        a. 分治（子问题）  max_sum(i) = Max(max_sum(i-1), 0) + a[i]
        b. 状态数组定义: f[i] (包含第i个元素并以其结尾的最大子序列和）
        c. DP方程: f[i] = Max(f[i-1], 0) + a[i]
"""


class Solution(object):
    def max_sub_array(self, nums):
        """
            1. dp问题. 公式为: dp[i] = max(nums[i], nums[i] + dp[i-1])
            2. 最大子序列和 = 当前元素自身最大，或者 包含之前后 最大
        """
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i-1]) +  nums[i]
            # 也可直接复用nums
            # nums[i] = max(0, nums[i-1]) + nums[i]

        return max(dp)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    res = sol.max_sub_array(nums)
    print(res)
