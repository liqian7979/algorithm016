# -*- coding: utf-8 -*-
# @ModuleName: BullsAndCows
# @Author: Liqian
# @Time: 2020/9/12 22:57
# @Software: PyCharm
"""
猜数字游戏
你在和朋友一起玩猜数字游戏，该游戏规则如下：
    1.你写出一个秘密数字，并请朋友猜这个数字是多少。
    2.朋友每猜测一次，你就会给他一个提示，告诉他的猜测数字中有多少位属于数字和确切位置都猜对了（称为"Bulls"，公牛），
    有多少位属于数字猜对了但是位置不对（称为"Cows"，奶牛）。
    3.朋友根据提示继续猜，直到猜出秘密数字。
请写出一个根据秘密数字和朋友的猜测数返回提示的函数，返回字符串的格式为xAyB，x和y都是数字，A表示公牛，用B表示奶牛。
    . xA表示有x位数字出现在秘密数字中，且位置都与秘密数字一致。
    . yB表示有y位数字出现在秘密数字中，且位置与秘密数字不一致。
请注意秘密数字和朋友的猜测数都可能含有重复数字，每位数字只能统计一次。
示例1：
    输入：secret = "1807", guess = "7810"
    输出："1A3B"
    解释：1公牛和3奶牛。公牛是8，奶牛是0,1和7。
示例2：
    输入：secret = "1123", guess = "0111"
    输出："1A1B"
    解释：朋友猜测数中的第一个1是公牛，第二个或第三个1可被视为奶牛。
说明：你可以假设秘密数字和朋友的猜测数都只包含数字，并且它们的长度永远相等。
"""


class Solution(object):
    def get_hint(self, secret: str, guess: str):
        # 公牛计数
        A = 0
        # 奶牛计数
        B = 0
        sec_b, gue_b = [], []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                sec_b.append(secret[i])
                gue_b.append(guess[i])
        for num in set(gue_b):
            sec_num = sec_b.count(num)
            gue_num = gue_b.count(num)
            if num in sec_b:
                B += min(sec_num, gue_num)

        print('{}A{}B'.format(A, B))


if __name__ == '__main__':
    s_test = "1123"
    g_test = "0111"
    sol = Solution()
    sol.get_hint(s_test, g_test)
