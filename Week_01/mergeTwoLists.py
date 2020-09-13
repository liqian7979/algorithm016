# -*- coding: utf-8 -*-
# @ModuleName: mergeTwoLists
# @Author: Liqian
# @Time: 2020/9/11 21:36
# @Software: PyCharm
"""
合并两个有序链表
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成。
示例：
    输入：1 -> 2 -> 4, 1 -> 3 -> 4
    输出：1 -> 1 -> 2 -> 3 -> 4 -> 4
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_node(data):
    """单链表初始化"""
    head = ListNode(val=data[0], next=None)
    node = head
    for d in data[1:]:
        node.next = ListNode(val=d, next=None)
        node = node.next
    return head


class Solution(object):
    def merge_two_lists(self, l1: ListNode, l2: ListNode):
        """递归实现"""
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.merge_two_lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_lists(l1, l2.next)
            return l2

    def merge_two_lists2(self, l1, l2):
        """非递归实现"""
        # 定义一个空的头节点
        head = ListNode()
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return head.next


if __name__ == '__main__':
    data1 = [1, 2, 3]
    data2 = [1, 3, 4]
    ln1 = list_node(data1)
    ln2 = list_node(data2)
    sol = Solution()
    # merge_result = sol.merge_two_lists(ln1, ln2)
    merge_result = sol.merge_two_lists2(ln1, ln2)
    print(merge_result)