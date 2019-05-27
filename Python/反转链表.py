'''

输入一个链表，反转链表后，输出新链表的表头。
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        # 注意空链表情况下的返回值
        pre = None
        while pHead:
            cur = pHead
            pHead = pHead.next
            cur.next = pre
            pre = cur
        return pre
