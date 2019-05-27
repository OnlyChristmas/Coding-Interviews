'''

请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        #def judge(l ,r):
        #    if not l and not r : return True
        #    if l and r and l.val == r.val:
        #        return judge(l.left,r.right) and judge(l.right, r.left)
        #    return False
        #
        #if not pRoot : return True
        #return judge(pRoot.left, pRoot.right)

        # 递归调用函数会有额外的开销，循环求解如下
        if not pRoot:return True
        stack = [pRoot.left, pRoot.right]
        while stack:
            node1 , node2 = stack.pop(), stack.pop()
            if not node1 and not node2 : continue
            if not node1 or not node2 : return False
            if node1.val != node2.val : return False
            stack += [node1.left,node2.right, node1.right, node2.left]
        return True
