#118. Pascal's Triangle
#Easy
#
#Given an integer numRows, return the first numRows of Pascal's triangle.
#
#In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
#Example 1:
#Input: numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
#Example 2:
#Input: numRows = 1
#Output: [[1]]
#
#Constraints:
#    1 <= numRows <= 30

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(row)

        return result
