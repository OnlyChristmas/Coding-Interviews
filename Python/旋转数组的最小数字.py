# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray == []: return None
        l, r = 0, len(rotateArray) - 1
        while l < r:
            mid = (r + l) // 2
            if rotateArray[mid] > rotateArray[l]:
                l = mid
            elif rotateArray[mid] < rotateArray[l]:
                r = mid
            else:
                l += 1
        return rotateArray[l]
