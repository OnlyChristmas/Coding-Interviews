'''

给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

''''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):

        # Approach one
        if not pRoot or k <= 0: return None
        def inorder(pRoot):
            if not pRoot: return []
            return inorder(pRoot.left) + [pRoot] + inorder(pRoot.right)
        res = inorder(pRoot)
        return res[k-1] if k <= len(res) else None



        # Approach two
        # if not root or k <= 0: return None
        # res , stack = [], []
        # while True:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     if not stack:
        #         if k > len(res):
        #             return None
        #         else:
        #             return res[k-1]
        #     node = stack.pop()
        #     res.append(node)
        #     if node.right: root = node.right
        
