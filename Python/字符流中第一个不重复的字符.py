'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
'''


# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.nums = []
        self.key_loc = 0
        self.dic = dict()
    def FirstAppearingOnce(self):
        for i in self.nums[self.key_loc:]:
            if self.dic.get(i) == 1:
                self.key_loc = self.nums.index(i)
                return i
        return '#'
    def Insert(self, char):
        self.nums.append(char)
        self.dic[char] = self.dic.get(char,0)+1
        
