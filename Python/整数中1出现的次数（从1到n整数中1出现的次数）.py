'''

求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

'''


# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res = 0
        s = str(n)
        length = len(s)
        for idx, i in enumerate(s):
            place = length - idx  # 当前位数（个位是1，十位是2……）
            pre = n // (10 ** place)  # 当前位数的高位数字
            aft = n % (10 ** (place - 1))  # 当前位数的低位数字
            if i == '0':
                res += pre * 10 ** (place - 1)
            elif i == '1':
                res += pre * 10 ** (place - 1) + aft + 1
            else:
                res += (pre + 1) * 10 ** (place - 1)
        return res
