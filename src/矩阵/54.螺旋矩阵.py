class Solution(object):

    def rotateMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        newMatrix = []

        for j in range(n - 1, -1, -1):
            newRow = []

            for i in range(m):
                newRow.append(matrix[i][j])

            newMatrix.append(newRow)
        return newMatrix

    def saveFirstLine(self,matrix):
        result = []
        for i in range(len(matrix[0])):
            result.append(matrix[0][i])
        return result

    def deleteFirstLine(self,matrix):
        matrix.pop(0)
        return matrix



    def spiralOrder(self, matrix):
        result = []
        while matrix:
            result.extend(self.saveFirstLine(matrix))
            self.deleteFirstLine(matrix)

            if matrix:
                matrix = self.rotateMatrix(matrix)

        return result




print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))