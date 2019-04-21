# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here

        # Approach one
        # return any(target in n  for n in array)


        # Approach two
        if array == ([] or [[]]) : return False
        col , row = len(array[0]) , len(array)
        r, c = row - 1 ,0
        while 0 <= c < col and 0 <= r < row :
            print(r,c )
            if array[r][c] < target:
                c += 1
            elif array[r][c] > target:
                r -= 1
            else:
                return True
        return False
