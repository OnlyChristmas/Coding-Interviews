'''
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。


'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        # 简单版本
        #res = []
        #while listNode:
        #    res.append(listNode.val)
        #    listNode = listNode.next
        #return res[::-1]


        # 同时复习一下反转链表题目
        res = []
        pre = None
        while listNode:
            res.insert(0, listNode.val)
            cur = listNode
            listNode = listNode.next
            cur.next = pre
            pre = cur
        return res
