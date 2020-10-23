# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-10-23 下午4:46
# @File     : minimumTotal.py
# @Software : PyCharm
"""
120. 三角形最小路径和
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点在这里指的是下标与上一层结点下标相同或者等于上一层结点下标+1的两个结点。
例如，给定三角形：
    [
        [2],
       [3,4],
      [6,5,7],
     [4,1,8,3]
    ]
自顶向下的最小路径和为11（即，2+3+5+1 = 11）
说明：
    如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""


class Solution(object):
    def minimum_total(self, triangle):
        """
        DP方程: f[i, j] = min(f[i+1, j], f[i+1, j+1]) + a[i, j]
        :param triangle: list[list[int]]
        :return:
        """
        dp = triangle
        for i in range(len(dp) - 2, -1, -1):
            for j in range(len(dp[i])):
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]

        # # 复用triangle
        # for i in range(len(triangle)-2, -1, -1):
        #     for j in range(len(triangle[i])):
        #         triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        # return triangle[0][0]

    def minimum_total1(self, triangle):
        # 只使用 O(n) 的额外空间
        dp = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]


if __name__ == '__main__':
    test = [[2], [3,4], [6,5,7], [4,1,8,3]]
    sol = Solution()
    # res = sol.minimum_total(test)
    res = sol.minimum_total1(test)
    print(res)