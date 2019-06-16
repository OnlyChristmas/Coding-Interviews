''''

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
''''




# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # 此题类似于leetcode 315题
         # Approach one 归并排序

        def MergeSort(enum):
            global res
            half = len(enum) // 2
            if half:
                left, right = MergeSort(enum[:half]), MergeSort(enum[half:])
                m, n = len(left), len(right)
                i = j = 0
                while i < m or j < n:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        enum[i+j] = left[i]
                        res += j
                        i += 1
                    else:
                        enum[i+j] = right[j]
                        j += 1
            return enum

        if len(data) < 2: return [0 for _  in range(len(data))]
        global res
        res = 0
        MergeSort(list(enumerate(data)))
        return res % 1000000007
