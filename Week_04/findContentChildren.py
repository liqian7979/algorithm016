# -*- coding: utf-8 -*-
# @ModuleName: findContentChildren
# @Author: Liqian
# @Time: 2020/10/11 21:01
# @Software: PyCharm
"""
分发饼干
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。
如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
注意：
    你可以假设胃口值为正。
    一个小朋友最多只能拥有一块饼干。
示例 1:
    输入: [1,2,3], [1,1]
    输出: 1
    解释:
        你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
        虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
        所以你应该输出1。
示例 2:
    输入: [1,2], [1,2,3]
    输出: 2
    解释:
        你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
        你拥有的饼干数量和尺寸都足以让所有孩子满足。
        所以你应该输出2.
"""


class Solution(object):
    def find_content_children(self, g, s):
        # 贪心算法
        # 用于记录满足的小孩个数
        res = 0
        # 分别对小孩胃口和饼干尺寸进行从小到大的排序
        g.sort()
        s.sort()

        # 小孩数目
        g_len = len(g)
        # 饼干数目
        s_len = len(s)

        # 初始化指针位于起始位置
        i = 0
        j = 0
        while i < g_len and j < s_len:
            if g[i] <= s[j]:
                # 饼干尺寸满足小孩胃口， res + 1
                res += 1
                # 小孩指针和饼干指针同时后移一位
                i += 1
                j += 1
            else:
                # 饼干尺寸不满足小孩胃口，饼干指针后移一位，继续比较
                j += 1

        return res


if __name__ == '__main__':
    g_test = [1, 2]
    s_test = [1, 2, 3]
    sol = Solution()
    result = sol.find_content_children(g_test, s_test)
    print(result)
