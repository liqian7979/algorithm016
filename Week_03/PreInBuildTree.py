# -*- coding: utf-8 -*-
# @ModuleName: PreInBuildTree
# @Author: Liqian
# @Time: 2020/9/27 17:18
# @Software: PyCharm
"""
从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。
注意:
    你可以假设树中没有重复的元素。
例如，给出
    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
        3
       / \
      9  20
        /  \
       15   7
"""
# 解决方法类似 从中序与后序遍历序列构造二叉树


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def build_tree(self, preorder, inorder):
        # 1. 根据前序遍历的第一个节点为根节点的特点，可依次获取各个子树的根节点
        # 2. 根据中序遍历的 左-根-右 的序列，可依据根节点划分该节点的左右子树节点集合
        # 3. 递归构造
        def recursion_tree(in_start, in_end):
            # 参数为在中序遍历中的左右区间位置
            if in_start > in_end:
                # 当区间为空时，没有节点可用于构造二叉树，结束
                return None
            # 获取根节点，前序遍历的第一个节点
            val = preorder.pop(0)
            root = TreeNode(val)
            # 获取根节点在中序遍历中的位置
            index = root_map[val]
            # 递归构造子树
            # 此时因前序遍历的第一个节点为根节点，以及前序遍历 根-左-右 的顺序，故应先构造左子树，再构造右子树
            # 构造左子树
            root.left = recursion_tree(in_start, index - 1)
            # 构造右子树
            root.right = recursion_tree(index + 1, in_end)
            return root

        # 创建中序遍历中{节点: 位置}键值对哈希表
        root_map = {val: i for i, val in enumerate(inorder)}
        return recursion_tree(0, len(inorder) - 1)


if __name__ == '__main__':
    pre_order = [3, 9, 20, 15, 7]
    in_order = [9, 3, 15, 20, 7]
    sol = Solution()
    result = sol.build_tree(pre_order, in_order)
    print(result)
