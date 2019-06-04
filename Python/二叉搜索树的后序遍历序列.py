'''

入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''


# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        length = len(sequence)
        if not sequence : return False
        if length <= 2: return True

        left = 0  # 判断左右子树是否满足二叉搜索树要求
        while sequence[left] < sequence[-1]:
            left += 1
        for j in range(left, length-1):
            if sequence[j] < sequence[-1]:
                return False
        # 左右子树为空的时候返回False
        return self.VerifySquenceOfBST(sequence[:left]) or self.VerifySquenceOfBST(sequence[left:length-1])
