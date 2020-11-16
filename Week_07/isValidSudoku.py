# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-11-11 下午4:52
# @File     : isValidSudoku.py
# @Software : PyCharm
"""
36. 有效的数独
判断一个9×9的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
    1. 数字 1-9 在每一行只能出现一次。
    2. 数字 1-9 在每一列只能出现一次。
    3. 数字 1-9 在每一个以粗实线分割的 3×3 宫内只能出现一次。
数独部分空格内已填入了数字，空白格用'.'表示。

示例1:
    输入:
        [
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
    输出: true

示例2:
    输入:
        [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
    输出: false
    解释: 除了第一行的第一个数字从5改为8以外，空格内其他数字均与示例1相同。
         但由于位于左上角的3×3宫内有两个8存在，因此这个数独是无效的。

说明:
    一个有效的数独（部分已被填充）不一定是可解的。
    只需要根据以上规则，验证已经填入的数字是否有效即可。
    给定数独序列只包含数字 1-9 和字符 '.' 。
    给定数独永远是 9x9 形式的。
"""


class Solution(object):
    def is_valid_sudoku(self, board):
        # init
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        # 遍历数独，进行判别
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True


if __name__ == '__main__':
    # board = [
    #         ["5","3",".",".","7",".",".",".","."],
    #         ["6",".",".","1","9","5",".",".","."],
    #         [".","9","8",".",".",".",".","6","."],
    #         ["8",".",".",".","6",".",".",".","3"],
    #         ["4",".",".","8",".","3",".",".","1"],
    #         ["7",".",".",".","2",".",".",".","6"],
    #         [".","6",".",".",".",".","2","8","."],
    #         [".",".",".","4","1","9",".",".","5"],
    #         [".",".",".",".","8",".",".","7","9"]
    #     ]

    board = [
            ["8","3",".",".","7",".",".",".","."],
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
    res = sol.is_valid_sudoku(board)
    print(res)