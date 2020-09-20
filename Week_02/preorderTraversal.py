# -*- coding: utf-8 -*-
# @ModuleName: preorderTraversal
# @Author: Liqian
# @Time: 2020/9/20 23:05
# @Software: PyCharm
"""
二叉树的前序遍历
给定一个二叉树，返回它的 前序 遍历。
示例:
    输入: [1,null,2,3]
       1
        \
         2
        /
       3
    输出: [1,2,3]
    进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""


class TreeNode(object):
    """Definition for a binary tree node"""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorder_traversal(self, root):
        # 利用栈迭代
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                stack += [root.right, root.left]
        return output


if __name__ == '__main__':
    sol = Solution()
    tree_test = [1, None, 2, 3]
    node_list = [TreeNode(val) for val in tree_test]
    node_list[0].right = node_list[2]
    node_list[2].left = node_list[3]

    result = sol.preorder_traversal(node_list[0])
    print(result)
