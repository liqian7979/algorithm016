# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-10-28 下午5:44
# @File     : RobII.py
# @Software : PyCharm
"""
213. 打家劫舍II
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈，
这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻
的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

示例 1：
    输入：nums = [2,3,2]
    输出：3
    解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2：
    输入：nums = [1,2,3,1]
    输出：4
    解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
         偷窃到的最高金额 = 1 + 3 = 4 。
示例 3：
    输入：nums = [0]
    输出：0
"""


class Solution(object):
    def rob(self, nums):
        """
        分两部分：
            1.不偷第一个房间nums[1:]，利用打家劫舍问题的方法得到一个最大金额res1;
            2.不偷最后一个房间nums[:n-1]，利用打家劫舍问题的方法得到一个最大金额res2;
            3.最后取两者的最大值 max(res1, res2)
        """
        def my_rob(nums):
            pre, cur = 0, 0
            for num in nums:
                pre, cur = cur, max(cur, pre + num)
            return cur
        if len(nums) == 1:
            return nums[0]
        return max(my_rob(nums[1:]), my_rob(nums[:-1]))


if __name__ == '__main__':
    # nums = [2, 3, 2]
    # nums = [1, 2, 3, 1]
    # nums = [0]
    nums = []
    sol = Solution()
    res = sol.rob(nums)
    print(res)
