'''
请实现两个函数，分别用来序列化和反序列化二叉树
'''



# 前序遍历 + 分治递归

# 第一种实现
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root: return "$"
        return str(root.val) + "," + self.Serialize(root.left) + "," + self.Serialize(root.right)

    def Deserialize(self, s):
        root, index = self.deserialize(s.split(","), 0)
        return root

    def deserialize(self,s,index):
        if s[index]=='$':
            return None,index+1
        root=TreeNode(int(s[index]))
        index += 1
        root.left, index = self.deserialize(s, index)
        root.right, index = self.deserialize(s, index)
        return root, index


# 第二种实现
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        return str(root.val) + "," + self.serialize(root.left) + ',' + self.serialize(root.right) if root else "$"

    def deserialize(self, data):
        self.index = -1
        data = data.split(',')
        def dfs(data):
            self.index += 1
            if data[self.index] == '$':
                return None
            root = TreeNode(int(data[self.index]))
            root.left = dfs(data)
            root.right = dfs(data)
            return root
        return dfs(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
