# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-11-12 上午10:29
# @File     : solveSudoku.py
# @Software : PyCharm
"""
37. 解数独
编写一个程序，通过填充空格来解决数独问题。
一个数独的解法需遵循如下规则:
    1.数字 1-9 在每一行只能出现一次。
    2.数字 1-9 在每一列只能出现一次。
    3.数字 1-9 在每一个以粗实线分割的 3×3 宫内只能出现一次。
空白格用'.'表示。
提示:
    给定的数独序列只包含数字 1-9 和字符'.'。
    你可以假设给定的数独只有唯一解。
    给定数独永远是 9×9 形式的。
"""


class Solution(object):
    def solve_sudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        :param board: List[List[str]]
        :return: None
        """
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

        # 收集需填数位置
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    # 更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3) * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        def backtrack(iter=0):
            if iter == len(empty):
                # 处理完empty代表找到了答案
                return True
            i, j = empty[iter]
            b = (i // 3) * 3 + j // 3
            # row[i] & col[j] & block[b] 为位置(i, j)可填的数字可能
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter+1):
                    return True
                # 回溯
                row[i].add(val)
                col[j].add(val)
                block[b].add(val)
            return False

        backtrack()


if __name__ == '__main__':
    board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
    sol = Solution()
    sol.solve_sudoku(board)
    print(board)
