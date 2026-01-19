#79. Word Search
#Medium
#
#Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
#The word can be constructed from letters of sequentially adjacent cells, where adjacent cells
#are horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
#Example 1:
#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
#Output: true
#
#Example 2:
#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
#Output: true
#
#Example 3:
#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
#Output: false
#
#Constraints:
#    m == board.length
#    n = board[i].length
#    1 <= m, n <= 6
#    1 <= word.length <= 15
#    board and word consists of only lowercase and uppercase English letters.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = '#'  # Mark as visited

            found = (dfs(i + 1, j, k + 1) or
                     dfs(i - 1, j, k + 1) or
                     dfs(i, j + 1, k + 1) or
                     dfs(i, j - 1, k + 1))

            board[i][j] = temp  # Restore
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
