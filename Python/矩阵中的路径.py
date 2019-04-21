# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if len(matrix) < 1 or rows <= 0 or cols <= 0 or not path: return False
    # 对于python来说，set、list、dict都是可变对象，不能直接在上边操作防止重复遍历。
    # 但如果输入是string是不可变对象，可以直接在上面操作。
        for i in range(rows):
            for j in range(cols):
                if path[0] == matrix[i*cols+j]:
                    if self.find(list(matrix), rows, cols, path[1:], i, j):
                        return True
        return False

    def find(self, matrix, rows, cols, path, i, j):
        if not path: return True
        matrix[i*cols+j] ='0'
        if j + 1 < cols  and matrix[i*cols+j+ 1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j + 1)
        elif j - 1 >= 0  and matrix[i*cols+j- 1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j - 1)
        elif i + 1 < rows  and matrix[(i+1)*cols+j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i + 1, j)
        elif i - 1 >= 0 and matrix[(i-1)*cols+j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i - 1, j)
        else:
            return False
