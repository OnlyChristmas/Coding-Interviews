'''

入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''



# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        # Approach one O(n) 空间复杂度
        #def preRoot(root):
        #    if not root: return []
        #    return [root.val] + preRoot(root.left) + preRoot(root.right)
        #if not pRoot1 or not pRoot2: return False
        #l1 = preRoot(pRoot1)
        #l2 = preRoot(pRoot2)
        #for i in range(len(l1)):
        #    if l1[i] == l2[0] and l1[i:len(l2)+i] == l2:
        #        return True


        # Approach two  O(m)~O(n*m)  O(1)
        def is_subTree(root1, root2):
            if not root2: return True
            if not root1 or root1.val != root2.val: return False
            return is_subTree(root1.left, root2.left) and is_subTree(root1.right, root2.right)

        if not pRoot1 or not pRoot2: return False
        return is_subTree(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left , pRoot2) or self.HasSubtree(pRoot1.right , pRoot2)
