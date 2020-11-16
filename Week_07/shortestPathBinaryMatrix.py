# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-11-16 下午2:14
# @File     : shortestPathBinaryMatrix.py
# @Software : PyCharm
"""
1091. 二进制矩阵中的最短路径
在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。
一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：
    相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角）
    C_1 位于 (0, 0)（即，值为 grid[0][0]）
    C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
    如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0）
返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。

示例1:
    输入: [[0, 1], [1, 0]]
    输出: 2
示例2:
    输入: [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    输出: 4
"""


class Solution(object):
    def shortest_path_binary_matrix(self, grid):
        """使用BFS搜索"""
        q, n = [(0, 0, 2)], len(grid)
        if grid[0][0] or grid[-1][-1]:
            return -1
        elif n <= 2:
            return n

        # BFS starts
        for i, j, d in q:
            for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1),
                         (i, j-1), (i, j+1),
                         (i+1, j-1), (i+1, j), (i+1, j+1)]:
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    if x == y == n-1:
                        return d
                    q += [(x, y, d+1)]
                    grid[x][y] = 1
        return -1


if __name__ == '__main__':
    # grid = [[0, 1], [1, 0]]
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    sol = Solution()
    res = sol.shortest_path_binary_matrix(grid)
    print(res)
