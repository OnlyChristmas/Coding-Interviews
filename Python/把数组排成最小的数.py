'''

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。


'''


# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # 由于整数的拼接很容易造成大数问题导致溢出，这里按照字符串拼接来处理。
        if not numbers: return ""
        compare = lambda a, b:int(str(a) + str(b)) - int(str(b) + str(a))
        min_string = sorted(numbers, cmp = compare)
        return ''.join(str(s) for s in min_string)
