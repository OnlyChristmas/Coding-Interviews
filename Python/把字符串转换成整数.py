'''

将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。

'''


# -*- coding:utf-8 -*-
import re
class Solution:
    def StrToInt(self, s):
        INT_MAX, INT_MIN = 2 ** 31, -2 ** 31 - 1
        all_str = list(map(str, range(10)))
        tmp = s.strip()
        if not tmp: return 0
        flag = False
        res = 0
        for i in tmp:
            if i == '-': flag = True
            if i in all_str:
                if res != 0:
                    res *= 10
                res += all_str.index(i)
            elif i != '+' and i != '-':
                return 0
        if flag:
            return -res if -res > INT_MIN else 0
        return res if res < INT_MAX else 0
