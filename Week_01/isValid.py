# -*- coding: utf-8 -*-
# @ModuleName: isValid
# @Author: Liqian
# @Time: 2020/9/13 17:58
# @Software: PyCharm
"""
有效的括号
给定一个只包括'(', ')', '{', '}', '[', ']'的字符串，判断字符串是否有效。
有效字符串需满足：
    1.左括号必须用相同类型的右括号闭合。
    2.左括号必须以正确的顺序闭合。
注意空字符串可认为是有效字符串。
示例1：
    输入："()"  输出：true
示例2：
    输入："(){}[]"  输出：true
示例3：
    输入："(]"  输出：false
示例4：
    输入："([)]"  输出：false
示例5：
    输入："{[()]}"  输出：true
"""
# 1.暴力：不断replace匹配的括号->""  O(n^2)
# 2.stack：遇到左括号则入栈，遇到右括号则进行判断是否匹配


class Solution(object):
    def is_valid(self, s):
        # if len(s) < 1:
        #     return True
        valid_dict = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for temp in s:
            if temp in valid_dict:
                # 遇到左括号入栈
                stack.append(temp)
            elif len(stack) == 0 or valid_dict[stack.pop()] != temp:
                # 遇到右括号进行判断是否匹配
                return False
        # 最后判断是否有未被匹配的括号
        return len(stack) == 0


if __name__ == '__main__':
    s_test = "][(])"
    sol = Solution()
    result = sol.is_valid(s_test)
    print(result)