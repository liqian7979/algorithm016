# -*- coding: utf-8 -*-
# @ModuleName: isAnagram
# @Author: Liqian
# @Time: 2020/9/20 22:30
# @Software: PyCharm
"""
有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
示例 1:
    输入: s = "anagram", t = "nagaram"
    输出: true
示例 2:
    输入: s = "rat", t = "car"
    输出: false
说明:
    你可以假设字符串只包含小写字母。
进阶:
    如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""


class Solution(object):
    def is_anagram(self, s, t):
        # 利用排序
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def is_anagram_hash(self, s, t):
        # 利用哈希，统计字符串中字符的频数
        c_count = dict()
        # 统计s中字符的频次
        for c in s:
            if c in c_count:
                c_count[c] += 1
            else:
                c_count[c] = 1

        # 遍历t中的字符
        for c in t:
            # 若字符c不在c_count中，则返回False
            if c not in c_count:
                return False
            # 若字符c在c_count中的频次为1，则删除c
            if c_count[c] == 1:
                del c_count[c]
            # 若字符c在c_count中频次大于1，则将频次减1
            else:
                c_count[c] -= 1
        # 若此时c_count = {}，则返回True，否则返回False
        return not c_count


if __name__ == '__main__':
    sol = Solution()
    s1 = "anagram"
    t1 = "nagaram"
    s2 = 'rat'
    t2 = 'car'
    # result = sol.is_anagram(s2, t2)
    result = sol.is_anagram_hash(s2, t2)
    print(result)
