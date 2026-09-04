# class Solution(object):
#     def rotate(self, matrix):
#         m = len(matrix)
#         n = len(matrix[0])
#         result = []
#
#         for i in range(n):
#             newRow = []
#
#             for j in range(m-1,-1,-1):
#                 newRow.append(matrix[j][i])
#
#             result.append(newRow)
#
#         return result

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(n - i - 1):
               matrix[i][j],matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i],matrix[i][j]

        matrix.reverse()

        return matrix


print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))