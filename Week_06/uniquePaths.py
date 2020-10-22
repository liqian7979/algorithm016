# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-10-22 上午10:55
# @File     : uniquePaths.py
# @Software : PyCharm
"""
62. 不同路径
一个机器人位于一个 m×n 网格的左上角。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角。
问总共有多少条不同的路径？
（m为列数，n为行数）

示例1:
    输入: m = 3, n = 2
    输出: 3
    解释:
        从左上角开始，总共有3条路径可以到达右下角。
        1. 向右 -> 向右 -> 向下
        2. 向右 -> 向下 -> 向右
        3. 向下 -> 向右 -> 向右

示例2:
    输入: m = 7, n = 3
    输出: 28
"""


class Solution(object):
    def unique_paths(self, m, n):
        """
           动态规划
           第一行和第一列位于边界，都只有一条路径可以到达
           故: dp[0][j] = 1, dp[i][0] = 1
           其余位置为: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        """
        # 初始化DP矩阵
        dp = [[1] * m] + [[1] + [0] * (m-1) for _ in range(n-1)]
        # print(dp)
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    def unique_paths1(self, m, n):
        """
        使用一维dp矩阵，减少内存空间使用
        """
        # 初始化
        dp = [1 for _ in range(m)]
        for i in range(1, n):
            for j in range(1, m):
                dp[j] += dp[j-1]
        return dp[m-1]


if __name__ == '__main__':
    sol = Solution()
    # res = sol.unique_paths(7, 3)
    res = sol.unique_paths1(7, 3)
    print(res)
