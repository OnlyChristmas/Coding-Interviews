'''

题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。


'''



# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        length = len(ss)
        if length == 0: return []
        if length == 1: return [ss]
        res = []
        for i in range(length):
            for j in self.Permutation(ss[:i]+ss[i+1:]):
                if ss[i] + j not in res : res.append(ss[i] + j)
        return res
