


'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix: return []
        res = []
        flag = [0, 0, 0, 1]
        i, j = 0, 0
        row, col, row_l, col_l = len(matrix), len(matrix[0]), -1, -1
        number = row * col
        while len(res) < number:
            res.append(matrix[i][j])
            if flag[3]:
                j += 1
                if j == col:
                    flag = [0, 1, 0, 0]
                    j -= 1
                    i += 1
                    row_l += 1
                    continue
            if flag[1]:
                i += 1
                if i == row:
                    flag = [0, 0, 1, 0]
                    i -= 1
                    j -= 1
                    col -= 1
                    continue
            if flag[2]:
                j -= 1
                if j == col_l:
                    flag = [1, 0, 0, 0]
                    j += 1
                    i -= 1
                    row -= 1
                    continue
            if flag[0]:
                i -= 1
                if i == row_l:
                    flag = [0, 0, 0, 1]
                    i += 1
                    j += 1
                    col_l += 1
                    continue
        return res
