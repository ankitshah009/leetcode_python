#79. Word Search
#Medium
#
#Given an m x n grid of characters board and a string word, return true if word
#exists in the grid.
#
#The word can be constructed from letters of sequentially adjacent cells, where
#adjacent cells are horizontally or vertically neighboring. The same letter cell
#may not be used more than once.
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

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Backtracking DFS approach.
        """
        m, n = len(board), len(board[0])

        def dfs(i: int, j: int, k: int) -> bool:
            if k == len(word):
                return True

            if (i < 0 or i >= m or j < 0 or j >= n or
                board[i][j] != word[k]):
                return False

            # Mark as visited
            temp = board[i][j]
            board[i][j] = '#'

            # Explore neighbors
            found = (dfs(i + 1, j, k + 1) or
                     dfs(i - 1, j, k + 1) or
                     dfs(i, j + 1, k + 1) or
                     dfs(i, j - 1, k + 1))

            # Restore
            board[i][j] = temp

            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False


class SolutionOptimized:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Optimized with pruning.
        """
        from collections import Counter

        m, n = len(board), len(board[0])

        # Check if board has enough characters
        board_count = Counter(c for row in board for c in row)
        word_count = Counter(word)

        for char, count in word_count.items():
            if board_count[char] < count:
                return False

        # Reverse word if it ends with more common letter
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        def dfs(i: int, j: int, k: int) -> bool:
            if k == len(word):
                return True

            if (i < 0 or i >= m or j < 0 or j >= n or
                board[i][j] != word[k]):
                return False

            temp = board[i][j]
            board[i][j] = '#'

            result = (dfs(i + 1, j, k + 1) or
                      dfs(i - 1, j, k + 1) or
                      dfs(i, j + 1, k + 1) or
                      dfs(i, j - 1, k + 1))

            board[i][j] = temp
            return result

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False


class SolutionVisitedSet:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Using visited set instead of modifying board.
        """
        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i: int, j: int, k: int, visited: set) -> bool:
            if k == len(word):
                return True

            if (i < 0 or i >= m or j < 0 or j >= n or
                (i, j) in visited or board[i][j] != word[k]):
                return False

            visited.add((i, j))

            for di, dj in directions:
                if dfs(i + di, j + dj, k + 1, visited):
                    return True

            visited.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0, set()):
                    return True

        return False
