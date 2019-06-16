'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

''''



# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        def isBalanced(root):
            if not root or self.flag == False: return 0
            left = isBalanced(root.left)
            right = isBalanced(root.right)
            if abs(left - right) > 1: self.flag = False
            return max(left, right) + 1

        self.flag = True
        isBalanced(pRoot)
        return self.flag
