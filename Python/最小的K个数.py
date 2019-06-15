'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

'''


# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # 如果最小的k个数字不要求顺序输出，O(n),O(1) 但是要修改原数组
        # def partition(tinput, l, r):
        #     key = tinput[l]
        #     while l < r:
        #         while l < r and key <= tinput[r]:
        #             r -= 1
        #         tinput[l] = tinput[r]
        #         while l < r and key > tinput[l]:
        #             l += 1
        #         tinput[r] = tinput[l]
        #     tinput[l] = key
        #     return l
        #
        # if not tinput: return []
        # n = len(tinput)
        # if n < k or k <= 0: return list()
        # left, right = 0, n - 1
        # index = partition(tinput, left, right)
        # while index + 1 != k:
        #     if index + 1 < k:
        #         left = index + 1
        #     else:
        #         right = index - 1
        #     index = partition(tinput, left, right)
        # return sorted(tinput[:k])

        # 不需要修改原数字，O(nlogk)，O(1) ,当n非常大时，占用内存小，仅读入一个大小为k的堆。对增量式数据也很友好。
        def heapAjust(nums, start, end):
            temp = nums[start]  # 记录较大的那个孩子下标
            child = 2 * start + 1
            while child <= end:  # 比较左右孩子，记录较大的那个
                if child + 1 <= end and nums[child] < nums[child + 1]:  # 如果右孩子比较大，下标往右移
                    child += 1
                if temp >= nums[child]:  # 如果根已经比左右孩子都大了，直接退出
                    break
                nums[start] = nums[child]  # 如果根小于某个孩子,将较大值提到根位置
                # nums[start], nums[child] = nums[child], nums[start]
                start = child  # 接着比较被降下去是否符合要求，此时的根下标为原来被换上去的那个孩子下标
                child = child * 2 + 1  # 孩子下标也要下降一层
            nums[start] = temp  # 最后将一开始的根值放入合适的位置(如果前面是交换，这句就不要)

        n = len(tinput)
        if not tinput: return []
        if k <= 0 or k > n: return []
        for i in range(int(k / 2) - 1, -1, -1):  # 建立大顶堆
            heapAjust(tinput, i, k - 1)
        for i in range(k, n):
            if tinput[i] < tinput[0]:
                tinput[0], tinput[i] = tinput[i], tinput[0]
                heapAjust(tinput, 0, k - 1)  # 调整前k个数
        return sorted(tinput[:k])
