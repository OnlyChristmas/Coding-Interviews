'''

从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot : return []
        q , res = [pRoot] ,[]
        while q:
            length = len(q)
            cur = []
            for _ in range(length):
                node = q.pop(0)
                cur.append(node.val)
                if node.left:  q.append(node.left)
                if node.right:  q.append(node.right)
            res.append(cur)
        return res
