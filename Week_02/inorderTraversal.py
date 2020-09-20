# -*- coding: utf-8 -*-
# @ModuleName: inorderTraversal
# @Author: Liqian
# @Time: 2020/9/20 23:34
# @Software: PyCharm
"""
二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。
示例:
    输入: [1,null,2,3]
       1
        \
         2
        /
       3
输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.travel_path = []

    def inorder_traversal(self, root):
        # 递归实现
        if root:
            self.inorder_traversal(root.left)
            self.travel_path.append(root.val)
            self.inorder_traversal(root.right)
        return self.travel_path

    def inorder_traversal2(self, root):
        # 利用栈进行迭代
        if root is None:
            return []
        stack, output = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            output.append(root.val)
            root = root.right
        return output


if __name__ == '__main__':
    sol = Solution()
    tree_test = [1, None, 2, 3]
    node_list = [TreeNode(val) for val in tree_test]
    node_list[0].right = node_list[2]
    node_list[2].left = node_list[3]
    # result = sol.inorder_traversal(node_list[0])
    result = sol.inorder_traversal2(node_list[0])
    print(result)
