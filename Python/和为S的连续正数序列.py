'''

小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

'''



# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        l, r = 1, 2
        max_num = tsum // 2 + 1
        tsum = 2 * tsum
        while r <= max_num:
            key = (l + r) * (r - l + 1)
            if key == tsum:
                if r - l + 1 > 1: res.append([i for i in range(l, r + 1)])
                r += 1
            elif key < tsum:
                r += 1
            else:
                l += 1
        return res
