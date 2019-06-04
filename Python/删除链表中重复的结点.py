'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

'''


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here

        # 注意所有节点都一样的情况,如何删除最后一个结点
        res = pre = ListNode(-1)
        res.next = tmp = pHead
        while tmp:
            if tmp.next and tmp.val == tmp.next.val:
                cur = tmp.next
                while cur and cur.val == tmp.val:
                    cur = cur.next
                pre.next, tmp = cur, cur
            else:
                pre = tmp
                tmp = tmp.next
        return res.next
