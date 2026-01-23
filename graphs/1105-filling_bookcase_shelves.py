#1105. Filling Bookcase Shelves
#Medium
#
#You are given an array books where books[i] = [thicknessi, heighti] indicates
#the thickness and height of the ith book. You are also given an integer
#shelfWidth.
#
#We want to place these books in order onto bookcase shelves that have a
#total width shelfWidth.
#
#We choose some of the books to place on this shelf such that the sum of
#their thickness is less than or equal to shelfWidth, then build another
#level of the shelf of the bookcase so that the total height of the bookcase
#has increased by the maximum height of the books we just put down. We repeat
#this process until there are no more books to place.
#
#Note that at each step of the above process, the order of the books we place
#is the same order as the given sequence of books.
#
#Return the minimum possible height that the total bookshelf can be after
#placing shelves in this manner.
#
#Example 1:
#Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
#Output: 6
#Explanation:
#The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
#
#Example 2:
#Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
#Output: 4
#
#Constraints:
#    1 <= books.length <= 1000
#    1 <= thicknessi <= shelfWidth <= 1000
#    1 <= heighti <= 1000

from typing import List
from functools import lru_cache

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """
        DP: dp[i] = min height to place books[0:i]
        For each book i, try placing it with previous books on same shelf.
        """
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            width = 0
            height = 0

            # Try placing books[j:i] on the same shelf
            for j in range(i, 0, -1):
                width += books[j - 1][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + height)

        return dp[n]


class SolutionMemo:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """Memoized recursion"""
        n = len(books)

        @lru_cache(maxsize=None)
        def dp(i):
            if i == n:
                return 0

            width = 0
            height = 0
            result = float('inf')

            for j in range(i, n):
                width += books[j][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j][1])
                result = min(result, height + dp(j + 1))

            return result

        return dp(0)


class SolutionOptimized:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """Space-optimized with rolling array not needed - already O(n) space"""
        n = len(books)
        dp = [0] + [float('inf')] * n

        for i in range(1, n + 1):
            width, height = 0, 0
            j = i
            while j > 0:
                width += books[j - 1][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + height)
                j -= 1

        return dp[n]
