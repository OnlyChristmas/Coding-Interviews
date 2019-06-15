'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

'''


# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # 普通的想法时遍历n个数，找到符合要求的数
        # 更好的思路是丑数都是2，3，5的倍数，直接找到他们。不对非丑数进行取余验证。
        # 空间换时间
        if index < 1 : return 0
        res = [1]
        k2,k3,k5 = 0 ,0 ,0
        for _ in range(1,index):
            min_num = min(res[k2]*2,res[k3]*3,res[k5]*5)
            res.append(min_num)
            if min_num == res[k2]*2:
                k2+=1
            if min_num == res[k3]*3:
                k3+=1
            if min_num == res[k5]*5:
                k5+=1
        return res[-1]
             
