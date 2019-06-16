'''

统计一个数字在排序数组中出现的次数。
'''



# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # 直观的想法从前到后的顺序遍历，但是算法题几乎不会将顺序查找作为考察要点……

        def getFirst(nums):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if data[mid] >= k:      # 注意前后两个二分查找条件不一致
                    end = mid - 1
                else:
                    start = mid + 1
            # 导致两个函数越界的指针不一致，应该返回的指针是非越界指针
            return start if start < len(nums) and nums[start] == k else -1
        def getLast(nums):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if data[mid] <= k:
                    start = mid + 1
                else:
                    end = mid - 1
            return end if end < len(nums) and nums[end] == k else -1

        if not data: return 0
        first, last = getFirst(data), getLast(data)
        return last - first + 1 if first != -1 and last != -1 else 0
