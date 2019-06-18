'''

我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

'''



class Solution:
    def rectCover(self, number):
        number <= 0: return 0
        a, b = 1,2
        while number > 2:
            a, b = b, a+b
            number -= 1
        return b if number != 1 else a# write code here
