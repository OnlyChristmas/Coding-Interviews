'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

'''


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        fast , slow = pHead, pHead
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast and fast == slow:
                slow = pHead
                while fast != slow:
                    fast = fast.next
                    slow  = slow.next
                return fast
        return None
