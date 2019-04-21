# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        # 迭代法
        if number == 1: return 1
        if number == 2: return 2
        a,b = 1,2
        while number > 2:
           a,b = b,a+b
           number -= 1
        return b

        # 递归法  时间开销过大，栈溢出
        # if number == 1: return 1
        # if number == 2: return 2
        # return self.jumpFloor(number-1) + self.jumpFloor(number-2)
