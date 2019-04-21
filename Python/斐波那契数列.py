# -*- coding:utf-8 -*-


class Solution:
    def Fibonacci(self, n):
        # write code here
        # 迭代法
        #if n == 0: return 0
        #elif n == 1: return 1
        #else:
        #    a, b = 0, 1
        #    while n > 1:
        #        a, b = b, a + b
        #       n -= 1
        #    return b
        
        # 递归法  效率低,且容易栈溢出，无法通过
        #if n == 0:return 0
        #if n == 1:return 1
        #return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
        
        # 公式法
        root_five = 5**0.5
        result = (((1 + root_five) / 2)**n - ((1 - root_five) / 2)**n) / root_five
        return int(result)
