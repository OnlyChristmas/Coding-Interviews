'''
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)

'''


# -*- coding:utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def LastRemaining_Solution(self, n, m):
        # 本题式著名的约瑟夫环问题

        # Approach one 动规求解
        # 第n次选中某个数字是建立在第n-1次选中某个数字的基础上。因此关键是找到递归公式。
        # 每次递归的起点是不一样的，要找到起点的规律（角标映射的规律）
        # 如果第1次删除第k个数字，那么下次的起点就是k+1，考虑k之间的数字会补在最后, 加入取余运算。因此可以有映射关系P(x)=(x-k-1)%n
        # 但是现在需要逆向的关系公式， 因此逆映射为 p^-1(x) = (x+k+)%n = (x+m)%n
        # 另外，当只有一个数字可选的时候，显然f(0) = 0， 这是动规边界条件。
        # if n <= 0 or m <= 0: return -1
        # res = 0
        # for i in range(2, n + 1):
        #     res = (res + m) % i
        # return res

        # Approach two 环形链表求解
        if n <= 0 or m <= 0: return -1
        head = q = ListNode(0)
        for i in range(1, n):
            q.next = ListNode(i)
            q = q.next
        q.next = head

        while n > 1:
            for i in range(1, m):
                head = head.next
            head.val = head.next.val
            head.next = head.next.next
            n -= 1
        return head.val
