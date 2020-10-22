# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-10-22 下午3:24
# @File     : uniquePathsWithObstacles.py
# @Software : PyCharm
"""
63. 不同路径II
一个机器人位于一个 m×n 网格的左上角。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
说明: m 和 n 的值均不超过100.
（m为列数，n为行数）

示例1:
    输入:
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    输出: 2
    解释:
        3×3 网格的正中间有一个障碍物。
        从左上角到右下角一共有 2 条不同的路径:
        1. 向右 -> 向右 -> 向下 -> 向下
        2. 向下 -> 向下 -> 向右 -> 向右
"""


class Solution(object):
    def unique_paths_with_obstacles(self, obstacle_grid):
        # 动态规划
        # 初始位置有障碍时，路径数为0
        if obstacle_grid[0][0] == 1:
            return 0
        # 获取行数
        n = len(obstacle_grid)
        # 获取列数
        m = len(obstacle_grid[0])
        print(n, m)
        # 初始化dp矩阵
        dp = [[0] * m for _ in range(n)]
        # 根据是否有障碍初始化边界位置
        # 若在第一行和第一列遇到障碍，则从此位置之后都为0
        for i in range(m):
            if obstacle_grid[0][i] == 0:
                dp[0][i] = 1
            else:
                break
        for j in range(n):
            if obstacle_grid[j][0] == 0:
                dp[j][0] = 1
            else:
                break
        print(dp)
        for r in range(1, n):
            for c in range(1, m):
                # 判断当前位置是否有障碍
                if obstacle_grid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]


if __name__ == '__main__':
    test = [[0, 0], [1, 1], [0, 0]]
    sol = Solution()
    res = sol.unique_paths_with_obstacles(test)
    print(res)