''''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.


'''


# -*- coding:utf-8 -*-
class Solution:
    def offer50(s):
        # 注意时间与空间的平衡 O(n) O(1)
        dic = dict()
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for idx, n in enumerate(s):
            if dic.get(n, 0) == 1:
                return idx
        return -1

    	# Approach two  因为候选的字符有限，可以从字符的角度循环，不需要辅助的存储空间，还能加速运算
        # res = [s.index(i) for i in string.ascii_lowercase if s.count(i) == 1 ]
        # return min(res) if res else -1

# 相关题目1 ： 输入两个字符串，从第一个字符串中删除在第二个字符串中出现过的所有字符。
# 类似解决思路：将第二个字符串中出现的字符建立哈希表。再遍历第一个字符串中的每个字符，查询只需O(1)。总的时间复杂度O(n),空间复杂度O(1)

# 相关题目2：删除一个字符串中出现的所有重复字符。
# 类似解决思路：根据ASCII建立一个哈希表，默认所有为0。如果出现一次则改为1。遍历过程中每个字符都查询哈希表O(1)。总的时间复杂度O(n),空间复杂度O(1)

# 相关题目3：如果两个字符串出现的字符类型以及其数量都完全一致，只是位置不一样，成为变位词。如何检测是否是变位词。
# 类似解决思路：遍历第一个字符串建立哈希表统计出现的字符及其个数，再对第二个字符串进行遍历的时候出现相同字符就减一（前提哈希表中存在这个字符），如果最后哈希表中所有的字符数量都为0，则是变位数。

# 进阶问题：找到一个字符流中第一个只出现一次的字符位置。
# 相似解法：首先考虑如何存放字符流方便查找操作，这里选用哈希表。同样根据字符的读入逐渐建立。如果该字符不存在于哈希表，则value记录其位置；如果已存在，将其value改为-1。当字符流终止时，只需要遍历哈希表，找到其value值为正，且数值最小的value输出。

class Offer50_1:
    # 字符流中的第一个不重复的字符
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
        self.dic[char] = self.dic.get(char, 0) + 1
