#944. Delete Columns to Make Sorted
#Easy
#
#You are given an array of n strings strs, all of the same length.
#
#The strings can be arranged such that there is one on each line, making a grid.
#
#You want to delete the columns that are not sorted lexicographically.
#
#Return the number of columns that you will delete.
#
#Example 1:
#Input: strs = ["cba","daf","ghi"]
#Output: 1
#Explanation: Column 1 'b','a','h' is not sorted, so delete it.
#
#Example 2:
#Input: strs = ["a","b"]
#Output: 0
#
#Example 3:
#Input: strs = ["zyx","wvu","tsr"]
#Output: 3
#
#Constraints:
#    n == strs.length
#    1 <= n <= 100
#    1 <= strs[i].length <= 1000
#    strs[i] consists of lowercase English letters.

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        """
        Count columns that are not sorted.
        """
        if not strs:
            return 0

        count = 0
        n_rows = len(strs)
        n_cols = len(strs[0])

        for col in range(n_cols):
            for row in range(1, n_rows):
                if strs[row][col] < strs[row - 1][col]:
                    count += 1
                    break

        return count


class SolutionZip:
    """Using zip to get columns"""

    def minDeletionSize(self, strs: list[str]) -> int:
        count = 0

        for col in zip(*strs):
            if list(col) != sorted(col):
                count += 1

        return count


class SolutionCompact:
    """One-liner"""

    def minDeletionSize(self, strs: list[str]) -> int:
        return sum(list(col) != sorted(col) for col in zip(*strs))


class SolutionAll:
    """Using all()"""

    def minDeletionSize(self, strs: list[str]) -> int:
        count = 0
        for col in zip(*strs):
            if not all(col[i] <= col[i + 1] for i in range(len(col) - 1)):
                count += 1
        return count
