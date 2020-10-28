# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-10-28 下午4:23
# @File     : Rob.py
# @Software : PyCharm
"""
198. 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋 。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你不触动警报装置的情况下，一夜之内能够偷窃到的最高金额。

示例1:
    输入: [1, 2, 3, 1]
    输出: 4
    解释: 偷窃 1 好房屋（金额 = 1）， 然后偷窃 3 号房屋（金额 = 3）。
          偷窃到的最高金额 = 1 + 3 = 4
示例2:
    输入: [2, 7, 9, 3, 1]
    输出: 12
    解释: 偷窃 1 号房屋（金额 = 2），偷窃 3 号房屋（金额 = 9），接着偷窃 5 号房屋（金额 = 1）。
          偷窃到的最高金额 = 2 + 9 + 1 = 12
"""


class Solution(object):
    def rob(self, nums):
        """
        dp[i][0,1]: 0,...,i 能偷到的最大值 (,)
        0: 不偷第i个房间时； 1: 偷第i个房间时
        DP方程:
            dp[0][0] = 0
            dp[0][1] = nums[0]
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        """
        if len(nums) == 0:
            return 0
        # dp数组初始化
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, n):
            # 不偷第i个房间，从0到i个房间可偷的最大金额
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            # 偷第i个房间，从0到i个房间可偷的最大金额
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[n-1][0], dp[n-1][1])

    def rob2(self, nums):
        """
         简化：
            dp[i]: 0,...,i 能偷到的最大值， 第i个房子可偷或者不偷
            DP方程:
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
                dp[0] = nums[0]
                dp[1] = max(nums[0], nums[1])
        """
        if len(nums) == 0:
            return 0
        if len(nums) < 2:
            return nums[0]
        # dp数组初始化
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]

    def rob3(self, nums):
        """
        再次简化：
            不用dp数组，利用两个中间变量
        """
        # i-2状态的值
        pre = 0
        # i-1状态的值
        now = 0
        for num in nums:
            pre, now = now, max(pre + num, now)
        return now


if __name__ == '__main__':
    # nums = [1, 2, 3, 1]
    # nums = [2, 7, 9, 3, 1]
    nums = []
    sol = Solution()
    # res = sol.rob(nums)
    # res = sol.rob2(nums)
    res = sol.rob3(nums)
    print(res)
