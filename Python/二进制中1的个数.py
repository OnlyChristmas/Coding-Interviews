# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        # 复数的补码前面自动填充1
        # 方法一
        # return sum([(n>>i & 1) for i in range(0,32)])

        # 方法二
        # 标志位一路左移，做“与”操作
        #flag = 1
        #count = 0
        #for _ in range(32):
        #    if flag & n: count += 1
        #    flag = flag << 1
        #return count


        # python中 -4294967296 的二进制位 Ob0, 虽然一个负数在做了若干次“与”操作后，二进制为零，但是其十进制数是一个越来越小的负数
        # 因此在采用，“n与(n-1)做与操作恰好去掉n的最右位1”，这一性质时，终止条件不能以十进制来表示，否则是个死循环。
        # 方法三
        count = 0
        while n & 0xffffffff != 0:
            count += 1
            n = n & (n - 1)
        return count
