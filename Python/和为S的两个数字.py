'''

输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的，且小的数字在前面。

'''


# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array: return []
        l , r = 0 , len(array) -1
        while l < r:
            if array[l] + array[r] == tsum:
                return [array[l],array[r]]
            elif array[l] + array[r] < tsum:
                l += 1
            else:
                r -= 1
        return []
