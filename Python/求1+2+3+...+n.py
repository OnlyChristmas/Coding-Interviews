''''
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''
# -*- coding:utf-8 -*-
class Solution:
    # 主要考察面试人的心态是否积极，这个题目本身意义不大，实际环境中不会涉及到
    # 想法一： 构造函数求解
    # 想法二： 虚函数求解
    # 想法三： 利用函数指针求解
    # 想法四： 利用模板类型求解

    def __init__(self):
        self.sum = 0
    def Sum_Solution(self, n):
        # write code here
        def qiusum(n):
            self.sum += n
            n -= 1
            return n>0 and self.Sum_Solution(n)

        qiusum(n)
        return self.sum
