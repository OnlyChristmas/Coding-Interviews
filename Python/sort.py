# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：        sort
   Description :
   Author :           bw_zhang
   date：             2019/3/26 14:55
-------------------------------------------------
   Change Activity:   2019/3/26 14:55
-------------------------------------------------
"""

import time
import random




def BubbleSort(nums):
    start = time.time()
    if len(nums) < 2: return nums
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    print('BubbleSort answer is {}, used {} : '.format(nums, time.time() - start))



def BubbleSort_quick(nums):
    start = time.time()
    if len(nums) < 2: return nums
    flag = True
    for i in range(len(nums)):
        if flag == False : break
        flag = False
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                flag = True
    print('BubbleSort_quick answer is {}, used {} : '.format(nums, time.time() - start))


def SelectSort(nums):
    start = time.time()
    if len(nums) < 2: return nums
    for i in range(len(nums)):
        min_num = i 
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_num]:
                min_num = j
        if min_num != i:
            nums[min_num], nums[i] = nums[i], nums[min_num]
    print('SelectSort answer is {}, used {} : '.format(nums, time.time() - start))


def InsertSort(nums):
    start = time.time()
    if len(nums) < 2: return nums
    key = 1
    while key < len(nums):
        for i, n in enumerate(nums[:key]):
            if nums[key] < n:
                nums.insert(i, nums.pop(key))
                break
            if i == len(nums[:key]) - 1 : nums.insert(i + 1 , nums.pop(key)) 
        key += 1
    print('InsertSort answer is {}, used {} : '.format(nums, time.time() - start))





def QuickSort(nums, left, right):
    if left >= right: return  # 快排是一个原地排序，不需要返回nums
    low, high = left, right
    key = nums[low]
    while left < right:
        while left < right and nums[right] > key:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= key:
            left += 1
        nums[right] = nums[left]
    nums[right] = key
    QuickSort(nums, low, left - 1)
    QuickSort(nums, left + 1, high)




def QuickSort_approach_two(array, l, r):
    def partition(array, l, r):
        key = array[l]
        while l < r:
            while l < r and array[r] >= key:
                r -= 1
            if l < r:
                array[l] = array[r]
            while l < r and array[l] < key:
                l += 1
            if l < r:
                array[r] = array[l]
        array[l] = key
        return l

    if l < r:
        if len(array) < 2: return
        q = partition(array, l, r)
        QuickSort_approach_two(array, l, q - 1)
        QuickSort_approach_two(array, q + 1, r)





def merge_sort(nums):
    if len(nums) < 2 : return nums    
    mid = len(nums) //2
    first = merge_sort(nums[:mid])
    secend = merge_sort(nums[mid:])
    return merge(first, secend)

def merge(first, secend):
    result = []
    i , j = 0 , 0
    length_f, length_s = len(first), len(secend) 
    while i < length_f and j < length_s:
        if first[i] <= secend[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(secend[j])
            j += 1
    return result +  first[i:] + secend[j:]






def MAX_Heapify(heap,HeapSize,root):#在堆中做结构调整使得父节点的值大于子节点
    left = 2*root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:#如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger],heap[root] = heap[root],heap[larger]
        MAX_Heapify(heap, HeapSize, larger)

def Build_MAX_Heap(heap):#构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)#将堆的长度当独拿出来方便
    for i in range((HeapSize -2)//2,-1,-1):#从后往前出数
        MAX_Heapify(heap,HeapSize,i)

def HeapSort(heap):#将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    if len(heap) < 2 : return heap
    start = time.time()
    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        MAX_Heapify(heap, i, 0)
    print('InsertSort answer is {}, used {} : '.format(heap, time.time() - start))




if __name__ == '__main__':
    little = [30,50,57,77,62,78,94,80,84]
    nums = [random.randint(1,1000) for i in range(1000)]
    # num = [5, 3, 8, 6, 4, 5, 9, 39, 30, 9, 0, 4, 1, 62, 5]
    # num = [random.randrange(-100000, 100000, 1) for _ in range(10000)]

    # BubbleSort(nums+ [i for i in range(1000) ])
    # BubbleSort_quick(nums + [i for i in range(1000) ])

    # SelectSort(num)
    # InsertSort(nums)
    # QuickSort_1(num, 0, len(num) - 1)
    # QuickSort(num, 0, len(num) - 1)
    # QuickSort_approach_two(num, 0, len(num) - 1)
    # print(num)
    # print(merge_sort(nums))

    HeapSort(little)



   