# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack_A = []
        self.stack_B = []
    def push(self, node):
        # write code here
        self.stack_A.append(node)
    def pop(self):
        # return xx
        if self.stack_B: return self.stack_B.pop()
        else:
            while self.stack_A:
                self.stack_B.append(self.stack_A.pop())
            return self.stack_B.pop()