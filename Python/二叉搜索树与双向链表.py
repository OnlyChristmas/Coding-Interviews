'''

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.head = None
        self.tail = None
    def Convert(self, pRootOfTree):
        # write code here
        # 中序遍历与递归，记住最左端节点，另一个辅助指针构建双向链表。
        #  思路解释 https://blog.csdn.net/huhehaotechangsha/article/details/90770854
        if not pRootOfTree: return
        self.Convert(pRootOfTree.left)
        if not self.head :
            self.head,self.tail = pRootOfTree,pRootOfTree
        else:
            self.tail.right,pRootOfTree.left = pRootOfTree,self.tail
            self.tail = self.tail.right
        self.Convert(pRootOfTree.right)
        return self.head
