'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''


# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        #if len(array) < 2: return array
        #i = 0
        #while True:
        #    if not (array[i] & 1):
        #        for j in range(i + 1, len(array)):
        #            if array[j] & 1:
        #                key = j
        #                break
        #            elif j == len(array) -1:
        #                return array
        #        while key > i:
        #            array[key], array[key - 1] = array[key - 1], array[key]
        #            key -= 1
        #    else:
        #        i += 1

        # 简化版本
        if len(array) < 2: return array
        for i in range(len(array)):
            for j in range(len(array) - 1, i, -1):
                if array[j] & 1 and not (array[j - 1] & 1):
                    array[j], array[j - 1] = array[j - 1], array[j]
        return array
