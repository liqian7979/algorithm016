# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-11-16 下午3:03
# @File     : slidingPuzzle.py
# @Software : PyCharm
"""
773. 滑动谜题
在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
示例:
    输入: board = [[1, 2, 3], [4, 0, 5]]
    输出: 1
    解释: 交换 0 和 5，1步完成。
    输入: board = [[1, 2, 3], [5, 4, 0]]
    输出: -1
    解释: 没有办法完成谜板
    输入: board = [[4, 1, 2], [5, 0, 3]]
    输出: 5
    解释: 完成谜板的最少移动次数是5，一种移动路径:
          尚未移动: [[4, 1, 2], [5, 0, 3]]
          移动 1 次: [[4, 1, 2], [0, 5, 3]]
          移动 2 次: [[0, 1, 2], [4, 5, 3]]
          移动 3 次: [[1, 0, 2], [4, 5, 3]]
          移动 4 次: [[1, 2, 0], [4, 5, 3]]
          移动 5 次: [[1, 2, 3], [4, 5, 0]]
    输入: board = [[3, 2, 4], [1, 5, 0]]
    输出: 14
"""


class Solution(object):
    def sliding_puzzle(self, board):
        """BFS"""
        # 将二维数组变换为一维字符串
        # 方向变换向量  0位于不同位置时对应的可交换的位置（在一维字符串中）
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        # 存放位置移动过的字符串
        used = set()
        cnt = 0
        s = ''.join(str(c) for row in board for c in row)
        q = [s]
        # BFS starts
        while q:
            new = []
            for s in q:
                used.add(s)
                if s == '123450':
                    return cnt
                arr = [c for c in s]
                # 开始移动0
                zero_index = s.index('0')
                for move in moves[zero_index]:
                    new_arr = arr[:]
                    new_arr[zero_index], new_arr[move] = new_arr[move], new_arr[zero_index]
                    new_s = ''.join(new_arr)
                    if new_s not in used:
                        new.append(new_s)
            cnt += 1
            q = new
        return -1


if __name__ == '__main__':
    # board = [[1, 2, 3], [4, 0, 5]]
    # board = [[1, 2, 3], [5, 4, 0]]
    # board = [[4, 1, 2], [5, 0, 3]]
    board = [[3, 2, 4], [1, 5, 0]]
    sol = Solution()
    res = sol.sliding_puzzle(board)
    print(res)
