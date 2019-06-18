'''

写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。


'''


# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # 不能用运算符，很容易想到是基于位运算和二进制的解法（加法三步走战略）
        # 第一步：两个数加和但不进位，也就是 0+0=0；0+1=1；1+0=1；1+1=0  可以用异或代替
        # 第二步：找到进位的位置，0+0=0；0+1=0；1+0=0；1+1=10 , 用与运算加左移一位的方式代替，
        # 第三步：重复上述两步，直到没有进位为止。

        # 如果出现负数上述方法会有问题，需要额外处理，相当于实现了减法
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while num2:
            num1, num2 = num1 ^ num2, (num1 & num2) << 1
            num1 = num1 & mask
            num2 = num2 & mask
        return num1 if num1 <= MAX else ~(num1 ^ mask)


        # 瞎抖机灵
        # return sum([num1,num2])
