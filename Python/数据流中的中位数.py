''''

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

''''



# -*- coding:utf-8 -*-
from heapq import *
class Solution:
    # 用平衡的二叉搜索树或者最大最小堆实现， O(logn) 插入新数据 , O(1) 获取中位数

    def __init__ (self):
        self.maxheap = []
        self.minheap = []
    def Insert(self, num):
        if (len(self.maxheap)+len(self.minheap))&1: #总数为奇数插入最大堆
            if len(self.minheap)> 0:
                if num > self.minheap[0]:#大于最小堆里的元素
                    heappush(self.minheap, num)#新数据插入最小堆
                    heappush(self.maxheap, -self.minheap[0])#最小堆中的最小插入最大堆
                    heappop(self.minheap)
                else:
                    heappush(self.maxheap, -num)
            else:
                heappush(self.maxheap, -num)
        else:                           #总数为偶数 插入最小堆
            if len(self.maxheap)> 0: #小于最大堆里的元素
                if num < -self.maxheap[0]:
                    heappush(self.maxheap, -num)#新数据插入最大堆
                    heappush(self.minheap, -self.maxheap[0])#最大堆中的最大元素插入最小堆
                    heappop(self.maxheap)
                else:
                    heappush(self.minheap, num)
            else:
                heappush(self.minheap, num)
    def GetMedian(self,n=None):
        if (len(self.maxheap)+len(self.minheap))&1:
            mid = self.minheap[0]
        else:
            mid = (self.minheap[0]-self.maxheap[0])/2.0
        return mid
