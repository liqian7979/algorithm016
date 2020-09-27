# -*- coding: utf-8 -*-
# @ModuleName: InPostBuildTree
# @Author: Liqian
# @Time: 2020/9/27 17:14
# @Software: PyCharm
"""
从中序与后序遍历序列构造二叉树
根据一棵树的中序遍历与后序遍历构造二叉树。
注意:
    你可以假设树中没有重复的元素。
例如，给出
    中序遍历 inorder = [9,3,15,20,7]
    后序遍历 postorder = [9,15,7,20,3]
    返回如下的二叉树：
        3
       / \
      9  20
        /  \
       15   7
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def build_tree(self, inorder, postorder):
        # 1. 根据后序遍历的最后一个节点为根节点的特点，可依次获取各个子树的根节点
        # 2. 根据中序遍历的 左-根-右 的序列，可依据根节点划分该节点的左右子树节点集合
        # 3. 递归构造
        def recursion_tree(in_start, in_end):
            # 参数为中序遍历的左右区间位置
            if in_start > in_end:
                # 区间为空时，没有节点可用于构造二叉树，结束
                return None

            # 获取子树的根节点
            val = postorder.pop()
            root = TreeNode(val)

            # 获取根节点在中序遍历中的位置
            # ind = inorder.index(val)
            # 利用构建哈希表查询更快
            ind = root_map[val]

            # 根据后序遍历的 左-右-根 的顺序特点，应先构造右子树，再构造左子树
            # 构造右子树
            root.right = recursion_tree(ind + 1, in_end)
            # 构造左子树
            root.left = recursion_tree(in_start, ind - 1)

            return root

        # 创建中序遍历中(节点: 位置)键值对的哈希表
        root_map = {val: i for i, val in enumerate(inorder)}
        return recursion_tree(0, len(inorder) - 1)


if __name__ == '__main__':
    in_order = [9, 3, 15, 20, 7]
    post_order = [9, 15, 7, 20, 3]
    sol = Solution()
    result = sol.build_tree(in_order, post_order)
    print(result)
