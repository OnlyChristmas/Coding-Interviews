# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        # 斐波那契数列的升级版，数学归纳法。
        return 2 ** (number - 1)
