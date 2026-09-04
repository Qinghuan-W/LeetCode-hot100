# class Solution(object):
#     def setZeroes(self, matrix):
#         m = len(matrix)
#         n = len(matrix[0])
#
#         origin = [row[:] for row in matrix]
#
#         for i in range(m):
#             for j in range(n):
#
#                 if origin[i][j] == 0:
#                     matrix[i] = [0] * n
#
#                     for x in range(m):
#                         matrix[x][j] = 0
#
#         return matrix

class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        firstRowZero = False
        firstColZero = False

        # 先检查第一行原本有没有 0
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZero = True

        # 再检查第一列原本有没有 0
        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True

        # 用第一行、第一列做标记
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 根据标记，把内部位置清零
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 最后处理第一行
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0

        # 最后处理第一列
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0

        return matrix

print(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]))