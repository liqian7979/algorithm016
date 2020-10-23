# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-10-20 上午11:31
# @File     : longestCommonSubsequence.py
# @Software : PyCharm
"""
1143. 最长公共子序列
给定两个字符串text1和text2，返回这两个字符串的最长公共子序列的长度。
一个字符串的子序列是指这样一个新的字符串: 它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以
不删除任何字符）后组成的新字符串。
例如，"ace"是"abcde"的子序列，但"aec"不是"abcde"的子序列。两个字符串的公共子序列是这两个字符串所共同拥有的子序列。
若这两个字符串没有公共子序列，则返回0.

示例1:
    输入: text1 = "abcde", text2 = "ace"
    输出: 3
    解释: 最长公共子序列是"ace"，它的长度为3.
示例2:
    输入: text1 = "abc", text2 = "abc"
    输出: 3
    解释: 最长公共子序列是"abc"，它的长度为3.
示例3:
    输入: text1 = "abc", text2 = "def"
    输出: 0
    解释: 两个字符串没有公共子序列，返回0.
"""


class Solution(object):
    def longest_common_subsequence(self, text1, text2):
        """
        DP方程:
            if s1[-1] != s2[-1]: LCS[s1, s2] = max(LCS[s1-1, s2], LCS[s1, s2-1])
            if s1[-1] == s2[-1]: LCS[s1, s2] = LCS[s1-1, s2-1] + 1
        """
        # 初始化dp矩阵 (m+1)×(n+1), 便于第一行和第一列的状态计算
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        # 根据dp方程计算状态值
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


if __name__ == '__main__':
    text1 = "abc"
    text2 = "dfe"
    sol = Solution()
    res = sol.longest_common_subsequence(text1, text2)
    print(res)
