'''

输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）


'''


# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here

        if not pHead: return None

        # 将新结点复制出来，插进原链表
        tmp = pHead
        while tmp:
            node = RandomListNode(tmp.label)
            node.next = tmp.next
            tmp.next, tmp = node , node.next

        # 复制随机指针
        tmp = pHead
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next

        # 拆分两个链表(注意边界条件，插入后的链表一个为偶数，原链表结点为空的时候就可以停止)
        res = new_head = RandomListNode(0)
        origin = pHead
        while origin:
            new_head.next =  origin.next
            new_head = new_head.next
            origin.next = new_head.next
            origin = origin.next
        return res.next
