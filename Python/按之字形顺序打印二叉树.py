'''
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        res , q = [] ,[pRoot]
        next_right = True
        while q:
            length = len(q)
            cur = []
            for _ in range(length):
                node = q.pop(0)
                cur.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            next_right = not next_right
            res.append(cur[::-1] if next_right else cur)
        return res
