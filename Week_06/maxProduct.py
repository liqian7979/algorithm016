# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-10-27 下午2:19
# @File     : maxProduct.py
# @Software : PyCharm
"""
152. 乘积最大子数组
给你一个整数数组nums，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
示例1:
    输入: [2, 3, -2, 4]
    输出: 6
    解释: 子数组 [2, 3] 有最大乘积 6.
示例2:
    输入: [-2, 0, -1]
    输出: 0
    解释: 结果不能为2，因为 [-2, -2] 不是子数组
"""

"""
思考:
    1.DP问题:
        a.分治（子问题）: 需考虑负负得正的情况，保留当前位置的最大值和最小值
                        max_product[i] = Max(max_product[i-1] * a[i], min_product[i-1] * a[i], a[i])
                        min_product[i] = Min(max_product[i-1] * a[i], min_product[i-1] * a[i], a[i])
        b.状态数组定义 max_dp, min_dp
        c.DP方程 
            max_dp[i] = Max(max_dp[i-1] * a[i], min_dp[i-1] * a[i], a[i])
            min_dp[i] = Max(max_dp[i-1] * a[i], min_dp[i-1] * a[i], a[i])
"""


class Solution(object):
    def max_product(self, nums):
        # max_dp, min_dp = nums, nums  错误写法，其中一个改变则都改变了
        max_dp = [0] * len(nums)
        min_dp = [0] * len(nums)
        max_dp[0] = min_dp[0] = nums[0]
        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
            min_dp[i] = min(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
        return max(max_dp)

    def max_product2(self, nums):
        # 利用两个变量维护i-1时刻的状态，res维护最大乘积
        max_dp = min_dp = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_dp, min_dp = min_dp, max_dp
            max_dp = max(max_dp * nums[i], nums[i])
            min_dp = min(min_dp * nums[i], nums[i])
            res = max(max_dp, res)
        return res


if __name__ == '__main__':
    # nums = [2, 3, -2, 4]
    # nums = [-2, 0, -1]
    # nums = [-3, -1, -1]
    nums = [-4, -3, -2]
    sol = Solution()
    # res = sol.max_product(nums)
    res = sol.max_product2(nums)
    print(res)
