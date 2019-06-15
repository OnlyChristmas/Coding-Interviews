''''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.


'''


# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0) + 1
        for idx,n in enumerate(s):
            if dic.get(n,0) == 1:
                return idx
        return -1
