# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 or rows <= 0 or cols <= 0: return 0
        visited = [[1 for _ in range(cols)] for _ in range(rows)]
        return self.count(threshold, cols, rows, 0 ,0 ,visited)

    def count(self,threshold, cols, rows, i , j ,visited):
        if i >= rows or j >= cols or visited[i][j] == 0 or threshold < sum(map(int,str(i)+str(j))): return 0
        visited[i][j] = 0
        return 1 + self.count(threshold, cols, rows, i + 1 , j ,visited) + self.count(threshold, cols, rows, i  , j + 1,visited)
