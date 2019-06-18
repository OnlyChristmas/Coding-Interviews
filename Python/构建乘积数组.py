'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

'''


# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        length = len(A)
        if not length: return []
        C, D = [1 for _ in range(length)], [1 for _ in range(length)]
        for i in range(1, length):
            C[i] = C[i - 1] * A[i - 1]
        for i in range(length - 2, -1, -1):
            D[i] = D[i + 1] * A[i + 1]
        return [i * j for i, j in zip(C, D)]
