'''

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

'''


# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers: return None
        key, num = numbers[0], 1
        for i in numbers[1:]:
            if i == key:
                num += 1
            else:
                num -= 1
                if num == 0:
                    key = i
                    num = 1
        num = 0
        for i in numbers:
            if i == key:
                num += 1
        return key if num * 2 > len(numbers) else 0
