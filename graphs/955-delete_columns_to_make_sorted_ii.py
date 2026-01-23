#955. Delete Columns to Make Sorted II
#Medium
#
#You are given an array of n strings strs, all of the same length.
#
#We may choose any deletion indices, and we delete all the characters in those
#indices for each string.
#
#Suppose we chose a set of deletion indices answer such that after deletions,
#the final array has its elements in lexicographic order.
#
#Return the minimum possible value of answer.length.
#
#Example 1:
#Input: strs = ["ca","bb","ac"]
#Output: 1
#
#Example 2:
#Input: strs = ["xc","yb","za"]
#Output: 0
#
#Example 3:
#Input: strs = ["zyx","wvu","tsr"]
#Output: 3
#
#Constraints:
#    n == strs.length
#    1 <= n <= 100
#    1 <= strs[i].length <= 100
#    strs[i] consists of lowercase English letters.

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        """
        Greedy: keep column if it doesn't break order of unsettled pairs.
        """
        n = len(strs)
        m = len(strs[0])
        deleted = 0

        # settled[i] = True if strs[i] < strs[i+1] is already guaranteed
        settled = [False] * (n - 1)

        for col in range(m):
            # Check if keeping this column breaks any unsettled pair
            can_keep = True
            for i in range(n - 1):
                if not settled[i] and strs[i][col] > strs[i + 1][col]:
                    can_keep = False
                    break

            if can_keep:
                # Update settled status
                for i in range(n - 1):
                    if strs[i][col] < strs[i + 1][col]:
                        settled[i] = True
            else:
                deleted += 1

        return deleted


class SolutionExplicit:
    """More explicit tracking"""

    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        # For each adjacent pair, track if order is determined
        determined = [False] * (n - 1)
        deleted = 0

        for col in range(m):
            # Try to keep this column
            valid = True
            new_determined = determined[:]

            for i in range(n - 1):
                if determined[i]:
                    continue

                if strs[i][col] > strs[i + 1][col]:
                    valid = False
                    break
                elif strs[i][col] < strs[i + 1][col]:
                    new_determined[i] = True

            if valid:
                determined = new_determined
            else:
                deleted += 1

        return deleted
