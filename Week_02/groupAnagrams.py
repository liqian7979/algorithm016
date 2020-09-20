# -*- coding: utf-8 -*-
# @ModuleName: groupAnagrams
# @Author: Liqian
# @Time: 2020/9/20 22:52
# @Software: PyCharm
"""
字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
示例:
    输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
    输出:
    [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
    ]
说明：
    所有输入均为小写字母。
    不考虑答案输出的顺序。
"""


class Solution(object):
    def group_anagrams(self, strs):
        # 对字符串做排序后，利用字典哈希
        str_dic = dict()
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted in str_dic:
                str_dic[s_sorted].append(s)
            else:
                str_dic[s_sorted] = [s]
        # 按输出格式返回
        return [str_dic[key] for key in str_dic]


if __name__ == '__main__':
    sol = Solution()
    strs_test = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = sol.group_anagrams(strs_test)
    print(result)
