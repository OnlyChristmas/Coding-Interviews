'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

'''


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        # 递归解法只需要一个新头结点,但注意特殊情况空链表
        if not pHead1: return pHead2
        if not pHead2: return pHead1
        head = ListNode(None)
        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2


        # 循环的解法需要两个新头结点，并注意拼接尾链
        #res = cur = ListNode(None)
        #while pHead1 and pHead2:
        #    if pHead1.val <= pHead2.val:
        #        cur.next, pHead1 = pHead1, pHead1.next
        #    else:
        #        cur.next, pHead2 = pHead2, pHead2.next
        #    cur = cur.next
        #cur.next = pHead1 if pHead1 else pHead2
        #return res.next
