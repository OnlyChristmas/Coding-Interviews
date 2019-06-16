'''

给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

'''



# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # Approach one   O(n) ~ O(kn)
        # length = len(nums)
        # if k > length or k <= 0: return []
        # l , r = 0 , k-1
        # res = [max(nums[l:r+1])]
        # r += 1
        # while r < length:
        #     if nums[r] >= res[-1]:
        #         res.append(nums[r])
        #         l += 1
        #         r += 1
        #     elif nums[l] == res[-1]:
        #         l += 1
        #         res.append(max(nums[l:r+1]))
        #         r += 1
        #     else:
        #         res.append(res[-1])
        #         l += 1
        #         r += 1
        # return res



        # Approch two   一个双向队列  O(n) , O(1)
        res , tmp = [] , []
        if size > len(num) or size <= 0 : return []
        for i in range(len(num)):
            if len(tmp) > 0 and tmp[0] <= i - size:
                tmp.pop(0)
            while len(tmp) > 0 and num[tmp[-1]] <= num[i]:
                tmp.pop()
            tmp.append(i)
            if i >= size-1:
                res.append(num[tmp[0]])
        return res
            
