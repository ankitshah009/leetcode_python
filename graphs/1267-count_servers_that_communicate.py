#1267. Count Servers that Communicate
#Medium
#
#You are given a map of a server center, represented as a m * n integer matrix
#grid, where 1 means that on that cell there is a server and 0 means that it
#is no server. Two servers are said to communicate if they are on the same row
#or on the same column.
#
#Return the number of servers that communicate with any other server.
#
#Example 1:
#Input: grid = [[1,0],[0,1]]
#Output: 0
#Explanation: No servers can communicate with others.
#
#Example 2:
#Input: grid = [[1,0],[1,1]]
#Output: 3
#Explanation: All three servers can communicate with at least one other server.
#
#Example 3:
#Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
#Output: 4
#Explanation: The two servers in the first row can communicate with each other.
#The two servers in the third column can communicate with each other.
#The server at right bottom corner can't communicate with any other server.
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m <= 250
#    1 <= n <= 250
#    grid[i][j] == 0 or 1

from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        """
        Count servers in each row and column.
        Server communicates if row_count > 1 or col_count > 1.
        """
        m, n = len(grid), len(grid[0])

        # Count servers per row and column
        row_count = [sum(grid[i]) for i in range(m)]
        col_count = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        result += 1

        return result


class SolutionTwoPasses:
    def countServers(self, grid: List[List[int]]) -> int:
        """Alternative with explicit counting"""
        m, n = len(grid), len(grid[0])

        row_count = [0] * m
        col_count = [0] * n

        # First pass: count servers
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # Second pass: count communicating servers
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    count += 1

        return count
